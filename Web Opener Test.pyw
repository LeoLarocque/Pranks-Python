import webbrowser
import pyautogui
import time
time.sleep(3)
webbrowser.open_new_tab("https://fakeupdate.net/win10ue/")
time.sleep(0.1)
pyautogui.press("Fn")
pyautogui.press("F11")
