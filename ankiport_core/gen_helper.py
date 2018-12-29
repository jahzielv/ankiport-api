import genanki
import random
import json
import io


def gen_id():
    return random.randrange(1 << 30, 1 << 31)


class DeckGenerator:

    def __init__(self):
        self.my_model = genanki.Model(
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
            css=""".card {
            font-family: arial;
            font-size: 100px;
            text-align: center;
            color: red;
            background-color: white;
        }"""
        )

    def makeCss(self, jsonDict):
        """
            Takes a JSON object (a dict) and turns it into a string for loading
            into genanki.
        """

    def makeNote(self, question, answer):
        my_note = genanki.Note(model=self.my_model, fields=[question, answer])
        return my_note

    def makeDeck(self, deckName, notes):
        my_deck = genanki.Deck(gen_id(), deckName)
        for note in notes:
            my_deck.add_note(note)
        genanki.Package(my_deck).write_to_file(deckName + ".apkg")

    def makeDeckBytes(self, deckName, notes):
        '''
        Creates a deck with the given list of notes. Returns a BytesIO object
        containing all the binary data of the Anki deck.
        '''
        my_deck = genanki.Deck(gen_id(), deckName)
        deck_bytes = io.BytesIO()

        for note in notes:
            my_deck.add_note(note)
        genanki.Package(my_deck).write_to_file(deck_bytes)
        return deck_bytes
