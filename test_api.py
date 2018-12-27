import main
import json


def test_basic():
    api = main.getApp().test_client()
    res = api.get("/test")
    resObj = json.loads(res.data)

    assert {"this_page": "API test"} == resObj
