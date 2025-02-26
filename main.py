from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python 3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print_report(book_path)

main()