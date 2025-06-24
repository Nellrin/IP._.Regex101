class Node:
    __slots__ = ("kind", "children")
    
    def __init__(self, kind, *children):
        self.kind = kind
        self.children = list(children)

    def __repr__(self, lvl=0):
        if all(isinstance(c, Node) and c.kind == "None" for c in self.children):
            return ""  

        pad = "   " * lvl
        if not self.children:
            return f"{pad}({self.kind})"

        out = f"{pad}+ {self.kind}"
        for c in self.children:
            if isinstance(c, Node):
                sub = c.__repr__(lvl + 1)
                if sub: 
                    out += "\n" + sub
            else:
                if c is not None:
                    out += "\n" + "   " * lvl + "|  {" + repr(c) + "}"
        return out