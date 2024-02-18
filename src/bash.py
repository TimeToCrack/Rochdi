from os import *

def start():
    command = input("> ")
    if command == "help":
        print("help, mdir, rmdir, pr")
    if command == "mdir":
        namedir = input("NAME > ")
        system(f"md {namedir}")
    if command == "rmdir":
        namedir = input("NAME > ")
        system(f"rd {namedir}")
    if command == "pr":
        printe = input("TEXT > ")
        print(printe)
