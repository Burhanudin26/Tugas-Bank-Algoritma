text=input("Hai apa kabar?").lower().strip()

if text[0:5]=="hello":
    print("Thank you for 0$")
elif text[0]=="h":
    print("This is your 20$")
else:
    print("This is your 100$")