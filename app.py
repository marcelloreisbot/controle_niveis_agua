from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com as situacoes do reservatorio
niveis_agua = [
    "Muito baixo (critico)",
    "Baixo",
    "Medio",
    "Alto",
    "Muito alto (alerta)"
]

# Funcao que retorna a cor conforme o nivel
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulacao dos niveis do reservatorio
print("MONITORAMENTO\n")

for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + f"Nivel {nivel}: {mensagem}")

# Restaura o estilo padrao do terminal
print(Style.RESET_ALL)
