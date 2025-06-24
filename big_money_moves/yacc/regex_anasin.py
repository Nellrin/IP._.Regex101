import sys
import ply.yacc as yacc
from lexer.regex_analex import tokens, lexer


from yacc.node import *
from yacc.productions.state import *
from yacc.productions.expr import *
from yacc.productions.init import *


def p_empty(p):
    "empty :"

def p_error(p):
    if p:
        print(f"[YACC] erro perto de '{p.value}' (Token: {p.type}) (Posição: {p.lexpos})")
    else:
        print("[YACC] erro: fim de entrada inesperado")


parser = yacc.yacc(
    start="whole",
    optimize=True,
    write_tables=True,
)


if __name__ == "__main__":    
    data = input("[Insira o Regex a ser aplicado]: ")
    ast = parser.parse(data, lexer=lexer)
    print(ast)
