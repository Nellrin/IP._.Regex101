import sys
from autools import testar_regex_com_automato, desenhar_automato
import shutil

def linha_horizontal(caracter='='):
    largura = shutil.get_terminal_size((80, 20)).columns
    print(caracter * largura)


def main():
    if len(sys.argv) < 2:
        print("Uso: python testar_automato.py <arquivo_textos.txt> <regex>")
        sys.exit(1)

    arquivo_textos = sys.argv[1]
    regex = ""

    with open("regex_input.txt", "r", encoding="utf-8") as f:
        regex = f.read().strip()

    with open(arquivo_textos, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        amount = len(linhas)




    print()
    linha_horizontal()
    print(f"[Fonte do conteúdo a ser testado] (\033[1m{arquivo_textos}\033[0m)")
    print(f"[Regex a ser utilizado]           '\033[1m{regex}\033[0m'")
    linha_horizontal()
    print()
    linha_horizontal()
    
    
    
    passou = 0
    for index, linha in enumerate(linhas):
        texto = linha.strip()
        if not texto:
            continue
        result = testar_regex_com_automato(index + 1, amount,texto, regex)
        if result is not None: 
            passou = passou + 1


    print()
    linha_horizontal()
    print(f" O Regex passou a \033[1m{passou}\033[0m de \033[1m{amount}\033[0m testes")

    linha_horizontal()
    print()

    if len(sys.argv) > 2:
        desenhar_automato(regex, nome="automato")

if __name__ == "__main__":
    main()
