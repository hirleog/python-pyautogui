import pyautogui
import time

print(pyautogui.position())
print(pyautogui.size())

pyautogui.PAUSE = 0.3 #ESPERA 0.3 SEGUNDOS PARA CADA AÇÃO DO pyautogui
pyautogui.moveTo(x=-449, y=147, duration=2) #MOVE MAS NAO CLICA
pyautogui.click(x=-535, y=281)  # CLICA NA CORDENADA PASSADA
# # pyautogui.scroll(-200) # numero negativo = scroll para baixo
# time.sleep(5) # AGUARDA 5 SEGUNDOS PARA REALIZAR A FUNÇÃO

# # funções do teclado
# pyautogui.write("Se inscreve no canal")
# pyautogui.hotkey("ctrl", "v")
# pyautogui.press("enter")



