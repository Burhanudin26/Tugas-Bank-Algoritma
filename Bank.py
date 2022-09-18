text=input("Hello?").lower().strip()

if "hello" in text:
    print("Thank you for 0$")
elif text[0]=="h":
    print("This is your 20$")
else:
    print("This is your 100$")
