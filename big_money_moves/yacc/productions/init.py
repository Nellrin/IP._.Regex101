from yacc.node import Node


def p_whole(p):
    """ 
        whole : start expr end 
    """

    p[0] = Node("WHOLE", p[1], p[2], p[3])

def p_start(p):
    """ 
        start : START 
              |

    """
    if len(p) > 1:
        p[0] = Node("START", p[1])


def p_end(p):
    """ 
        end : END 
            | 

    """
    if len(p) > 1:
        p[0] = Node("END", p[1])