import os
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from time import sleep
from interactor import Interactor

# Opens question file then extracts the info and closes it

#Initializes browser

directory = 'C:/Users/Loye/OneDrive/Desktop/Code/Python_projects/Actual_projects/Comptia/'
#directory = input("Input directory: (syntax drive://file//lo//cation.txt)")
#"C:/Users/Loye/OneDrive/Desktop/Comptia/CompTIA unit 4.5 questions.txt"

        
'''
driver = webdriver.Edge()
action = ActionChains(driver)
question_input = Interactor()

#Opens browser link
driver.get("https://dashboard.blooket.com/my-sets")
'''
#opens all files in the directory and iterates through them
for files in os.listdir(directory):
    name = files.split()
    
    #name.remove('questions.txt')
    name = ' '.join(name)
    

    with open (directory+files,'r',encoding='utf-8') as questions:
        list_of_questions = questions.readlines()
        
        for vals in list_of_questions:
            
            
            if vals.split() in ['â—¦\n','\n','â€¢\n','*','\ufeff\n',''] :
               list_of_questions.remove(vals.split())
            
            list_of_questions[list_of_questions.index(vals)] = list_of_questions[list_of_questions.index(vals)].split()
        print(list_of_questions)
        questions.close()
   
    #Xpaths for the inputs and buttons nececarry
    '''xpath_dictionary = {
    'title input xpath': '//*[@id="app"]/div/div/div[7]/form/div[1]/div[2]/input',
    'create button xpath':'//*[@id="app"]/div/div/div[7]/form/div[3]/div',
    'add question button xpath':'//*[@id="app"]/div/div/div[7]/div/div[1]/div[2]/div[1]',
    'quesiton input xpath':'//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[1]/div[2]',
    'answer 1 input xpath':'//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[1]/div/div[2]',
    'answer 2 input xpath':'//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[2]/div/div[2]',
    'answer 3 input xpath': '//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[3]/div/div[2]',
    'answer 4 input xpath':'//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[2]',
    'answer 4 check xpath':'//*[@id="app"]/div/div/div[8]/div/div/div[3]/div[2]/div[4]/div/div[1]/div[1]',
    'save button xpath' : '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[2]',
    'save set xpath':'//*[@id="app"]/div/div/div[7]/div/div[1]/div[1]/div[5]',
    'escape button xpath': '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[1]',
    'cancel button xpath':  '//*[@id="app"]/div/div/div[8]/div/div/div[2]/div[2]/div[1]/',
    'input password':'/html/body/main/div[2]/div[2]/form/div[2]/input',
    'input user':'/html/body/main/div[2]/div[2]/form/div[1]/input',
    'create set':'/html/body/div[1]/div/div/div[1]/a[6]'
    }
    #question_input.interact_with(0.2,xpath_dictionary['input password'],driver,input('Password: '), 0)
    #question_input.interact_with(0.2,xpath_dictionary['input user'],driver,input('Username: '), 0)
    title_maker = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath_dictionary['title input xpath']))
    )
    create_button =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_dictionary['create button xpath']))
    )



    #Sends the file name as the title for the blooket
    #title_maker.send_keys(input("What is the name for the blooket"))
    title_maker.send_keys(name)
    create_button.click()
    add_question_button =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_dictionary['add question button xpath']))
    )
    sleep(5)
    add_question_button.click()

    question_index = 0
    question_input.action = action


    sleep(5)
  #Iterates through all the question texts and inputs them then saves the blooket then clicks create set
    
    for vals in range(int((len(list_of_questions)/5))):
       try: 
            question_input.interact_with(0.1,xpath_dictionary['quesiton input xpath'],driver,list_of_questions,question_index)
            question_input.interact_with(0.1,xpath_dictionary['answer 1 input xpath'],driver,list_of_questions,question_index+1)
            question_input.interact_with(0.1,xpath_dictionary['answer 2 input xpath'],driver,list_of_questions,question_index+2)
            question_input.interact_with(0.1,xpath_dictionary['answer 3 input xpath'],driver,list_of_questions,question_index+3)
            question_input.interact_with(0.1,xpath_dictionary['answer 4 input xpath'],driver,list_of_questions,question_index+4)
            question_input.click(xpath_dictionary[ 'answer 4 check xpath'],0.5)
        
       except:
            question_input.click(xpath_dictionary[ 'cancel button xpath'],0.1)
       finally:
           print('question done')
       question_input.click(xpath_dictionary['save button xpath'],0.2)
       question_input.click(xpath_dictionary['add question button xpath'],3)
       question_index+=5
    question_input.click(xpath_dictionary['escape button xpath'])
    question_input.click(xpath_dictionary['save set xpath'],5)
    question_input.click(xpath_dictionary['create set'],5)
    print("Blooket done")
    '''
