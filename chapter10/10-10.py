dog_flie = "10-8-dogs.txt" 
cat_flie = "10-8-cats.txt" 
alice_flie = "Alice in Wonderland.txt"

def read_files(filename): 
    try:
        with open(filename, "r", encoding="utf-8") as file: 
            file_contents = file.read() 
    except FileNotFoundError: 
#        print("File not found.") 
        pass
    else:
        return file_contents 

alice = read_files(alice_flie) 
print(alice.count("the")) 
print(alice.lower().count("the")) 