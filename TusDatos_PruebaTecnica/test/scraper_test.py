from TusDatos_PruebaTecnica.utils.imports import *
from TusDatos_PruebaTecnica.utils.config_variables import * 
from TusDatos_PruebaTecnica.utils.selenium_functions import AutomationFunctions as af

# func: save_data
# args: 
    # - data: get data to parse html function
    # - ld(load_data): load json file with dict 
    # - RUC: save ruc with main key for Actor id
    # - process_id: save process id, with main key to Actor>RUC
# details: save judiciary actions and judiciary process details  
def save_data(data, ld, RUC, process_id):
    ## get the directory of the current script
    data_dir = os.getcwd()
    ## Build the path to the file data.json
    data_path = os.path.join(data_dir, '..', 'data', 'stored_data', 'data.json')

    ## ===============//=================
    if 'Cédula/RUC/Pasaporte del Actor/Ofendido' in data[process_id]['Tipo de Proceso']: 
        ld['Actor'][RUC].update(data)
    else:
        ld['Demandado'][RUC].update(data)

    with open(data_path, 'w') as file:
        json.dump(ld, file)

# func: items_controller
# args: 
    # - controller: get item id for controller the last item
    # - page: controller the curretn page in a variable
# details: this function controller pagination 
def items_controller(controller, page):
    
    while True:
        sleep(1)
        pagination = driver.find_element(By.XPATH, '//*[@aria-live="polite"]').text
        id = driver.find_elements(By.XPATH, '//*[@class="causa-individual ng-star-inserted"]//*[@class="id"]')
        item_id = [item.text for item in id]
    
        if pagination != page:
            print(pagination)
            af.do_clickByXpath(driver, '//button[@aria-label="Página siguiente"]')
            continue
        else:
           # Usar filter con una función lambda para obtener los elementos que son iguales a 'controller'
            filtered_items = list(filter(lambda x: x[1] == controller, enumerate(item_id)))
            # Formatear el resultado para obtener (índice, valor)
            result = [(index, value) for index, value in filtered_items]
            return result, pagination 

# func: do_get_html
# args: 
    # - driver: get driver to wwebdriver
    # - RUC: save ruc with main key for Actor id
# details: enter in url and get whole page to judiciary actions 
def do_get_html(driver, RUC):
    ## get actions click
    judiciary_actions = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lista-movimiento-individual ng-star-inserted"]'))
        )
    
    count = len(judiciary_actions)
    
    for i in range(count):
        sleep(3)
        af.do_clickByXpath(driver, '//div[@class="movimiento-individual ng-star-inserted"]['+str(i+1)+']//*[@class="actuaciones-judiciales"]/a') ## enter in judiciary actions
        print('enter in judiciary actions... ')
        sleep(1.5)
        driver.refresh()
        sleep(ram.randint(3, 7))
        ## get html to judiciary page 
        html = driver.page_source
        parse(html, RUC)
        sleep(2.5)
        driver.back()     

# func: find_results
# args: 
    # - driver: get driver to wwebdriver
    # - RUC: save ruc for search bar 
    # - INPUT_XPATH: get input xpath
