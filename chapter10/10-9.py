dog_flie = "10-8-dogs.txt" 
cat_flie = "10-8-cats.txt" 

def read_files(filename): 
    try:
        with open(filename, "r") as file: 
            file_contents = file.read() 
    except FileNotFoundError: 
#        print("File not found.") 
        pass
    else:
        print(file_contents) 

read_files(dog_flie) 
read_files(cat_flie) 