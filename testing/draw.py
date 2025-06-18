from graphviz import Digraph

def draw_graph():
    # Cria um novo gráfico direcionado
    dot = Digraph(comment='Exemplo de Gráfico com Graphviz')

    # Adiciona nós (círculos e quadrados) com nomes
    dot.node('A', 'Nó A', shape='circle')  # Círculo
    dot.node('B', 'Nó B', shape='circle')  # Círculo
    dot.node('C', 'Nó C', shape='square')  # Quadrado
    dot.node('D', 'Nó D', shape='square')  # Quadrado
    dot.node('E', 'Nó E', shape='doublecircle')  # Círculo

    # Adiciona arestas (linhas) com nomes
    dot.edge('A', 'B', label='Linha 1')
    dot.edge('B', 'C', label='Linha 2')
    dot.edge('C', 'D', label='Linha 3')
    dot.edge('D', 'E', label='Linha 4')
    dot.edge('E', 'A', label='Linha 5')

    # Renderiza o gráfico em um arquivo
    dot.render('graph_output', view=True, format='png')

if __name__ == '__main__':
    draw_graph()