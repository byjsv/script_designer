import win32api

while True:
    for i in range(255):
        if win32api.GetKeyState(i) & 0x8000:
            print(i)