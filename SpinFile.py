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
