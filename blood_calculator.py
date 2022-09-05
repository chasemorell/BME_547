def interface():
    print("Blood Calculator");
    print("Options")
    print("1 - HDL")
    print("2 - LDL")
    print("9 - Quit")

    keep_running = True
    while keep_running:
        choice = input("Enter Choice: ")
        if choice == "9":
            return
        if choice == "1":
            HDL_driver();
        if choice == "2":
            LDL_driver();

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
        print(check_HDL(input_HDL()))

def LDL_driver():
        print(check_LDL(input_LDL()))

def input_LDL():
    LDL_input = input("Enter the LDL value:")
    return int(LDL_input)

def check_LDL(x):
    if(x<130):
        return "Normal"
    elif(x<=159):
        return "Borderline High"
    elif(x<=189):
        return "High"
    elif(x>=190):
        return "Very High"

interface()
