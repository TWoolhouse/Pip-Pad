def main():
    print("Avalible Programs:\n"+", ".join(read_programs()))

def read_programs():
    try:
        with open("./Bin/Text_Files/programs.txt","r") as file:
            return [line.strip() for line in file.readlines()]
    except IOError: return []

