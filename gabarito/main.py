import pyautogui
pyautogui.PAUSE = 0.5 # comando pra dizer ao pyautogui pra ele esperar 0.5 segundo pra executar cada linha de codigo 
import time # biblioteca do py para fazer um sleep
# pyautogui.click -> clickar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escreveer um texto

# passo 1: entrar no sistema da empresa = https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
#pyautogui.write("Internet")
pyautogui.press("enter")

# abrir o perfil correto do google(somente pra quem possui mais de um perfil)
time.sleep(1)
pyautogui.click(x=787, y=572)

#digitar  o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 seg
time.sleep(3)
# passo 2: faer login
# preenche o email
pyautogui.click(x=760, y=406)
pyautogui.write("teste@gmail.com")
time.sleep(1)
#preenche a senha
pyautogui.click(x=735, y=504)
pyautogui.write("senhaqualquer")
pyautogui.press("enter")
time.sleep(1)
#clica no login
pyautogui.click(x=966, y=567)

# passo 3: importar base dados
# passo 4: cadastrar 1 produto
# passo 5: reoetir parar todos os outros produtos

# pyautogui -> faz automaçoes com py