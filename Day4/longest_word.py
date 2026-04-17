s = input ("Enter a string: ") 
longest_word = ""
words = s.split()
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)
