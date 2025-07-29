import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import word_count
from stats import count_characters
from stats import sort_characters


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

    print(sys.argv)

main()

    
    
