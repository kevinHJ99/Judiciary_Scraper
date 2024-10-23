from Judiciary_Scraper.utils.imports import *

## get the directory of the current script
config_dir = os.getcwd()

## Build the path to the file config.yaml
config_path = os.path.join(config_dir, '..', 'config', 'config.yaml')

## open file config.yaml in read mode
with open(config_path, 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

## Wait time
WT = config['scraper']['wait_time']
WAIT_TIME = sleep(ram.uniform(WT[0], WT[1]))


## generate global variables
ACTOR_RUC = config['actor_ruc']
DENFENDAT_RUC = config['defendant_ruc']
URL = config['url']
ACTOR_INPUT_ID = config['elements_by_id']['actor_input_id']
DENFENDAT_INPUT_ID = config['elements_by_id']['defendant_input_id']
RETRIES = config['scraper']['retries']
TIME_LOAD = config['scraper']['time_load']
TIME_OUT = config['scraper']['time_out_request']
USER_AGENT = config['scraper']['user_agent']
SAVE_DATA = config['save_data']

## all items xpath
JUDICIARY_ACTIONS_XPATH = config['elements_by_xpath']['judgement_actions_xpath']
TYPE_PROCESS_XPATH = config['elements_by_xpath']['type_process_xpath']
FILTER_ID_XPATH = config['elements_by_xpath']['filter_id_xpath']
JUDGEMENT_ID_XPATH = config['elements_by_xpath']['judgement_id_xpath']
DATE_XPATH = config['elements_by_xpath']['date_xpath']
MATTER_TITLE = config['elements_by_xpath']['matter_title']
TYPE_ACTION_XPATH = config['elements_by_xpath']['type_action_xpath']
SUBJECT_XPATH = config['elements_by_xpath']['subject_xpath']
JUDICIARY_XPATH = config['elements_by_xpath']['judiciary_xpath']
INCOME_TYPE_XPATH = config['elements_by_xpath']['income_type_xpath']
NUMBER_PROCESS_XPATH = config['elements_by_xpath']['number_process_xpath']
ACTOR_XPATH = config['elements_by_xpath']['actor_xpath']
DEFENDANT_XPATH = config['elements_by_xpath']['defendant_xpath']
