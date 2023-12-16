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

def amazon_input(prod_val:str):
    prod_name = prod_val
    driver = webdriver.Chrome()
    web_link ="https://www.amazon.in/"
    driver.get(web_link)
    try:
        search_val= driver.find_element(By.ID,"twotabsearchtextbox")
        search_val.send_keys(prod_val)
        search_btn = driver.find_element(By.ID, "nav-search-submit-button")
        search_btn.click()
    except Exception as e:
        search_val = driver.find_element(By.ID, "nav-bb-search")
        search_val.send_keys(prod_val)
        search_btn = driver.find_element(By.CLASS_NAME, "nav-bb-button")
        search_btn.click()


    product_nav = driver.find_element(By.XPATH,"//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
    product_nav.click()
    time.sleep(3)
    product_source = driver.page_source
    soup = BeautifulSoup(product_source, 'html.parser')
    #print(soup)
    product_price = soup.find("span",class_="a-price-whole")
    product_price_symbol = soup.find('span', class_="a-price-symbol")
    star_rating = soup.find('span',class_="a-icon-alt").text
    product_img_link = soup.find('img',class_='s-image')
    product_img_src=product_img_link.get('src')
    try:
        product_description = soup.find(class_='a-size-medium a-color-base a-text-normal').get_text()
    except Exception as e:
        product_description = soup.find(class_='a-size-large product-title-word-break').get_text()
    product_global_ratings = soup.find(class_="a-size-base s-underline-text").get_text()
    #print(star_rating)
    product_star_rating = re.match(r"([\d.]+)", star_rating).group(1)
    print("val:",product_description)
    #print(product_star_rating)

    print("Product Description:", product_description)
    print("Product Price: " + str(product_price_symbol.text) + str(product_price.text.strip()))
    print("Product Star ratings :", product_star_rating)
    print("Product Global ratings:", product_global_ratings)
    print("Product Image Link :",product_img_src)

    amazon_result = {
        "product_description": product_description,
        "product_price": str(product_price_symbol.text) + str(product_price.text.strip()),
        "product_star_ratings": product_star_rating,
        "product_global_ratings": product_global_ratings,
        "product_img_src": product_img_src
    }
    driver.quit()
    return amazon_result

