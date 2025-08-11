import sys
from stats import get_number_of_words, count_symbols, sort_symbols_dictionary

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    get_number_of_words(text)
    print("--------- Character Count -------")
    counter = count_symbols(text)
    sorted_counter = sort_symbols_dictionary(counter)
    for i in sorted_counter:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()