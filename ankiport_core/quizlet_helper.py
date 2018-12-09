import requests
import pprint
import json
import sys
import time
import os
import genanki
import random
import ankiport_core.gen_helper as gen_helper

DEBUG = 0

CLIENT_ID = ""
SECRET_KEY = ""

# Looks for a given file in a given directory.


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            print("found")
            return os.path.join(root, name)
        else:
            return None

# Verifies that you have a creds.txt file. Very unsafe, should probably
# be encrypted. I'll fix that soon.


def creds_file_exists():
    if (find("creds.txt", "./secrets") != None):
        with open("./secrets/creds.txt", 'r') as creds_file:
            global CLIENT_ID
            CLIENT_ID = creds_file.readline().replace("\n", "")
            global SECRET_KEY
            SECRET_KEY = creds_file.readline().replace("\n", "")
            print("id: " + CLIENT_ID)
            return True
    else:
        print("didn't find the file")
        return False


def getSet(setID):
    creds_file_exists()
    apiUrl = "https://api.quizlet.com/2.0/sets/{0}?client_id={1}&whitespace=1".format(setID,
                                                                                      CLIENT_ID)
    apiResponse = requests.get(apiUrl)
    if apiResponse.status_code:
        return json.loads(apiResponse.text)
    else:
        return None


def portSet(setID):
    qSet = getSet(setID)
    print(qSet)
    if (qSet == None):
        return (False, "FAILED")
    notes = []
    set_name = qSet["title"]
    for term in qSet['terms']:
        if DEBUG == 1:
            continue
        else:
            notes.append(gen_helper.makeNote(term['term'], term['definition']))

    # Make the Anki deck!
    gen_helper.makeDeck(set_name, notes)
    return (True, set_name)


def debug():
    # testing()
    # spinCurse()

    if not creds_file_exists():
        print("Verification failed")
    # verify_creds("jahziel_villasana8")
    # port("jahziel_villasana8", "2110 Final Exam")
    # my_notes = [gen_helper.makeNote()]
    # gen_helper.makeDeck("yote deck", my_notes)


def apiTest(string):
    return string * 4


if DEBUG == 1:
    # debug()
    find("creds.txt", "./")
