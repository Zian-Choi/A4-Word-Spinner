# A4: Word Spinner by DAHEE HONG (u1500852) & Zian Choi (u1534573)
# Usernames: 'Dahee-Hong' is DAHEE HONG and 'puagra' and 'Zian-Choi' both are Zian Choi
# https://github.com/Zian-Choi/A4-Word-Spinner

from Spinner import Spinner


def main():
    spinner = Spinner('synonyms-simplified.txt')

    with open('essay.txt', 'r') as file:
        original_text = file.read().lower()

    print("Original:", original_text)

    for i in range(1, 4):
        modified_text = spinner.spin_text(original_text)
        print(f"Option {i}", modified_text)


if __name__ == "__main__":
    main()
