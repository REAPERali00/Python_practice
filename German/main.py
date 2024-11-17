from card import Card
import re


class Question:
    def __init__(self, german: str, english: str):
        self.german = german
        self.english = english

    def __repr__(self):
        return f"Question(German: '{self.german}', English:'{self.english}')"


class Game:
    
    def read_gc_data(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            notes = file.read()
        pattern = r"- `([^`]+)`-> (.+)"
        matches = re.findall(pattern, notes)
        questions = [
            Question(german.strip(), english.strip()) for german, english in matches
        ]
        return questions
    def card_question(self ): 
        ...



Card(
    "DO you like it so much that you are willing to die for it? ", 20, 0.5
).print_card()
