from selenium import webdriver
import time

try:
    driver = webdriver.Chrome(executable_path="/Users/omerk/Downloads/Newchromedriver")
    driver.get("http://127.0.0.1:5001/users/get_user_data/1")
    name = driver.find_element_by_id('user').text
    print(name)
except:
    print('Error!')

finally:
    time.sleep(3)
    driver.quit()

