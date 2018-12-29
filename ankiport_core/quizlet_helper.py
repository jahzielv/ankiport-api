import requests
import pprint
import json
import sys
import time
import os
import genanki
import random
from ankiport_core.gen_helper import DeckGenerator

CLIENT_ID = ""
SECRET_KEY = ""


deckGen = DeckGenerator()


def find(name, path):
    """
        Looks for a given file in a given directory.
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        else:
            return None


def creds_file_exists():
    """
        Verifies that you have a creds.txt file.
    """
    if (find("creds.txt", "./secrets") != None):
        with open("./secrets/creds.txt", 'r') as creds_file:
            global CLIENT_ID
            CLIENT_ID = creds_file.readline().replace("\n", "")
            global SECRET_KEY
            SECRET_KEY = creds_file.readline().replace("\n", "")
            return True
    else:
        print("didn't find the creds file")
        return False


def getSet(setID):
    creds_file_exists()
    apiUrl = "https://api.quizlet.com/2.0/sets/{0}?client_id={1}&whitespace=1".format(setID,
                                                                                      CLIENT_ID)
    apiResponse = requests.get(apiUrl)
    if apiResponse.status_code == 404:
        return None
    else:
        return json.loads(apiResponse.text)


def portSet(setID):
    qSet = getSet(setID)
    if (qSet == None):
        return (False, 404)
    notes = []
    set_name = qSet["title"]
    for term in qSet['terms']:
        notes.append(deckGen.makeNote(term['term'], term['definition']))

    # Make the Anki deck!
    ret_bytes = deckGen.makeDeckBytes(set_name, notes)
    return (True, set_name, ret_bytes)
