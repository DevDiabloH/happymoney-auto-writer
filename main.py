import pyautogui as auto
import pyperclip

var = str(pyperclip.paste());

rep = {"-", "_", ",", " "}
for r in rep:
    var = var.replace(r, "")

print("wait a 3sec.")
auto.sleep(3)
auto.typewrite(var, interval=0.03)