text=input("Hello?").lower()
text=text.replace(" ","")
if "hello" in text:
    print("Thank you for 0$")
elif text[0]=="h":
    print("This is your 20$")
else:
    print("This is your 100$")
