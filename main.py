
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = get_word_count(text)
    chars = get_char_count(text)
    chars_sorted_list = chars_to_sorted(chars)
    
    print(f"--- Begin report of {path}) ---")
    print(f"{words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
    print("\n--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def sort_on(d): 
    return d["num"]
 
def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_to_sorted(chars):
    sorted = []
    for char in chars:
        if char.isalpha():
            sorted.append({"char": char, "num": chars[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
            

main()

