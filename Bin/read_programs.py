from os import listdir

def main():
    print("Avalible Programs:\n"+", ".join(get_programs()))

def get_programs():
    for dir in ["C:/Users/Tom/Documents/Code/Github/Pip-Pad/Programs/"]:
        return [i for i in listdir(dir) if i[-3:] ==".py"]
