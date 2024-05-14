"""Counts the number of words in a given sentence."""
################# Code ##########################

# create a funtion that calculate the words present in the sentence
def count_words(sentence):
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

# Get input from the user
user_sentence = input("Enter a sentence: ")

# Count the number of words
word_count = count_words(user_sentence)

# Print the result
print(f"The sentence has {word_count} words.")