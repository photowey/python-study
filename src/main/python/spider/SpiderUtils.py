# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file SpiderUtils.py
# @description the Utils in web crawlers
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


import http

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

from fake_useragent import UserAgent
import json


def populate_headers() -> dict:
    """
    populate chrome headers \n
    :rtype: dict
    """
    http_headers = {
        "User-Agent": UserAgent().chrome
    }

    return http_headers


def populate_request(url: str) -> Request:
    """
    populate request \n
    :param url: URL
    :return: Request
    :rtype request
    """
    http_headers = populate_headers()
    request = Request(url, headers=http_headers)

    return request


def handle_request_get(url: str) -> http.client.HTTPResponse:
    """
    handle the specific request \n
    :param url: the URL
    :return: the HTTPResponse
    """
    http_headers = populate_headers()
    request = Request(url, headers=http_headers)
    response = urlopen(request)

    return response


def handle_request_post(url: str, params: dict) -> http.client.HTTPResponse:
    """
    handle the specific request \n
    :param url: the URL
    :param params: the params of Request
    :return: the HTTPResponse
    """
    http_headers = populate_headers()
    form_data = urlencode(params).encode()
    request = Request(url, data=form_data, headers=http_headers)
    response = urlopen(request)

    return response


def request_html(url: str) -> http.client.HTTPResponse:
    """
    request html \n
    :param url: the URL
    :return: the byte of page's html
    """
    response = handle_request_get(url)

    return response


def save_html(file_name: str, html: bytes) -> None:
    """
    save the html to ./ \n
    :param file_name: the target file name
    :param html: the bytes of read html
    :return: None
    """
    with open(file_name, mode="wb", encoding="utf-8") as target:
        target.write(html)

    return


def save_text(file_name: str, html: str) -> None:
    """
    save the html to ./ \n
    :param file_name: the target file name
    :param html: the str of read html
    :return: None
    """
    with open(file_name, mode="a", encoding="utf-8") as target:
        target.write(html)

    return


def text_format(text: str, *args) -> str:
    """
    format the str \n
    :param text: the origin str
    :param args: the args
    :return: the formatted str
    """
    return text.format(*args)


def url_encode(url: str) -> str:
    """
    encode the url to %xx \n
    :param url: the URL
    :return: the encode URL
    :rtype str
    """
    return urlencode(url)


def content_encode(text: str) -> bytes:
    """
    encode the target text to bytes \n
    :param text: the target text
    :return: the bytes
    :rtype bytes
    """
    return text.encode()


def content_decode(content: bytes) -> str:
    """
    decode the target bytes to str \n
    :param content: the target bytes
    :return: the decode text
    :rtype str
    """
    return content.decode()


def to_json(content: str) -> dict:
    """
    deserialize the str to JSON object \n
    :param content: the target json str
    :return: the JSON object
    :rtype dict
    """
    return json.loads(content)


def to_json_str(content: dict) -> str:
    """
    serialize the JSON object to str \n
    :param content: the target JSON object
    :return: the JSON str
    :rtype str
    """
    return json.dumps(content, ensure_ascii=False)


def to_json_pretty(content: dict) -> str:
    """
    serialize the JSON object to str \n
    :param content: the target JSON object
    :return: the JSON str
    :rtype str
    """
    return json.dumps(content, sort_keys=True, indent=4, ensure_ascii=False)
