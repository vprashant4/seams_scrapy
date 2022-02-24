import os
import random
import time

# selenium libraries
from selenium import webdriver
from scrapy.utils.project import get_project_settings

import scrapy
from samsscraper.items import SamsscraperItem
from scrapy.loader import ItemLoader



class SamsSpider(scrapy.Spider):
    # name of the spider
    name = "sams"

    def start_requests(self):
        # create chrome driver
        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(driver_path, options=options)
        # go to website
        driver.get("https://in.seamsfriendly.com/collections/shorts")
        Loading_products_page_two = driver.find_elements_by_xpath('//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[4]/div/div[3]/div[2]/button')
        Loading_products_page_two[0].click()
        time.sleep(5)
        Loading_products_page_three = driver.find_elements_by_xpath('//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[4]/div/div[3]/div[2]/button')
        Loading_products_page_three[0].click()
        time.sleep(5)

        xpath = '//*[@id="shopify-section-collection-template"]/section/div[3]/div[2]/div[2]/div[2]//a[text()]'
        link_elements = driver.find_elements_by_xpath(xpath)

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)

        driver.quit()

    def parse(self, response, **kwargs):
        item = SamsscraperItem()
        item['title'] = response.xpath("//meta[@name='twitter:title']/@content").get()
        item['description'] = response.xpath("//meta[@name='twitter:description']/@content").get()
        item['price'] = response.xpath("/html/head/meta[14]/@content").get()
        item['image_all'] = response.css('div.AspectRatio.AspectRatio--withFallback img::attr(src)').getall()


        yield item

