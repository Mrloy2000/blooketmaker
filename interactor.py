#from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep



class Interactor():

    def __init__(self):
        self.action = ''
        self.driver = ''
    def interact_with(self,sleep_time,xpath,driver_input,question_list,question_index):
     
            action = self.action
            self.driver = driver_input
            interactable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
            interactable.click()
            sleep(sleep_time)
            action.send_keys(question_list[question_index]).perform()
    def click(self,xpath,sleep_time = 0):
           interactable = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,xpath)))
           sleep(sleep_time)
           interactable.click()








