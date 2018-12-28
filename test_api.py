import main
import json

api = main.getApp().test_client()


def test_basic():
    '''
        Simple test to make sure the API connects.
    '''
    res = api.get("/test")
    resObj = json.loads(res.data)

    assert {"this_page": "API test"} == resObj


def getTextOnlySet():
    '''
        Downloads a text only Quizlet for use in testing.
        The set being used to test is found at https://quizlet.com/266087552/french-definitions-flash-cards/.
    '''
    # api = main.getApp().test_client()
    qID = "266087552"
    res = api.get("/port?setID=" + qID)
    return res


def test_TextOnly_Name():
    '''
        Testing the download of a text only Quizlet set.
        Makes sure that the file downloaded has the correct name.
    '''
    expectedFileName = "french definitions.apkg"
    res = getTextOnlySet()

    assert res.headers["x-filename"] == expectedFileName


def test_TextOnly_Size():
    '''
        Testing the download of a text only Quizlet set.
        The set being used to test is found at https://quizlet.com/266087552/french-definitions-flash-cards/.
        Makes sure that the file downloaded has the correct filesize.
    '''
    expectedFileSize = 53466
    res = getTextOnlySet()
    actualSize = len(res.data)

    assert actualSize != 0 and actualSize == expectedFileSize
