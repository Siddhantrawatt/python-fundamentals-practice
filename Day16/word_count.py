def count_words(filename):
    with open(filename, "r") as file:
        data = file.read()
        words = data.split()
        return len(words)

print(count_words("data.txt"))