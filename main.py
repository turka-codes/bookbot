import sys
from stats import get_num_words, get_sorted_character_count

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    dict = get_sorted_character_count(text)
    
    for item in dict:
        print(f"{item['char']}: {item['num']}")

main()