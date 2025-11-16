import time 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import messagebox


def fazer_login():
    
    # Pegar o que o usuário digitou
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    # Verificar se preencheu tudo
    if usuario == "":
        messagebox.showwarning("Atenção", "Digite o usuário!")
        return
    
    if senha == "":
        messagebox.showwarning("Atenção", "Digite a senha!")
        return
    
    # Desabilitar botão enquanto roda
    botao_entrar.config(state="disabled")
    texto_status.config(text="Carregando...")
    janela.update()
    
    try:
        # Abrir o Chrome
        janela.update()
        navegador = webdriver.Chrome()
        
        # Entrar no site
        janela.update()
        navegador.get("https://loja.algar.com.br/")
        navegador.maximize_window()
        sleep(3)
        
        # Clicar nos menus
        janela.update()
        
        navegador.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/div[3]/div/div/div[1]/i').click()
        sleep(2)
        
        navegador.find_element(By.XPATH, '//*[@id="headerFloatingAnchor"]/div/div/div/div[2]/div[1]').click()
        sleep(3)
        
        navegador.find_element(By.XPATH, '//*[@id="headerFloatingAnchor"]/div/div/div/div[2]/div[1]/div/div[2]/div/ul/li[4]/a').click()
        sleep(2)
        
        # Digitar usuário
        janela.update()
        
        campo_usuario = navegador.find_element(By.XPATH, '//*[@id="username"]')
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)
        sleep(1)
        
        # Digitar senha
        janela.update()
        
        campo_senha = navegador.find_element(By.XPATH, '//*[@id="password"]')
        campo_senha.clear()
        campo_senha.send_keys(senha)
        sleep(1)
        
        # Clicar em entrar
        janela.update()
        
        navegador.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[3]/form/div/div[2]/div[1]/button').click()
        sleep(3)
        
        #
        navegador.find_element(By.XPATH, '//*[@id="modalOverlay"]/div/span').click()
        sleep(1)

        url_atual = navegador

        
        
    except Exception as erro:
        texto_status




#############################################
# CRIAR A JANELA


janela = tk.Tk()
janela.title("Login Algar")
janela.geometry("300x250")

# Título
titulo = tk.Label(janela, text="Login Algar", font=("Arial", 18, "bold"))
titulo.pack(pady=20)

# Campo de Usuário
texto_usuario = tk.Label(janela, text="Usuário/Cpf:", font=("Arial", 10))
texto_usuario.pack()

entrada_usuario = tk.Entry(janela, font=("Arial", 11), width=30)
entrada_usuario.pack(pady=5)

# Campo de Senha
texto_senha = tk.Label(janela, text="Senha:", font=("Arial", 10))
texto_senha.pack(pady=(10, 0))

entrada_senha = tk.Entry(janela, font=("Arial", 11), width=30, show="*")
entrada_senha.pack(pady=5)

# Botão Entrar
botao_entrar = tk.Button(
    janela,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=20,
    command=fazer_login
)
botao_entrar.pack(pady=20)

# Texto de Status
texto_status = tk.Label(janela, text="", font=("Arial", 9))
texto_status.pack()

# Iniciar o programa
janela.mainloop()