# details: enter page and find items results 
def find_results(driver, RUC, INPUT_XPATH):
    ## find all process with the RUC 
    af.do_stringById(driver, INPUT_XPATH, RUC+Keys.ENTER)
    driver.set_page_load_timeout(15) ## wait page load 
    controller = 0
    page = ''
    count = 0
    while True:

        ## ===============//=================
        items = WebDriverWait(driver, 15).until( ## get amount items in whole page 
                EC.presence_of_element_located((By.XPATH, '//div[@class="mat-mdc-paginator-page-size-value ng-star-inserted"]'))
        ).text 
        pag = driver.find_element(By.XPATH, '//*[@aria-live="polite"]').text
        page = pag
        ## ===============//=================
        
        ## enter to judiciary
        for i in range(int(items)): 
            sleep(ram.uniform(3.5, 5.5))
            print(page)
            ic = items_controller(controller, page)
            if pag != page:
                page = ic[1]
                controller = int(ic[0][1])+1                
                af.do_clickByXpath(driver, '//div[@class="causa-individual ng-star-inserted"]['+str(ic[0][0]+1)+']//*[@class="detalle"]/a')
                do_get_html(driver, RUC)
                sleep(2.5)
                driver.back()
            else:
                item_id = driver.find_element(By.XPATH, '//*[@class="causa-individual ng-star-inserted"]['+str(i+1)+']//*[@class="id"]').text 
                controller=int(item_id)
                af.do_clickByXpath(driver, '//div[@class="causa-individual ng-star-inserted"]['+str(i+1)+']//*[@class="detalle"]/a')
                do_get_html(driver, RUC)
                sleep(2.5)
                driver.back()
            
        count+=1
        if count != 5: 
                try:
                    af.do_clickByXpath(driver, '//button[@aria-label="Página siguiente"]')
                except:
                    break
        else: break
            
# func: parse
# args: 
    # - html: get html to parse html page
    # - RUC: save ruc with main key for Actor id
# details: parse html and find details and judiciary actions
def parse(html, RUC):
    
    dom = af.do_get_dom_html(html) ## parse page
    
    ## get the directory of the current script
    data_dir = os.getcwd()
    ## Build the path to the file data.json
    data_path = os.path.join(data_dir, '..', 'data', 'stored_data', 'data.json')
    
    with open(data_path, 'r') as file: 
        load_data = json.load(file)

    process_id = dom.xpath(JUDGEMENT_ID_XPATH)[0]
    data = {
        process_id: {
            "Tipo de Proceso": dom.xpath(TYPE_PROCESS_XPATH)[0],
            "RUC del actor": dom.xpath(FILTER_ID_XPATH)[0],
            "Fecha Ingreso": dom.xpath(DATE_XPATH)[0],
            "Materia": dom.xpath(MATTER_TITLE)[0],
            "Tipo de Accion": dom.xpath(TYPE_ACTION_XPATH)[0],
            "Delito/Aunto": dom.xpath(SUBJECT_XPATH)[0],
            "Judicatura": dom.xpath(JUDICIARY_XPATH)[0],
            "Tipo de Ingreso": dom.xpath(INCOME_TYPE_XPATH)[0],
            "Numero de proceso vinculado": dom.xpath(NUMBER_PROCESS_XPATH),
            "Actor": dom.xpath(ACTOR_XPATH)[0],
            "Defensor": dom.xpath(DEFENDANT_XPATH),
        }
    }

    finally_data = {}

    ## generate actions list
    date, details, actions = [], [], []
        
    ## ===============//=================
    judiciary_actions_date = dom.xpath('//*[@role="button"]//span//span[1]')
    for jd in judiciary_actions_date:
        ja_date = jd.xpath(".//text()")
        date.append(ja_date[0])
    finally_data['date'] = date

    ## ===============//=================
    judiciary_actions_details = dom.xpath('//*[@class="mat-mdc-tooltip-trigger title"]')
    for jad in judiciary_actions_details: 
        ja_details = jad.xpath('.//text()')
        details.append(ja_details[0])
    finally_data['details'] = details
    
    ## ===============//=================
    judiciary_actions = dom.xpath('//mat-expansion-panel//*[@class="actividad pagina"]')
    for i in range(len(judiciary_actions)):
        p_actions = dom.xpath('//mat-expansion-panel['+str(i+1)+']//*[@class="actividad pagina"]') # iterate for this actions number
        for p in p_actions: 
            paragraph = p.xpath('.//text()')
        actions.append(''.join(paragraph))
    finally_data['actions'] = actions

    ## ===============//=================
    data[process_id].update({"Acciones Judiciarias":finally_data}) # save judiciary action in data
    
    ## ===============//=================
    save_data(data, load_data, RUC, process_id) #save data in json file