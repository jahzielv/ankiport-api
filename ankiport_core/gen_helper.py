import genanki
import random
import json


def gen_id():
    return random.randrange(1 << 30, 1 << 31)


my_model = genanki.Model(
    gen_id(),
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    # css=[
    #     {
    #         ".card":{
    #             'font-family': 'arial',
    #             'font-size': '60px',
    #             'text-align': 'center',
    #             'color': 'black',
    #             'background-color': 'white'
    #         }
    #     },
    # ]
)


def makeNote(question, answer):
    my_note = genanki.Note(model=my_model, fields=[question, answer])
    return my_note


def makeDeck(deckName, notes):
    my_deck = genanki.Deck(gen_id(), deckName)
    for note in notes:
        my_deck.add_note(note)
    genanki.Package(my_deck).write_to_file(deckName + ".apkg")
