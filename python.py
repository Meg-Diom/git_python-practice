name = input("Enter your surname. It should be atleast 4 letters: ")
if name == "Beifong":
    pincode = int(input("Enter your pincode: "))
    if pincode == 2005:
        print("Welcome home!!!")
    else:
        print("Incorrect pincode.")
        pincode = int(input("Enter your pincode again: "))
        if pincode == 2005:
            print("That was close! Welcome home!!!")
        else: 
            print("Your fingerprint is required to unlock this device.")
else:
    print("You are not eligible to unlock this device.")