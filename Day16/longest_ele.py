def longest_word(filename):
    with open(filename, "r") as file:
        words = file.read().split()
    
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

print(longest_word("data.txt"))