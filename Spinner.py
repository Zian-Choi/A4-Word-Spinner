# A4: Word Spinner by DAHEE HONG (u1500852) & Zian Choi (u1534573)
# Usernames: 'Dahee-Hong' is DAHEE HONG and 'puagra' and 'Zian-Choi' both are Zian Choi
import random


class Spinner:
    def __init__(self, synonym_file):
        self.synonym_dict = self.load_synonyms(synonym_file)

    def load_synonyms(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    word, synonym_str = line.split(':')
                    synonyms[word.strip()] = [syn.strip() for syn in synonym_str.split(',')]
        return synonyms

    def spin_text(self, text, probability = 50):
        words = text.split()
        new_words = []

        for word in words:
            stripped_word = ''.join(char for char in word if char.isalnum())
            if stripped_word in self.synonym_dict:
                if random.randint(1, 100) > probability:
                    word = random.choice(self.synonym_dict[stripped_word])
                    new_words.append(word)
                else:
                    new_words.append(stripped_word)

            else:
                new_words.append(stripped_word)

        # Return the text joined back into a single string
        return ' '.join(new_words)
