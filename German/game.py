from card import Card
import re
import os
import random
import time


class Question:
    def __init__(self, german: str, english: str):
        self.german = german
        self.english = english

    def german_card(self):
        Card(self.german).print_card()

    def english_card(self):
        Card(self.english).print_card()

    def __repr__(self):
        return f"Question(German: '{self.german}', English:'{self.english}')"


class Game:

    def __init__(self):
        self.score = 0
        self.Questions = []

    def read_gc_data(self, filepath):
        if not os.path.exists(filepath):
            print("error; File not found")
            return []
        with open(filepath, "r", encoding="utf-8") as file:
            notes = file.read()
        pattern = r"- `([^`]+)`-> (.+)"
        matches = re.findall(pattern, notes)
        questions = [
            Question(german.strip(), english.strip()) for german, english in matches
        ]
        return questions

    def start(self):
        print(
            "Hi! Welcome to the German flashcard game! "
            "We will show you a card and you guess the corresponding answer!"
        )
        self.Questions = self.read_gc_data("coffee_break.md")
        random.shuffle(self.Questions)
        time.sleep(2)
        for question in self.Questions:
            os.system("clear")
            print("here is the german card: ")
            question.german_card()
            input("Press enter when you are ready! ")

            print("here is the english card: ")
            question.english_card()

            ans = input("did you get it right?[y/n] ").strip().lower()
            self.score += 0 if ans == "n" else 1
            if ans == "q":
                return

        print(f"\nGame Over! Your final score is {self.score}/{len(self.Questions)}.")
