from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "insiderCrawler"
    allowed_domains = ["www.tradingview.com"]
    start_urls = [
        "https://www.tradingview.com/news/corporate-activity/?section=insider_trading"
    ]

    rules = (
        Rule(
            LinkExtractor(allow="news/mtnewswires.com", deny="corporate-activity"),
            callback="parse_insider",
        ),
        Rule(LinkExtractor(allow="news"), callback="parse_news"),
    )

    def parse_insider(self, response):
        yield {
            "info": response.css(".title-KX2tCBZq::text").get(),
            "Symbol": response.css(".description-cBh_FN2P::text").get(),
        }


# test for git
