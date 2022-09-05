def interface():
    print("Blood Calculator");
    print("Options")
    print("1 - HDL")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter Choice: ")
        if choice == "9":
            return
        if choice == "1":
            HDL_driver();

def input_HDL():
    HDL_input = input("Enter the HDL value:")
    return int(HDL_input)

def check_HDL(x):
    if(x>=60):
        return "Normal"
    elif(x>=40 and x<60):
        return "Borderline Low"
    elif(x<40):
        return "Low"

def HDL_driver():
    while(True):
        print(check_HDL(input_HDL()))

interface()
