"""Zygomatic has a number of online gaming portals that all
seem to use the same platform. This module contains an asbstract
base class which will crawl sites generated by this platform.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from cloudfeaster import spider


class ZygomaticSpider(spider.Spider):

    def crawl(self, browser):
        max_num_games = 10

        ten_seconds = 10
        web_driver_wait = WebDriverWait(browser, ten_seconds)

        xpath = "//img[@class='card-img-top']"
        title_elements = web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        title_elements = title_elements[:max_num_games]
        titles = [title_element.get_attribute('alt') for title_element in title_elements]

        xpath = "//div[@class='card back']/a"
        link_elements = web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, xpath)))
        link_elements = link_elements[:max_num_games]
        links = [link_element.get_attribute('href') for link_element in link_elements]

        data = {}
        for rank in range(0, max_num_games):
            data[rank + 1] = {
                'title': titles[rank],
                'link': links[rank],
            }

        return spider.CrawlResponseOk(data)
