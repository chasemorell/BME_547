def interface():
    print("Blood Calculator");
    print("Options")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter Choice: ")
        if choice == "9":
            return
        

interface()
