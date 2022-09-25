from socket import timeout
import requests
import enum
 
from requests.structures import CaseInsensitiveDict
from http import HTTPStatus

HTTP_TKN_USER_AGENT = 'User-Agent'
HTTP_TKN_CONTENT_TYPE = 'Content-Type'
HTTP_TKN_ID_ENCODING = 'Id-Encoding'
HTTP_TKN_AUTHORIZATION = 'Authorization'
 

class ContentType(enum.Enum):
    APP_HTML = 1
    APP_JSON = 2
    APP_XML = 3
    APP_URL_ENC = 4


class EncodingType(enum.Enum):
    PLAIN = 0
    BASE64 = 1


def content_type(content_type):
    return {
        content_type.APP_HTML: 'application/html',
        content_type.APP_JSON: 'application/json',
        content_type.APP_XML: 'application/xml',
        content_type.APP_URL_ENC: 'application/x-www-form-urlencoded'
    }.get(content_type, 'application/html')


def encoding_type(encoding_type):
    return {
        encoding_type.PLAIN: '0',
        encoding_type.BASE64: '1'
    }.get(encoding_type, '0')


def header_agent(value):
    return HTTP_TKN_USER_AGENT, value


def header_content_type(value):
    return HTTP_TKN_CONTENT_TYPE, content_type(value)


def header_encoding_type(value):
    return HTTP_TKN_ID_ENCODING, encoding_type(value)


def header_authorization(value):
    return HTTP_TKN_AUTHORIZATION, value


#
#   format_header:
#       creates an https header
#
def format_header(**kwargs):
    header = CaseInsensitiveDict()
    for key, value in kwargs.items():
        methods = {
            'agent': header_agent,
            'content_type': header_content_type,
            'encoding_type': header_encoding_type,
            'authorization': header_authorization
        }
        if key in methods:
            http_header, http_value = methods[key](value)
            header[http_header] = http_value
    return header

#
#   post_request:
#       creates post request with no response-buffer
#
def post_request(url, headers, payload, cacerts, valid_responses, timeout=None):
    try:
        result = requests.post(url, data=payload, headers=headers, verify=cacerts, timeout=timeout )
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, None, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    return True, None, result.status_code
 
 
#
#   delete_request:
#       creates delete request with no response-buffer
#
def delete_request(url, headers, cacerts, valid_responses, timeout=None):
    try:
        result = requests.delete(url, headers=headers, verify=cacerts, timeout=timeout)
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, None, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    return True, None, result.status_code
 
#
#   get_request:
#       creates get request with response-buffer
#
def get_request(url, headers, cacerts, valid_responses, timeout=None):
    try:
        result = requests.get(url, headers=headers, verify=cacerts, timeout=timeout)
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, None, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    msg = result.json() if result else None
    return True, msg, result.status_code
 
 
#
#   put_request:
#       creates put request with no response-buffer
#
def put_request(url, headers, payload, cacerts, valid_responses, timeout=None):
    try:
        result = requests.put(url, data=payload, headers=headers, verify=cacerts, timeout=timeout)
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, None, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    return True, None, result.status_code
