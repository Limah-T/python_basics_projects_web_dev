import re

def count_words(sentence):
    """Checks if user input is not empty, split and count words else print a message to user."""
    if not sentence:
        print("Sentence cannot be empty")
        return
    
    # Remove punctuation and split words
    split_words = re.sub(r'[^\w\s]', '', sentence)  # Removes punctuation
    words = split_words.split()
    length = len(words)
    print("Total word count is: ", length)
    
       
user_input = input("Enter sentence and separate each word with SPACE: ")
count_words(sentence=user_input)
