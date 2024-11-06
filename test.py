def get_word_count(text):
    word_count = text.split()
    
    return len(word_count)


print(get_word_count("I am Cute"))