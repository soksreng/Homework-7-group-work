def backward_string_by_word(text):
    words = text.split()
    
    reversed_words = [word[::-1] for word in words]
    
    return ' '.join(reversed_words)

print(backward_string_by_word(''))  
print(backward_string_by_word('world'))  
print(backward_string_by_word('hello world')) 
print(backward_string_by_word('hello world, how are you?'))  