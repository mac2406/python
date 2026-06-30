name = input("Enter name: ")

print(f"Original: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

sent = input("Enter sentence: ")
print(f"Total characters: {len(sent)}")
print(f"Number of space: {sent.count(' ')}")

word = input("Enter a word: ")
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")

#Take a sentence.
#Replace:
#AI
#with
#Artificial Intelligence

sent = input("Enter sentence: ")
sent = sent.replace("AI", "Artificial Intelligence")
print(sent)