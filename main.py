import sys
from stats import get_no_of_words, count_chars, sort_dict

def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    book_text = get_book_text(book)
    print(f"Analyzing book found at {book}...")
    
    num_words = get_no_of_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")

    char_occurences = sort_dict(count_chars(book_text))
    print("--------- Character Count -------")
    for char_dict in char_occurences:
        print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
