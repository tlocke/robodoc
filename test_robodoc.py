from robodoc.robodoc import FormatSpider
from scrapy.http import HtmlResponse, Request


def test_xslx():
    url = 'http://www.example.com/'

    body = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p><a href="spreadsheet.xlsx">Spreadsheet</a></p>
  </body>
</html>
"""

    response = HtmlResponse(
        url=url, request=Request(url=url), body=body, encoding='utf-8')

    spider = FormatSpider()
    actual = next(spider.parse_item(response))['document_url']
    assert actual == url + 'spreadsheet.xlsx'
