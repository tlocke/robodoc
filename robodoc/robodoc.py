from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(CrawlSpider):
    name = "RoboDoc"
    allowed_domains = ['www.gov.uk']
    start_urls = [
        'https://www.gov.uk/government/publications/'
        'annual-return-spreadsheet-template-for-isa-managers']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 10}
    rules = (
        Rule(
            LinkExtractor(allow=(r'.*', )),
            follow=True, callback='parse_item'),)

    def parse_item(self, response):
        violations = {}
        for anchor in response.xpath('//a'):
            href = anchor.xpath('@href').extract_first()
            parts = href.split('.')
            if len(parts) > 1:
                extension = parts[-1]
                if extension in ('xls', 'xslx', 'doc', '.docx'):
                    violations[href] = {
                        'page': response.url,
                        'extension': extension,
                        'href': href}

        # print("violations", violations, file=sys.stderr)
        for violation in violations.values():
            yield violation
