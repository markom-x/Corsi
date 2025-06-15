def check_hello_greetings(user_input, hello_detected):
    return hello_detected in user_input

def main():
        greeting = input("Greeting: ").casefold().replace(" ", "")
        hello = "hello"
        if check_hello_greetings(greeting, hello):
                print("$0")
        elif greeting[0] == "h":
                print("$20")
        else:
                print("$100")
main()





