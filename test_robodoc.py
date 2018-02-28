from robodoc.robodoc import FormatSpider
from scrapy.http import HtmlResponse, Request


def test_xslx():
    url = 'http://www.example.com/spreadsheet.xlsx'
    body = 'xml_spreadsheet'

    request_headers = {
        'Referer': 'http://www.example.com/'}
    request = Request(url=url, headers=request_headers)

    response_headers = {
        'Last-Modified': b'Mon, 20 Nov 1995 19:12:08 -0500'}
    response = HtmlResponse(
        url=url, headers=response_headers, request=request, body=body,
        encoding='utf-8')

    spider = FormatSpider()
    actual = next(spider.parse_item(response))['document_url']
    assert actual == url
