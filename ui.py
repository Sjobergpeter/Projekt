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


'''
# Skriver ut allt som går att använda
print(f"Timezone: {timezone}")
print(f"datetime: {datetime}")
print(f"Date: {date}")
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}h")
print(f"Minute: {minute}m")
print(f"Second: {second}s")
print(f"Day of week: {day_of_week}")
'''
