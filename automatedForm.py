#!/usr/local/bin/python3

import selenium
from selenium import webdriver      
from selenium.webdriver.common.keys import Keys
import time
import json
import os
#import pyvirtualdisplay
#from pyvirtualdisplay import Display
#from selenium import webdriver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH='./env/bin/chromedriver'

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path=os.getcwd() + '/env/bin/chromedriver', chrome_options=options)

#browser = webdriver.PhantomJS(executable_path=os.getcwd() + '/env/bin/phantomjs')
#browser = webdriver.Chrome(ChromeDriverManager().install())
#browser = webdriver.Chrome()


with open('filePaths.json') as f:
    paths = json.load(f)

#with open('testInput.json', encoding='utf-8') as data_file:
#    inputs = json.loads(data_file.read())
descriptionPath = '//*[@id="request-description-input"]'
picturePath = "//input[@type='file']"
submitPath = '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[9]/button[2]/span[1]'
finalSubmitPath = '/html/body/div[7]/div/div/div[2]/div[1]/form/div[1]/p/a'

#javascript to scroll view
scrollToViewScript = "arguments[0].scrollIntoView(true);"


def start():
    browser.get("https://topics.arlingtonva.us/reportproblem/")
    time.sleep(1)
    frame = browser.find_elements_by_tag_name("iframe")
    browser.switch_to.frame(frame[0])

#graffitiButton = browser.find_elements_by_link_text('Graffiti')
#print(graffitiButton)

def navigateToForm(problem):
    firstTypeSelect = browser.find_element_by_xpath(paths[problem]['address'])
    browser.execute_script(scrollToViewScript, firstTypeSelect)
    firstTypeSelect.click()

    nextButton = browser.find_element_by_xpath(paths[problem]['next'])
    browser.execute_script(scrollToViewScript, nextButton)
    nextButton.click()


def fillForm(inputs):
    problem = inputs['name']
    for key in paths[problem]['inputs'].keys():
        if(key!='description' and key!='picture'):
            tmpBox = browser.find_element_by_xpath(paths[problem]['inputs'][key])
            browser.execute_script(scrollToViewScript, tmpBox)
            tmpBox.send_keys(inputs[key])
        else:
            if(key=='description' and paths[problem]['inputs'][key]):
                descriptionBox = browser.find_element_by_xpath(descriptionPath)
                descriptionBox.send_keys(inputs["describe"])
            elif(key=='picture' and paths[problem]['inputs'][key]):
                picUpload = browser.find_element_by_xpath(picturePath)
                picUpload.send_keys(inputs[key])
    time.sleep(5)
    submitBox = browser.find_element_by_xpath(submitPath)
    submitBox.click()

    time.sleep(3)
    finalSubmit = browser.find_element_by_xpath(finalSubmitPath)
    #finalSubmit.click()

#navigateToForm(inputs['name'])
#fillForm(inputs)


#parkBox = browser.find_element_by_xpath(paths["Litter"]['inputs']['park'])
#parkBox.send_keys("Lyons Park")




#finalSubmit.click()


#image upload xpath: '/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/form/div[2]/div[6]/div/span[1]/input[2]'



"""     "Traffic": {
        "address": "",
        "next": "",
        "inputs": {
            "location": "",
            "street": "",
            "type": ""
        }
    } */ """