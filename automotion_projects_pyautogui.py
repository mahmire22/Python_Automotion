import pyautogui
import  time

#Give the python file some time before continuing
time.sleep(3)

#Mouse Function
print(pyautogui.size()) #prints the resolution of your screen
print(pyautogui.position()) #prints the current position
pyautogui.moveTo(100, 100, 3)#moves the mouse over time (3 seconds)
pyautogui.moveRel(100, 100, 3)#move the mouse relative to its current position
pyautogui.click(100, 100, 3, 3, button="left")


pyautogui.scroll(500) #scroll up
pyautogui.scroll(-500) #scroll down

#Mouse up and down
pyautogui.mouseUp(100, 100, button="left")
pyautogui.mouseDown(100, 100, button="left")
