from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome = Chrome()
chrome.implicitly_wait(10)
chrome.maximize_window()

csc_url = "https://cloud-stg2.calix.com"
username = "test@calix.com"
password = "Admin123"
devices_id = ['CXNK0088AD99','CXNK0088AD97','CXNK007A3F67','CXNK005A964E']
subscribers = []
for device in devices_id:
    subscribers.append('autotest_'+device)

def CSC_login(url,username,passwd):
    chrome.get(url)
    chrome.find_element_by_name("username").send_keys(username)
    chrome.find_element_by_xpath("//*[@type='submit']").click()
    chrome.find_element_by_name("password").send_keys(passwd)
    chrome.find_element_by_xpath("//*[@type='submit']").click()
    # time.sleep(10)
    try:
        ok_btn = WebDriverWait(chrome, 20, 0.5).until(EC.presence_of_element_located((By.ID, '92715395-d27b-725c-0d6f-75335af45705')), 'no ok_btn')
        ok_btn.click()
    except Exception as err:
        print(err)

def CSC_search(device):
    subscriber = "autotest_"
    chrome.find_element_by_id("inputKey").send_keys(device)
    chrome.find_element_by_id("searchKey").click()
    time.sleep(2)
    try:
        # chrome.find_element_by_xpath("//*[contains(text(),'No matching subscriber found')]")
        chrome.find_element_by_xpath("//*[contains(text(),'%s')]" %subscriber)
        print(subscriber + device + " is existed, please delete it !")
    except Exception as err:
        # print(err)
        print(subscriber + device + " is not found, env is clean.")
    # chrome.refresh()
    chrome.find_element_by_id("inputKey").clear()

def sub_check(devices):
    for device in devices:
        CSC_search(device)

def secure_check():
    chrome.find_element_by_id("netops").click()
    chrome.find_element_by_id("policies").click()
    chrome.find_element_by_id("secure-onboarding").click()
    status = chrome.find_element_by_id("org-secure-onboarding-switch").is_selected()

    if status is True:
        chrome.find_element_by_xpath("//input[@id='org-secure-onboarding-switch']/../span").click()
        chrome.find_element_by_id("submit-org-secure-onboarding-policy-btn").click()
        status = chrome.find_element_by_id("org-secure-onboarding-switch").is_selected()
        print("Close and Secure onboard is " + str(status))
    else:
        print("Secure onboard is already " + str(status))

CSC_login(csc_url,username,password)
sub_check(devices_id)
secure_check()
chrome.close()