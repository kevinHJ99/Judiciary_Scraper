from Judiciary_Scraper.utils.imports import *
from Judiciary_Scraper.utils.config_variables import * 
from Judiciary_Scraper.utils.selenium_functions import AutomationFunctions as af
from Judiciary_Scraper.scripts.scraper import find_results

## find file directory S
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


## find path from logs file directory   
search_path = '/' 
filename = 'scraper.log'
print("search directory")
file_path = find_file(filename, search_path)

## verify if path exists
if file_path:
    print(f'Found File: {file_path}')
    logging.basicConfig(filename=file_path, level=logging.INFO)
else:
    print('File not found')

# URLs lists, Lists of searchs Terms and XPaths
searchs = [
    (URL, ACTOR_RUC, ACTOR_INPUT_ID),
    (URL, DENFENDAT_RUC, DENFENDAT_INPUT_ID)
]

options = Options()

options.add_argument('--incognito') # execute chrome in incognito mode
options.add_argument('--no-sandbox') # disable sandbox
options.add_argument("--disable-gpu")  # disable use to GPU for better velocity
options.add_argument('--disable-infobars') # disable inforbars
options.add_argument('--disable-web-security') # reduce web page security
options.add_argument('--ignore-certificate-errors') # disable prevention certificates in web page 
options.add_argument(f"--user-agent={USER_AGENT['User-Agent']}") # inicialite driver with preferal user-agent
options.add_argument('--disable-blink-features=AutomationControlled') # disable chrome automation notification
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

for url, consults, id in searchs:
    for consult in consults:
        # Ejecutar búsqueda
        find_results(url, options, consult, id)
        # Intervalo aleatorio entre ejecuciones de las búsquedas
        sleep(ram.uniform(60, 120))
