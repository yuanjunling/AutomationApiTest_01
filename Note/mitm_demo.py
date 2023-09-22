# coding=utf-8
from mitmproxy import http

def request(flow):
    request_data=flow.request
    request_url=request_data.url
    print('url------------>',request_url)


