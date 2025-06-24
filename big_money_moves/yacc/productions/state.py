from yacc.node import Node

def p_charlist(p):
    """
        charlist : charlist CHAR 
                 | charlist CHAR MINUS CHAR
                 | 
    """

    if len(p) == 3:
        p[0] = p[1] + [p[2]]

    elif len(p) == 5:
        p[0] = p[1] + [chr(c) for c in range(ord(p[2]), ord(p[4]) + 1)]

    else:
        p[0] = []

def p_charclass_opt(p):
    """
    charclass : LBRACKET charlist CHAR RBRACKET
    """

    p[0] = Node("POSSIBLE",''.join(p[2] + [p[3]]))


def p_charclass_exc(p):
    """
    charclass : EXCEPTOPTS charlist CHAR RBRACKET
    """

    p[0] = Node("EXCEPTION",''.join(p[2] + p[3]))


def p_state(p):
    """
    state : WILDCARD
            | BARSS 
            | BARLS 
            | BARSW 
            | BARLW
            | BARSD 
            | BARLD 
            | BARN 
            | BART
            | SPACE 
            | CHAR
            | charclass
            | LITERALBAR END
            | LITERALBAR START
            | LITERALBAR LITERALBAR
            | LITERALBAR ONEORMANY
            | LITERALBAR NULORMANY
            | LITERALBAR OR
            | LITERALBAR LBRACKET
            | LITERALBAR RBRACKET
            | MINUS
            | LITERALBAR LCURLY
            | LITERALBAR RCURLY
            | LITERALBAR NULORONE
            | LITERALBAR COLON
            | LITERALBAR LPARENTHESIS
            | LITERALBAR RPARENTHESIS
    """
    p[0] = Node("STATE", p[len(p) - 1])