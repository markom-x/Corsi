import pyfiglet
import sys
try:
    pyfiglet.figlet_format("", font=sys.argv[2])
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        listen = input("Input: ")
        print(f"Output:\n{pyfiglet.figlet_format(listen, font=sys.argv[2])}")
    else:
        sys.exit("Invalid usage")
except IndexError:
    try:
        if sys.argv[1] != "-f" or sys.argv[1] != "--font":
            sys.exit("Invalid usage")
    except IndexError:
        listen = input("Input: ")
        print(f"Output:\n{pyfiglet.figlet_format(listen)}")
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")
