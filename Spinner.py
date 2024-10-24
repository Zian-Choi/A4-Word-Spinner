# A4: Word Spinner by DAHEE HONG (u1500852) & Zian Choi (u1534573)
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

        # Check if the word is in the dictionary of synonyms
        for word in words:
            stripped_word = ''.join(char for char in word if char.isalnum())
            if word in self.synonyms:
                if random.randint(1, 100) > 50:
                    word = random.choice(self.synonyms[word])
                    new_words.append(word)
                else:
                    new_words.append(stripped_word)

            else:
                new_words.append(stripped_word)

        # Return the text joined back into a single string
        return ' '.join(new_words)
