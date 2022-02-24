# import os
# import random
import time

# selenium libraries
from selenium import webdriver
from scrapy.utils.project import get_project_settings

import scrapy
from samsscraper.items import SamsscraperItem
# from scrapy.loader import ItemLoader


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
        loading_products_page_two = driver.find_elements_by_xpath('//button[text()="Load more products"]')
        loading_products_page_two[0].click()
        time.sleep(5)
        loading_products_page_three = driver.find_elements_by_xpath('//button[text()="Load more products"]')
        loading_products_page_three[0].click()
        time.sleep(5)

        xpath = '//*[@class="ProductItem__Title Heading"]/a'
        link_elements = driver.find_elements_by_xpath(xpath)

        for link in link_elements:
            yield scrapy.Request(link.get_attribute('href'), callback=self.parse)

        driver.quit()

    def parse(self, response, **kwargs):
        item = SamsscraperItem()
        item['title'] = response.xpath("//meta[@name='twitter:title']/@content").get()
        item['description'] = response.xpath("//meta[@name='twitter:description']/@content").get()
        item['price'] = response.xpath("//meta[@property='product:price:amount']/@content").get() # /html/head/meta[14]/@content
        item['image_all'] = response.css('div.AspectRatio.AspectRatio--withFallback img::attr(src)').getall()
        yield item

