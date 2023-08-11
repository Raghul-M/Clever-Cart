from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random
from datetime import datetime
def flipkart_input(prod_val:str):
    prod_name = prod_val
    driver = webdriver.Chrome()
    web_link ="https://www.flipkart.com/"
    driver.get(web_link)
    try:
        cross = driver.find_element(By.XPATH, '//button[@class="_2KpZ6l _2doB4z"]').click()
        time.sleep(5)


    except Exception as e:
        pass
    search_val = driver.find_element(By.TAG_NAME, "input")
    search_val.send_keys(prod_val)
    search_btn = driver.find_element(By.TAG_NAME, "button")
    search_btn.click()
    time.sleep(5)
    product_nav = driver.find_element(By.XPATH, "//a[(@class='_1fQZEK')]")
    product_nav.click()
    time.sleep(2)
    product_source = driver.page_source
    soup = BeautifulSoup(product_source, 'html.parser')
    #print(soup.prettify())
    time.sleep(3)
    product_description = soup.find(class_="_4rR01T").text
    global_ratings =soup.find(class_="_2_R_DZ").text
    product_price = soup.find("div", class_="_30jeq3")
    product_star_rating = soup.find('div', class_="_3LWZlK")
    image_element = driver.find_element(By.XPATH, '//img[@class="_396cs4"]')
    product_global_rating =re.search(r"([\d,]+)", global_ratings).group(1)
    product_global_ratings=product_global_rating.replace(",", "")
    # Extract the image URL from the src attribute
    product_img_src = image_element.get_attribute("src")

    try:
        print("Product Description:", product_description)
    except Exception as e:
        print("Product Description: Not Available")
    print("Product Price: ",str(product_price.text).strip())
    print("Product Star ratings :", product_star_rating.text.strip())
    print("Product Global ratings:", product_global_ratings)
    print("Product Image Link :", product_img_src)

    flipkart_result = {
        "product_description": product_description,
        "product_price": str(product_price.text).strip(),
        "product_star_ratings": product_star_rating.text.strip(),
        "product_global_ratings": product_global_ratings,
        "product_img_src": product_img_src
    }
    return flipkart_result