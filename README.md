# bot_automacao
# Esse código foi feito para automatizar uma tarefa repetitiva no computador, que é entrar em um sistema online e cadastrar vários produtos.

# Ele faz isso em etapas:

# Abrir o navegador (Chrome) automaticamente e acessar o site do sistema da empresa.

# Fazer login sozinho, preenchendo e-mail e senha.

# Ler os produtos de uma planilha (CSV) usando a biblioteca pandas. Essa planilha contém informações como:

# Código do produto

# Marca

# Tipo

# Categoria

# Preço unitário

# Custo

# Observações

# Cadastrar cada produto no site: o pyautogui simula cliques, digitação e navegação entre os campos do formulário para preencher os dados corretamente.

# Repetir o processo para todos os produtos da planilha, até terminar.