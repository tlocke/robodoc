from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime as Datetime
from urllib.parse import urljoin
from collections import OrderedDict


class FormatSpider(CrawlSpider):
    name = "RoboDoc"
    allowed_domains = ['www.gov.uk']
    start_urls = ['https://www.gov.uk/']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 20000}
    rules = (
        Rule(
            LinkExtractor(allow=(r'.*', )),
            follow=True, callback='parse_item'),)

    def parse_item(self, response):
        problems = {}
        for anchor in response.xpath('//a'):
            href = anchor.xpath('@href').extract_first()
            parts = href.split('.')
            if len(parts) > 1:
                extension = parts[-1]
                if extension in ('xls', 'xlsx', 'doc', 'docx'):
                    problems[href] = OrderedDict(
                        (
                            ('document_url', urljoin(response.url, href)),
                            ('file_extension', extension),
                            ('link_url', response.url),
                            (
                                'crawl_timestamp',
                                Datetime.utcnow().strftime("%Y-%m-%d %H:%M"))))

        # print("problems", problems, file=sys.stderr)
        for problem in problems.values():
            yield problem
