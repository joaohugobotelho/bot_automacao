import pyautogui
pyautogui.PAUSE = 0.5 # comando pra dizer ao pyautogui pra ele esperar 0.5 segundo pra executar cada linha de codigo 
import time # biblioteca do py para fazer um sleep

# pyautogui -> faz automaçoes com py
# pyautogui.click -> clickar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escreveer um texto

# passo 1: entrar no sistema da empresa = https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
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

#time de 3 segundos pro site carregar
time.sleep(3)

# passo 3: importar base dados com o pandas
import pandas 
tabela = pandas.read_csv("produtos.csv")

# passo 4: cadastrar 1 produto

for i in tabela.index: #forzinho pra executar cada linha da tabela / o .index pega cada linha da tabela
    pyautogui.click(x=725, y=293)

    codigo = tabela.loc[i, "codigo"] # o .loc localiza o produto na sua categoria
    pyautogui.write(codigo)
    pyautogui.press("tab") # o tab passa para o proximo campo

    marca = tabela.loc[i, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[i, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[i, "categoria"]) # formatando para string utlizando o str
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[i, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[i, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[i, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000) # o .scroll funciona para o pyautogui fazer a rolagem do scroll sozinho(cima ou baixo)


# passo 5: reoetir parar todos os outros produtos



