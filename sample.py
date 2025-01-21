user_phrase = input("Please enter a phrase: ")
words = user_phrase.split()
abbreviation = ""
index = 0
common_words = ["the", "a", "an", "of", "in", "on", "to", "at", "for", "and", "or", "nor", "but", "yet", "so"]
while index < len(words):
    word = words[index]
    if word.lower() not in common_words:
        abbreviation += word[0].upper()
    index += 1
print(f"Abbreviation: {abbreviation}")
