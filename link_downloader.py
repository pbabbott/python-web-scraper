from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

login_url = 'https://thrivelife.com/myoffice'
username = ''
password = ''

driver = webdriver.Chrome()  

def quit_chrome():
    driver.quit()

def login_to_thrive():
    driver.get(login_url)
    time.sleep(2) 
    username_input_box = driver.find_element_by_id('email')
    password_input_box = driver.find_element_by_id('password')

    username_input_box.send_keys(username)
    password_input_box.send_keys(password)

    password_input_box.submit()

def get_customer_link(customer_id):
    time.sleep(1) 
    driver.get(f'https://www.thrivelife.com/myoffice/reports/index?report_key=customersdetails&customerId={customer_id}')
    
    paragraphs = driver.find_elements_by_tag_name('p')
    referral_link = 'NONE'
    for p in paragraphs:
        paragraph_text = p.text

        if ("REFERRAL LINK" in paragraph_text):
            clean_text = paragraph_text.replace('REFERRAL LINK', '')
            clean_text = "".join(clean_text.split())
            referral_link = clean_text
            break

    return referral_link
    

def test():
    login_to_thrive()
    get_customer_link('952604')
    quit_chrome()


