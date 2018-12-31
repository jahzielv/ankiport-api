import main
import json
import ankiport_core

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
    res = api.post("/port?setID=" + qID)
    return res


def test_TextOnly_Name():
    '''
        Testing the download of a text only Quizlet set.
        Makes sure that the file downloaded has the correct name.
    '''
    expectedFileName = "french definitions.apkg"
    res = getTextOnlySet()
    print(str(res.headers))

    assert res.headers["x-filename"] == expectedFileName


def test_TextOnly_Size():
    '''
        Testing the download of a text only Quizlet set.
        Makes sure that the file downloaded has the correct filesize.
    '''
    res = getTextOnlySet()
    actualSize = len(res.data)

    assert actualSize != 0


def test_css():
    x = {"font-family": "arial", "color": "green"}
    actualVal = ankiport_core.quizlet_helper.makeCss(x)
    expected = ".card{font-family:arial;color:green;}"
    assert expected == actualVal
