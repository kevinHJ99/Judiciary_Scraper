from Judiciary_Scraper.utils.imports import *
from Judiciary_Scraper.utils.config_variables import * 
from Judiciary_Scraper.utils.selenium_functions import AutomationFunctions as af
from Judiciary_Scraper.test.scraper_test import find_results

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


driver = af.set_up_Chrome(URL, options)
sleep(ram.uniform(3.5, 6.5))
find_results(driver, ACTOR_RUC[0], ACTOR_INPUT_ID)
