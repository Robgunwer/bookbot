from stats import *
import sys
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            content = f.read()
            return content
            

    x = word_count(get_book_text(path))
    y = character_count(get_book_text(path))
    z = list_of_dicts(y)

    def report():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(x)
        print("--------- Character Count -------")
        print(z)
        print("============= END ===============")

    report()
main()
