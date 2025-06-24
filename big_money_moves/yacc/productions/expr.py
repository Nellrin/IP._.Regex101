from yacc.node import Node
from yacc.productions.state import *

def p_phrase(p):
    """ 
        phrase : phrase state
               | state
               | 
    """
    if len(p) == 3:
        p[0] = Node("BUFFER", p[1], p[2])
    elif len(p) == 2:
        p[0] = Node("BUFFER", p[1])
    else:
        p[0] = Node("ϵ")


def p_quantifier(p):
    """ 
        quantifier : ONEORMANY
                   | NULORMANY
                   | LCURLY NUMBER RCURLY
                   | LCURLY NUMBER COMMA RCURLY
                   | LCURLY COMMA NUMBER RCURLY
                   | LCURLY NUMBER COMMA NUMBER RCURLY
                   | 
    """
    match len(p):
        case 2:
            p[0] = Node("QUANTIFIER_BASIC", p[1])

        case 4:
            p[0] = Node("QUANTIFIER_EXACT_AMOUNT", p[2])

        case 5:
            if p[2] == ',': p[0] = Node("QUANTIFIER_LESS_THAN", p[3])
            else:           p[0] = Node("QUANTIFIER_MORE_THAN", p[2])

        case 6:
            p[0] = Node("QUANTIFIER_RANGE", Node("MIN", p[3]), Node("MAX", p[5]))
        


def p_expropt_case(p):
    """ 
        expropt : NULORONE
                | 
    """
    if len(p) > 1:
        p[0] = Node("OPTIONAL", p[1])

def p_expr_full(p):
    """ 
        expr : expr alternative miniexpr expropt

    """
    p[0] = Node("EXPR", p[1], Node("ALT", p[2]),Node("MINI", p[3]),p[4])

def p_expr_noopt(p):
    """ 
        expr : expr alternative miniexpr

    """
    p[0] = Node("EXPR", p[1], Node("ALT", p[2]),Node("MINI", p[3]))

def p_expr_noalt(p):
    """ 
        expr : expr miniexpr expropt

    """
    p[0] = Node("EXPR", p[1],Node("MINI", p[2]),p[3])

def p_expr_only_mini(p):
    """ 
        expr : expr miniexpr

    """
    p[0] = Node("EXPR", p[1],Node("MINI", p[2]))

def p_expr_nul(p):
    """
        expr :
    """







def p_capture_group(p):
    """ 
        capture_group : LPARENTHESIS expr RPARENTHESIS
                      | LPARENTHESIS EXCEPTCAPTURE expr RPARENTHESIS
                      | LPARENTHESIS EXCEPTLOOKAHEADPOS expr RPARENTHESIS
                      | LPARENTHESIS EXCEPTLOOKAHEADNEG expr RPARENTHESIS
                      | LPARENTHESIS EXCEPTLOOKBEHINDPOS expr RPARENTHESIS
                      | LPARENTHESIS EXCEPTLOOKBEHINDNEG expr RPARENTHESIS
    """
    p[0] = Node("CAPTURE_GROUP", p[len(p)-2])



def p_alternative(p):
    """ 
    alternative : OR
                | 
    """
    if len(p) > 1:
        p[0] = Node("ALTERNATIVE", p[1])


def p_wtfamidoinghere(p):
    """ 
        wtfamidoinghere : phrase
                        | capture_group
    """
    if len(p) > 2:
        p[0] = Node("PHRASE", p[1],p[2])

    elif len(p) == 2:
        p[0] = Node("CAPTURE_GROUP", p[1])


def p_miniexpr(p):
    """ 
        miniexpr : miniexpr wtfamidoinghere quantifier
                 | 
    """
    if len(p) > 1:
        p[0] = Node("MINIEXPR",p[1],p[2], Node("QUANTIFIER", p[3]))
