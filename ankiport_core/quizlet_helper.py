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
            return os.path.join(root, name)
        else:
            return None

# Verifies that you have a creds.txt file. Very unsafe, should probably
# be encrypted. I'll fix that soon.


def creds_file_exists():
    if (find("creds.txt", "./") != None):
        with open("creds.txt", 'r') as creds_file:
            global CLIENT_ID
            CLIENT_ID = creds_file.readline().replace("\n", "")
            global SECRET_KEY
            SECRET_KEY = creds_file.readline().replace("\n", "")
            return True
    else:
        return False


def verify_creds(usr_name):
    url2 = "https://api.quizlet.com/2.0/users/{0}/sets?client_id={1}&whitespace=1".format(
        usr_name, CLIENT_ID)
    # try to connect to the api; this will either return a 401 (bad login)
    # or the JSON with all the user's stuff.
    apiResponse = requests.get(url2)
    if apiResponse.status_code:
        # json representation of all the user's sets
        return json.loads(apiResponse.text)
    else:
        return None


def port(usr_name, set_name):
    all_sets = verify_creds(usr_name)
    if DEBUG == 1:
        print(all_sets)
    if (all_sets == None):
        return False  # TODO: make this raise a custom exception

    # Get the index of the set we're looking for
    index = 0
    for user_set in all_sets:
        if user_set["title"] == set_name:
            break
        index = index + 1
    if index >= len(all_sets):
        return False

    # Extract all the notes from the set
    notes = []
    for term in all_sets[index]['terms']:
        if DEBUG == 1:
            continue
        else:
            notes.append(gen_helper.makeNote(term['term'], term['definition']))

    # Make the Anki deck!
    gen_helper.makeDeck(set_name, notes)
    return True


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
    debug()
