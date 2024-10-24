from Spinner import Spinner


def main():
    spinner = Spinner('synonyms-simplified.txt')

    with open('essay.txt', 'r') as file:
        original_text = file.read().lower()

    print("Original:", original_text)