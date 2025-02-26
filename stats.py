def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(string):
    words = string.split()
    length = len(words)
    return length

def get_char_count(string):
    lower_str = string.lower()
    char_dict = {}
    for char in lower_str:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def print_report(book):
    text = get_book_text(book)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_count = convert_dict(char_count)
    print("--- Begin report of", book,"---")
    for item in sorted_count:
        print(f"{item["char"]}: {item["num"]}")
    print(word_count, "words found in the document")
    print("--- End report ---")

def convert_dict(in_dict):
    sorted_list = []
    for char in in_dict:
        sorted_list.append({"char": char, "num": in_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]