
import qrcode

NAME = "Vlad"
SURNAME = "Panasiuk"
GROUP = "IT31"
EMAIL = "tpanasiuk12@gmail.com"
print(f"{NAME} {SURNAME}, {GROUP}")

text = f"{NAME} {SURNAME}, {GROUP}, {EMAIL}"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")
print(text)
