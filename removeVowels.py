def shortcut(s):
    """Defining function that removes vowels from strings."""
    vowels = "aeiou"
    new_word = []
    for letter in s:
        if letter not in vowels:
            new_word.append(letter)  
    return ''.join(new_word)

print(shortcut("hello"))
print(shortcut("helloo"))