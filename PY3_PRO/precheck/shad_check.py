from selenium.webdriver import Chrome
import time

# devices_mac2 = {'2028':'d0:76:8f:27:1c:05','2028_2':'d0:76:8f:27:1b:f5','4220':'48:77:46:bd:d5:75','2026':'44:65:7f:15:47:3e'}
# for device in devices_mac2:
#     print(devices_mac2)


chrome = Chrome()
chrome.implicitly_wait(10)
chrome.maximize_window()

shad_url = "https://stage.www.calix.ai/web/calixweb/sp-dashboard.html"
username = "felix.chang@calix.com"
password = "calix123"
devices_mac = ['d0:76:8f:27:1c:05','d0:76:8f:27:1b:f5','48:77:46:bd:d5:75','44:65:7f:15:47:3e']

def shad_login(url,username,passwd):
    chrome.get(url)
    chrome.find_element_by_id("email").send_keys(username)
    chrome.find_element_by_id("password").send_keys(passwd)
    chrome.find_element_by_id("sp-login-btn").click()
    chrome.find_element_by_xpath("//*[contains(text(),'Router Management')]").click()
    time.sleep(3)

def shad_search(device):
    chrome.find_element_by_id("macAddr").send_keys(device)
    try:
        chrome.find_element_by_xpath("//*[contains(text(),'Search')]").click()
        time.sleep(2)
        chrome.find_element_by_id("footer-btn-close").click()
        print(device + " is not onboard.")
    except Exception as err:
        # print(err)
        print(device + " is already onboard, please remove !")
    chrome.find_element_by_id("macAddr").clear()

def onboard_check(devices):
    for device in devices:
        shad_search(device)


shad_login(shad_url,username,password)
# shad_search("48:77:46:9a:04:cb")
onboard_check(devices_mac)
chrome.close()