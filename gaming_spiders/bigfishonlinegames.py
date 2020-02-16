#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import json
import sys

from cloudfeaster import spider


class BigFishOnlineGamesSpider(spider.Spider):

    @classmethod
    def get_metadata(cls):
        return {
            'url': 'http://www.bigfishgames.com/online-games/index.html',
        }

    def crawl(self, browser):

        data = {}

        for rank in range(1, 10):
            locator_fmt = (
                "//dl[contains(@class, 'game_list') and contains(@class, 'rank_list') and contains(@class, 'js_sort')]"
                "/dt/span[text()='%d']/../../dd/a"
            )
            locator = locator_fmt % rank
            link_element = browser.find_element_by_xpath(locator)
            link = link_element.get_attribute("href")
            title = link_element.get_text()

            data[rank] = {
                "title": title,
                "link": link,
            }

        return spider.CrawlResponseOk(data)


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(BigFishOnlineGamesSpider)
    crawler = spider.SpiderCrawler(BigFishOnlineGamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print(json.dumps(crawl_result))
    sys.exit(1 if crawl_result.status_code else 0)
