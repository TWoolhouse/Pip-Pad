version = 0.3

from sys import path
from importlib import import_module, reload
import _thread
for item in ["/home/pi/Documents/Pip-Pad/Bin/","/home/pi/Documents/Pip-Pad/Programs/"]:
    path.insert(0, item) # the exact path of where the python files will be

class ProgramGroup:

    def __init__(self):
        self.programs = {}

    def __repr__(self):
        return "Programs:\n{}".format(" ".join([str(self.programs[i]) for i in self.programs]))

    def run(self, name):
        self.programs[name].run()

    def add_program(self, name, module):
        self.programs[name.replace("_"," ")] = Program(name, module)

class Program:

    def __init__(self, name, module):
        self.name = name
        self.module = module

    def __repr__(self):
        return "\nName: {}\nModule: {}".format(self.name, self.module)

    def run(self):
        self.module.main()

def module_import(module):
    try:
        installed_module = import_module(module)
        return installed_module
    except ImportError: print(module+": "+bin.programs["messages"].module.msg["ImportError"])
    except ValueError: print(bin.programs["messages"].module.msg["valid"])

def get_module_name():
    while True:
        try:
            user_input = input("Please enter a program:\n").strip().lower()
            if user_input == "quit":    quit()
            elif user_input == "back":  return False
            elif (len(user_input) > 0) and (user_input != " "): return user_input
            else:   print(bin.programs["messages"].module.msg["valid"])
        except (EOFError, KeyboardInterrupt):   print(bin.programs["messages"].module.msg["quitback"])

def get_user_input():
    while True:
        try:
            user_input = input("[Import]\n[Run]\n[Programs]\n[Quit]\n\n> ").strip().lower()
            if user_input == "quit":    quit()
            return user_input
        except (EOFError, KeyboardInterrupt):   print(bin.programs["messages"].module.msg["quitback"])


bin = ProgramGroup()
for module in ["new_screen","messages","read_programs","ip_display"]:
    bin.add_program(module, module_import(module))
_thread.start_new_thread(bin.programs["ip display"].run, tuple())

all_modules = ProgramGroup()

while True:
    bin.programs["new screen"].module.new_screen()
    user_input = get_user_input()
    if user_input == "import":
        module = get_module_name()
        if module != False:
            all_modules.add_program(module, module_import(module))
    elif user_input == "run":
        module = get_module_name()
        if (module != False) and (module in list(all_modules.programs.keys())):
            bin.programs["new screen"].module.new_screen()
            all_modules.run(module)
            input(bin.programs["messages"].module.msg["continue"])
    elif user_input == "programs":
        bin.programs["new screen"].module.new_screen()
        print("Imported Programs:\n"+", ".join([all_modules.programs[i].name for i in all_modules.programs]))
        bin.run("read programs")
        input(bin.programs["messages"].module.msg["continue"])
    else:   print("Please enter a valid input")



