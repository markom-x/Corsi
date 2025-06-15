def main():
    due = 50
    while 0 < due <= 50:
        print(f"Amount Due: {due}")
        money = input("Insert Coin: ")
        match money:
            case "25" | "10" | "5":
                due = due - int(money)
    print(f"Change Owed: {abs(due)}")
main()
