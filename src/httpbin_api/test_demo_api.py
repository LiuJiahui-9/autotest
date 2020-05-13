import pytest
import requests
import json
from .const import *

class Test_httpbin():

    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert LOCAL_IP == response_data["origin"]

    def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name":"gucun","pwd":"19990927"}
        r = requests.post(url,data=post_data)
        print(r.headers)
        print(r.text)
        requests_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == requests_data["form"]["name"]
        assert post_data["pwd"] == requests_data["form"]["pwd"]