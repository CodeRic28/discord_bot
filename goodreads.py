from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

def book_desc(message):
    driver.get("https://www.goodreads.com/")
    name = ''
    text = ''
    search = driver.find_element_by_id("sitesearch_field")
    search.send_keys(message)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
    table_list = driver.find_elements_by_class_name("tableList")
    for item in table_list:
        title = item.find_element_by_class_name("bookTitle").text
        author = item.find_element_by_class_name("authorName").text
        name = f'{title} by {author}'
        # print(title.text, 'by', author.text)
    # if "https://www.goodreads.com/search" in driver.current_url:
    #     driver.find_element_by_xpath(
    #         '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a/span').click()
    if "https://www.goodreads.com/search" in driver.current_url:
        driver.find_element_by_class_name("bookTitle").click()
    try:
        desc = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "descriptionContainer"))
        )

        driver.find_element_by_xpath('''//*[@id="description"]/a''').click()
        text = desc.find_element_by_id('description').text
        less_pos = text.find('(less)')
        text = text[:less_pos]
        driver.get("https://www.goodreads.com/")
    except:
        text = driver.find_element_by_id('description').text
        driver.get("https://www.goodreads.com/")

    return name, text


# print(book_desc('1984'))


# book_name = []
# auth_name = []
# title_head = driver.find_element_by_id("all_votes")
# titles = title_head.find_elements_by_class_name("bookTitle")
# authors = title_head.find_elements_by_class_name("authorName")
# for title in titles:
#     book_name.append(title.text)
# for author in authors:
#     auth_name.append(author.text)
# books = list(zip(book_name, auth_name))


# driver.close()
