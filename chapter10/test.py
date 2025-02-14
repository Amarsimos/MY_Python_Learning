filename = 'Alice in Wonderland.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print("Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words.")