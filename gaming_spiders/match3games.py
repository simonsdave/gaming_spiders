#!/usr/bin/env python

import json

from cloudfeaster import spider

from zygomatic import ZygomaticSpider


class Match3GamesSpider(ZygomaticSpider):

    @classmethod
    def get_metadata(cls):
        return {
            "url": "http://www.match3games.com/?sort=mostPlayed",
        }


if __name__ == "__main__":
    crawl_args = spider.CLICrawlArgs(Match3GamesSpider)
    crawler = spider.SpiderCrawler(Match3GamesSpider)
    crawl_result = crawler.crawl(*crawl_args)
    print json.dumps(crawl_result)
