import pyautogui
import time

# Aguarda o usuário preparar o ambiente
time.sleep(1.5)

# PASSO 1 - entrar no google
pyautogui.hotkey("win")
pyautogui.write("Chrome",interval=0.1)
pyautogui.press("enter")

# PASSO 2 - pesquisar no google
pyautogui.moveTo(160, 50,duration=1)  
pyautogui.click()
time.sleep(0.5)
pyautogui.FAILSAFE = True
pyautogui.write("https://www.google.com")
pyautogui.press("enter")

# Aguarda carregamento
time.sleep(2)

# Digitar termo pesquisado
pyautogui.write("Clima hoje na minha cidade")
pyautogui.press("enter")
time.sleep(1.5)
# PASSO 3 - Clicar no campo de pesquisa da Wikipedia

img = pyautogui.screenshot()
img.save("tela.png")

print("Automação finalizada com sucesso!")

