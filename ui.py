import os

ui_width = 30


def line(dots=False):
    if not dots:
        print("-" * ui_width)
    if dots:
        print("*" * ui_width)


def header(text):
    print("|", text.center(26), "|")


def echo(text):
    print("| " + text)


def prompt(text):
    return input("| " + text + " > ")


def clear():
    if os.name == "nt":
        os.system("cls")

    elif os.name == "posix":
        os.system("clear")