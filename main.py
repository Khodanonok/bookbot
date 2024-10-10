

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = count_words(text)
    count_of_chars = count_chars(text)
    sorted_char_count= clean_dict(count_of_chars)
    print_report(count_of_words, sorted_char_count)

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    occurrences = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in occurrences:
            occurrences[char] += 1
        else: 
            occurrences[char] = 1
    
    return occurrences


def clean_dict(dict):
    cleaned_dict = {}

    for key, value in dict.items():
        if key.isalpha():
            cleaned_dict[key] = value
    return sorted(cleaned_dict.items(), reverse=True, key=lambda x: x[1])

  
def print_report(word_count, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for tuple in chars:
        print(f"The {tuple[0]} character was found {tuple[1]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()