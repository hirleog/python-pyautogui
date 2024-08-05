import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("CHRO")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("hashtagtreinamentos.com")
pyautogui.press("enter")

time.sleep(3)
posicao_cursopython = pyautogui.locateCenterOnScreen("cursopython.png")
pyautogui.click(posicao_cursopython) # clicar em "Curso de Python"
time.sleep(3)

pyautogui.scroll(-200)
pyautogui.click(x=441, y=870)

pyautogui.write("Lira")
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
