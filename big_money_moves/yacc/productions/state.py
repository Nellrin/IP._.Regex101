from yacc.node import Node

def p_charlist(p):
    """
        charlist : charlist CHAR
                 | 
    """


    if len(p) == 3:
        p[0] = p[1] + [p[2]]

    else:
        p[0] = []


def p_charclass_opt(p):
    """
    charclass : LBRACKET charlist RBRACKET
    """

    x = ''.join(str(c) for c in p[2])
    y = len(x)
    z = [x[0]]
    i = 1
    if y >= 3:
        while i < y - 1:
            if x[i] == '-':
                z.extend([chr(c) for c in range(ord(x[i-1])+1, ord(x[i+1]) + 1)])
                i += 1
                i += 1
            
            else:
                z.append(x[i])

            i += 1

    if y > i:
        z.append(x[y-1])


    z = ''.join(z)
    print(z)
    p[0] = Node("POSSIBLE",z)

def p_charclass_exc(p):
    """
    charclass : EXCEPTOPTS charlist RBRACKET
    """

    x = ''.join(str(c) for c in p[2])
    y = len(x)
    z = [x[0]]
    i = 1
    if y >= 3:
        while i < y - 1:
            if x[i] == '-':
                z.extend([chr(c) for c in range(ord(x[i-1])+1, ord(x[i+1]) + 1)])
                i += 1
                i += 1
            
            else:
                z.append(x[i])

            i += 1

    if y > i:
        z.append(x[y-1])


    z = ''.join(z)
    print(z)
    p[0] = Node("EXCEPTION",z)


def p_state(p):
    """
    state : BARSS 
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
            | LITERALBAR WILDCARD
            | LITERALBAR LBRACKET
            | LITERALBAR RBRACKET
            | MINUS
            | LITERALBAR LCURLY
            | LITERALBAR RCURLY
            | LITERALBAR NULORONE
            | LITERALBAR COLON
            | LITERALBAR LPARENTHESIS
            | LITERALBAR RPARENTHESIS
            | WILDCARD
    """
    p[0] = p[len(p) - 1]