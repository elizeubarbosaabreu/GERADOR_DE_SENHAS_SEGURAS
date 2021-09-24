import PySimpleGUI as sg
import string, clipboard, webbrowser
from random import choice, randint

# 
#  ____  _                           ____                                     _ 
# / ___|| |_ _ __ ___  _ __   __ _  |  _ \ __ _ ___ _____      _____  _ __ __| |
# \___ \| __| '__/ _ \| '_ \ / _` | | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
#  ___) | |_| | | (_) | | | | (_| | |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
# |____/ \__|_|  \___/|_| |_|\__, | |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
#                            |___/                                              
#   ____                           _             
#  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
#  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#                                                
caracteres_especiais = ['!', '#', '$', '%', '&', '*', ',', '.', ':', ';', '/', '?', '_', '-', '<', '>']
letras_minusculas = list(string.ascii_lowercase)
letras_maiusculas = list(string.ascii_uppercase)
letras = []
senha = ''
url = 'https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/'

def sortear_numero():
    return randint(0, 10)    

def sortear_minuscula(letras_minusculas):
    return choice(letras_minusculas)

def sortear_maiuscula(letras_maiusculas):
    return choice(letras_maiusculas)

def sortear_caracter(caracteres_especiais):
    return choice(caracteres_especiais)

def embaralhar(lista_de_funcoes):
    return choice(lista_de_funcoes)

sg.theme('Topanga')

layout = [[sg.Stretch(), sg.T('GERADOR DE SENHAS SEGURAS', font=('Arial', 18)), sg.Stretch()],
          [sg.HorizontalSeparator()],
          [sg.Stretch(),
           sg.T('Tamanho da senha:', font=('Arial', 12) ),
           sg.Combo(['8', '10', '12', '20', '25'], key='-tam_senha-', default_value='25'),
           sg.Stretch()],
          [sg.HorizontalSeparator()],
          [sg.Output(font=('Courier', 18), size=(30,2), key='-output-')],
          [sg.HorizontalSeparator()],
          [sg.Stretch(),
           sg.Button('Gerar Senha'),
           sg.Button('Copiar Senha'),
           sg.Button('Autor'),
           sg.Stretch()],
          [sg.HorizontalSeparator()],
          
          ]

window = sg.Window('GERADOR DE SENHAS SEGURAS', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    elif event == 'Autor':
        webbrowser.open(f'{url}')
        
    
    elif event == 'Gerar Senha':
        
        senha = ''
        window.FindElement('-output-').Update('')
        tamanho_da_senha = values['-tam_senha-']
        
        for letra in range(int(tamanho_da_senha)):
            
            lista_de_funcoes = (sortear_numero(),
                                sortear_minuscula(letras_minusculas),
                                sortear_maiuscula(letras_maiusculas),
                                sortear_caracter(caracteres_especiais))
            
            letras = embaralhar(lista_de_funcoes)
            
            senha += str(letras)           
            
        print(f'{senha}')
    
    if event == 'Copiar Senha':
        
        clipboard.copy(senha)        
        senha = ''
        
window.close()