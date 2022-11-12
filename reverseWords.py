# Complete the function that accepts a string parameter, 
# and reverses each word in the string. All spaces in the string should be retained.

sentence = "This is a sentence to be reversed"

def reverse_word(k):
    
    words = k.split(' ')
    reverse = [j[::-1] for j in words]
    new_sentence = " ".join(reverse)
    return new_sentence

print(reverse_word(sentence))