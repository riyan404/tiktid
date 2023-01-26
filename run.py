from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import random
import colorama,requests
from colorama import init
init()
colorama.init(autoreset=True)
from tiktok_downloader import snaptik
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
 
cwd = os.getcwd()

opts = webdriver.ChromeOptions()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")

opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
 
opts.add_argument('--no-sandbox')
 
opts.add_argument('--disable-setuid-sandbox')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certifcate-errors')
opts.add_argument('--ignore-certifcate-errors-spki-list')
#opts.add_argument('--disable-accelerated-2d-canvas')
opts.add_argument('--no-zygote')
opts.add_argument('--no-first-run')
opts.add_argument('--disable-dev-shm-usage')
opts.add_argument("--disable-infobars")
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-popup-blocking")
opts.add_argument('--log-level=3') 
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option("useAutomationExtension", False)
opts.add_experimental_option("excludeSwitches",["enable-automation"])
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
opts.add_argument('--disable-notifications')
 
def handle_url():
    element = wait(browser,35).until(EC.presence_of_element_located((By.XPATH, '//div[@data-e2e="user-post-item"]/div/div/a')))
    try_limit = 0
    urutan = 1
    list_url = []
    global success 
    success = []
    for i in range(1,999999):
        if try_limit == 5:
            break
        try:
            url_vid = wait(browser,9).until(EC.presence_of_element_located((By.XPATH, f'(//div[@data-e2e="user-post-item"]/div/div/a)[{i}]')))
            
            browser.execute_script("arguments[0].scrollIntoView();", url_vid)
            #with open('url.txt','a',encoding='utf-8') as f: f.write(f'{url_vid.get_attribute("href")}\n')
            print(f'[{urutan}] {url_vid.get_attribute("href")}')
            urutan = urutan+1
            list_url.append(url_vid.get_attribute("href"))
             
        except Exception as e:
            try:
                browser.execute_script("arguments[0].scrollIntoView();", url_vid)
            except:
                pass
            try_limit = try_limit + 1
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[+] Total All Video: {len(list_url)}")  
    number = 1
    for i in list_url:
        try:
            download(i,number)
            number = number + 1
        except Exception as e:
            print(e)
def download(url,number):
    
    file_list = "name.txt"
    myfile = open(f"{cwd}\\{file_list}","r")
    fold = myfile.read()
    if not os.path.exists(f"{cwd}\\Result\{fold}"):
        os.makedirs(f"{cwd}\\Result\\{fold}")
   
     
    headers ={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"105\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"105\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        #"cookie": ".AspNetCore.Antiforgery.FPqb9rLNMTY=CfDJ8EwS0UkJ03ZOthTIQLyF8IIzrvO-doR_Q2CNeLx88r3ib3VPl6duc-qpKbzMTn-1AhsaUpbIk1XzT7rd7jncbNAqttav8STwxIWmQ73D92xGnYaqY21gI07NW-9hKStS-_tBRXQcVUbKS7erXyYX7LM; .AspNetCore.Session=CfDJ8EwS0UkJ03ZOthTIQLyF8IJDpw5yKcaA%2FDiAxsH3zaFqpq7451zKepV9Ub31ULQGMIumDoJWI7UGFwletgzNw0EARvf6rr8%2BrKxxJPFPRQhRoN0qebyeufuX2IOlo2PCbZReK5BSAC6INADQDKPaVllobv0AEvyIdUPRJSLjfvyd; logglytrackingsession=a5c12b21-ab0f-4cbc-b65e-7743eaa6b377; .AspNetCore.Antiforgery.Lucky=23a8ae5c-311c-4784-a1bb-659718724b27",
        "Referer": "https://dltik.com/done?vid=7135124311030959365&source=tiktok&al=PVe_W-dKO2gSJLkq8E-7l_kEApHwT_VkMSAEdpILLBZXHdlztQxFm-BhqqbuTWMcOf6vmiyjm47VcOUDRzIW7A",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    } 
    
    browser.get(f"https://dltik.com/")
    wait(browser,9).until(EC.presence_of_element_located((By.XPATH, f'//input[@id="txt-input-url"]'))).send_keys(url)
    wait(browser,9).until(EC.presence_of_element_located((By.XPATH, f'//button[@id="btn-submit-link"]'))).click()
    sleep(2)
    id_vid = url.split("video/")
    id_vid = id_vid[1]
    results= requests.get(f"https://dltik.com/download?vid={id_vid}&source=tiktok", headers=headers)
    with open(f"{cwd}\\Result\\{fold}\\{id_vid}.mp4", 'wb') as f:
        for chunk in results.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)

    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[{number}] {url} Success Downloaded!")
     
    success.append(1)

    
def open_browser(url_tiktok):
    
    global browser
    global element
   
    random_angka = random.randint(100,999)
    random_angka_dua = random.randint(10,99)
     
    opts.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.{random_angka}.{random_angka_dua} Safari/537.36")

    browser = webdriver.Chrome(options=opts, desired_capabilities=dc)
   
    browser.get(f"https://www.tiktok.com/{url_tiktok}")
    handle_url()
    
    
if __name__ == '__main__':
 
    #print("[*] Automation Tiktok Download")
    print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[+] Mass Downloader All TikTok Video Without Watermark!") 
    while True:
        try:
            keyword = input(str(f"[+] Please Input Username TikTok target: "))
            
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[+] Trying to Get Total All {keyword} Video!")  

            try:
                name = keyword.split("tiktok.com/")

                name = name[1].split("@")
                
                try:
                    name = name[1].split("/video/")
                    name = name[0]
                    
                except Exception as e:
                    pass
                if "@" in keyword:
                    pass
                else:
                    name = "@"+name
            except:
                name = keyword
                if "@" in name:
                    pass
                else:
                    name = "@"+name
            with open('name.txt','w') as f:f.write(f"{name}")
            
            open_browser(name)
            global success 
            success = []
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[+] Success Download Total{success} Video!")  
        except Exception as e:
            print(e)
            print(colorama.Fore.GREEN + colorama.Style.BRIGHT + f"[+] All Done!")  
            break
