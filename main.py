import sys
from stats import count_words, chars_freq


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    chars = chars_freq(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in chars:
        print(f"{c['char']}: {c['count']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    main()
