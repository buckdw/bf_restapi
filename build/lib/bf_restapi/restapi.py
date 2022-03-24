import json
import requests
 
from requests.structures import CaseInsensitiveDict
from http import HTTPStatus
 
HTTP_TKN_USER_AGENT = 'User-Agent'
HTTP_TKN_CONTENT_TYPE = 'Content-Type'
HTTP_TKN_ID_ENCODING = 'Id-Encoding'
HTTP_TKN_AUTHORIZATION = 'Authorization'
 
#
#   post_request:
#       creates post request with no response-buffer
#
def post_request(url, headers, payload, cacerts, valid_responses):
    try:
        result = requests.post(url, data=payload, headers=headers, verify=cacerts)
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
def delete_request(url, headers, cacerts, valid_responses):
    try:
        result = requests.delete(url, headers=headers, verify=cacerts)
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, msg, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    return True, None, result.status_code
 
#
#   get_request:
#       creates get request with response-buffer
#
def get_request(url, headers, cacerts, valid_responses):
    try:
        result = requests.get(url, headers=headers, verify=cacerts)
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
def put_request(url, headers, payload, cacerts, valid_responses):
    try:
        result = requests.put(url, data=payload, headers=headers, verify=cacerts)
    except requests.exceptions.HTTPError:
        return False, result.json(), result.status_code
    except:
        return False, None, HTTPStatus.INTERNAL_SERVER_ERROR
    if result.status_code not in valid_responses:
        return False, None, result.status_code
    return True, None, result.status_code
