FILE_NAME = "./books/frankenstein.txt"


def main():
    with open(FILE_NAME) as f:
        file_contents = f.read()

        print_report(FILE_NAME, file_contents)


def print_report(file_name, file_contents):
    print(f"--- Begin report of {file_name} ---")
    print(f"{count_words(file_contents)} words found in the document")
    for key, value in count_chars(file_contents).items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def count_words(file_contents):
    words = file_contents.split()
    words = words.__len__()
    return words


def count_chars(file_contents):
    char_dict = dict()
    for char in file_contents:
        char_low = char.lower()
        if char_dict.get(char_low):
            char_dict[char_low] = char_dict[char_low] + 1
        else:
            char_dict[char_low] = 1
    return char_dict


if __name__ == "__main__":
    main()
