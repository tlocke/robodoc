from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime as Datetime
from collections import OrderedDict
from email.utils import parsedate_to_datetime


def format_date(dt):
    return '' if dt is None else dt.strftime("%Y-%m-%d %H:%M")


def make_line(response, extension, is_open):
    last_modified = format_date(
        parsedate_to_datetime(
            response.headers['Last-Modified'].decode('utf8')))

    return OrderedDict(
        (
            ('open_format', is_open),
            ('document_url', response.url),
            ('file_extension', extension),
            ('last_modified', last_modified),
            ('page_url', response.request.headers['Referer']),
            ('crawl_timestamp', format_date(Datetime.utcnow()))))


class FormatSpider(CrawlSpider):
    name = "RoboDoc"
    allowed_domains = ['www.gov.uk']
    start_urls = ['https://www.gov.uk/']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 80000}
    rules = (
        Rule(
            LinkExtractor(allow=(r'.*', ), deny_extensions=()),
            follow=True, callback='parse_item'),)

    def parse_item(self, response):
        extension = response.url.split('.')[-1].lower()
        # print('extension', extension, file=sys.stderr)
        if extension in ('xls', 'xlsx', 'doc', 'docx', 'ppt', 'pptx'):
            yield make_line(response, extension, False)
        elif extension in ('ods', 'odt', 'odp'):
            yield make_line(response, extension, True)
