import re
from graphviz import Digraph

def analisar_regex(regex):
    tokens = []
    i = 0
    while i < len(regex):
        c = regex[i]

        if c in ('^', '$'):
            i += 1
            continue

        token = ""

        if c == '\\' and i + 1 < len(regex):
            token = f"\\{regex[i+1]}"
            i += 2
        elif c == '[':
            j = i + 1
            while j < len(regex) and regex[j] != ']':
                j += 1
            token = regex[i:j+1] if j < len(regex) else regex[i:]
            i = j + 1 if j < len(regex) else i + 1
        elif c == '(':
            j = i + 1
            level = 1
            while j < len(regex) and level > 0:
                if regex[j] == '(':
                    level += 1
                elif regex[j] == ')':
                    level -= 1
                j += 1
            token = regex[i:j] if level == 0 else regex[i:]
            i = j
        elif c.isalnum():
            token = f"'{c}'"
            i += 1
        else:
            token = c
            i += 1

        if i < len(regex) and regex[i] in '*+?':
            token += regex[i]
            i += 1

        tokens.append(token)

    return tokens

def substituir_classes(token):
    token = token.replace(r'\\w', '[a-zA-Z0-9_]')
    token = token.replace(r'\\d', '[0-9]')
    return token

def rotulo_estado(token):
    return substituir_classes(token)

def rotulo_transicao(token):
    label = token[:-1] if token and token[-1] in '*+?' else token
    label = substituir_classes(label)
    return label

def extrair_opcoes_classe(token):
    if token.startswith('[') and token.endswith(']'):
        conteudo = token[1:-1]
        return [f"'{c}'" for c in conteudo]
    return None

def extrair_opcoes_alternancia(token):
    if token.startswith('(') and token.endswith(')'):
        conteudo = token[1:-1]
        opcoes = conteudo.split('|')
        def formata(op):
            op = op.strip()
            if len(op) == 1 and (op.isalnum() or op in ['\\d','\\w']):
                return substituir_classes(op) if op.startswith('\\') else f"'{op}'"
            return op
        return [formata(op) for op in opcoes]
    return None

def desenhar_automato(padrao, nome="automato"):
    tokens = analisar_regex(padrao)
    dot = Digraph()
    dot.attr(rankdir='LR')
    dot.node("S0", "Início", shape="circle")

    estado_atual = 0
    i = 0
    while i < len(tokens):
        token = tokens[i]
        current_state = f"S{estado_atual}"

        quantificador = None
        if token and token[-1] in '*+?':
            quantificador = token[-1]
            token_principal = token[:-1]
        else:
            token_principal = token

        if token_principal.startswith('(') and token_principal.endswith(')') and quantificador == '?':
            opcoes = extrair_opcoes_alternancia(token_principal)
            if opcoes is None:
                opcoes = [token_principal]

            estado_final_do_grupo = estado_atual + 1 + len(opcoes)
            dot.node(f"S{estado_final_do_grupo}", "", shape="circle")

            dot.edge(current_state, f"S{estado_final_do_grupo}", style="dashed", label="(opcional)")

            for idx, op in enumerate(opcoes):
                estado_intermediario = estado_atual + 1 + idx
                dot.node(f"S{estado_intermediario}", rotulo_estado(op), shape="circle")
                dot.edge(current_state, f"S{estado_intermediario}", label=rotulo_transicao(op))
                dot.edge(f"S{estado_intermediario}", f"S{estado_final_do_grupo}")

            estado_atual = estado_final_do_grupo
            i += 1
            continue

        next_state = f"S{estado_atual + 1}"
        dot.node(next_state, rotulo_estado(token), shape="circle")

        opcoes_alt = extrair_opcoes_alternancia(token_principal)
        opcoes_cls = extrair_opcoes_classe(token_principal)

        if opcoes_alt:
            for op in opcoes_alt:
                dot.edge(current_state, next_state, label=rotulo_transicao(op))
        elif opcoes_cls:
            for op in opcoes_cls:
                dot.edge(current_state, next_state, label=op)
        else:
            dot.edge(current_state, next_state, label=rotulo_transicao(token_principal))

        if quantificador in ('*', '+'):
            dot.edge(next_state, next_state, label=rotulo_transicao(token_principal))

        if quantificador in ('?', '*'):
            estado_pular = estado_atual + 2
            if estado_pular <= len(tokens):
                dot.edge(current_state, f"S{estado_pular}", style="dashed", label="(opcional)")

        estado_atual += 1
        i += 1

    dot.node(f"S{estado_atual + 1}", "Fim", shape="doublecircle")
    dot.edge(f"S{estado_atual}", f"S{estado_atual + 1}", label="✓")

    dot.render(filename=nome, format='png', cleanup=True, view=True)

def testar_regex_com_automato(index, total, texto, padrao, ignorar_maiusculas=False):
    i = 0
    flags = re.IGNORECASE if ignorar_maiusculas else 0
    resultado = re.fullmatch(padrao, texto, flags)
    print(f"\033[1m({index}/{total})\033[0m✅Passou! \033[1m'{texto}'\033[0m" if resultado else f"\033[1m({index}/{total})\033[0m❌Rejeite! \033[1m'{texto}'\033[0m")
    return resultado
