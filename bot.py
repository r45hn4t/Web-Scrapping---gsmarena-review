from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from pprint import pprint

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # Line 14,15 necessary for chromedriver closing
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(7)

# phone = input("Enter Phone Model: ").lower()
driver.minimize_window()
phone = "redmi"
driver.get("https://www.gsmarena.com/")
search = driver.find_element(By.ID,"topsearch-text")
search.clear()
search.send_keys(phone)
search.send_keys(Keys.ENTER)
results = driver.find_elements(By.TAG_NAME,"strong")
results[0].click()
model_name = driver.find_element(By.CLASS_NAME,"specs-phone-name-title")
expand_all_reveiws = driver.find_element(By.CSS_SELECTOR,"a[class='button']")
expand_all_reveiws.click()
all_reviews = []
review_no=1
while bool(driver.find_elements(By.LINK_TEXT,"»")):
    next_page = driver.find_elements(By.LINK_TEXT,"»")[0]
    reviews = driver.find_elements(By.CLASS_NAME,"uopin")
    for review in reviews:
        try:
            print(str(review_no)+": \n"+review.text.replace("\n","")+" \n \n")
        except UnicodeEncodeError:
            print("Unsupported character")
        review_no+=1
    next_page.click()

driver.close()
# for reviews in all_reviews:
#     for review in reviews:
#         pprint(review.text)




