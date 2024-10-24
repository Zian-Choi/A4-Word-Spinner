# A4: Word Spinner by DAHEE HONG (u1500852) & Zian Choi ()
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