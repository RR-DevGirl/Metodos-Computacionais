from time import time
import heapq
from collections import deque
from MapaMetro import (metro_map, metro_map_n_pond)
# 1° Questão

def dijkstra(grafo, origem, destino=None):
    distancias = {estacao: float('inf') for estacao in grafo}
    distancias[origem] = 0
    caminho = {estacao: None for estacao in grafo}
    fila_prioridade = [(0, origem)]
    visitados = set()
    while fila_prioridade:
        tempo_atual, estacao_atual = heapq.heappop(fila_prioridade)
        if estacao_atual in visitados:
            continue
        visitados.add(estacao_atual)
        if estacao_atual == destino:
            break
        for vizinho, peso in grafo[estacao_atual]:
            novo_tempo = tempo_atual + peso
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                caminho[vizinho] = estacao_atual
                heapq.heappush(fila_prioridade, (novo_tempo, vizinho))
        return caminho, distancias[destino]

def bfs(metro_map, origem, destino):
    visitados = set()
    fila = deque([(origem, [origem], 0)])
    while fila:
        estacao_atual, caminho, distancia_total = fila.popleft()
        if estacao_atual == destino:
            return caminho, distancia_total
        if estacao_atual not in visitados:
            visitados.add(estacao_atual)
            for vizinho, distancia in metro_map.get(estacao_atual, []):
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho], distancia_total + distancia))
    return caminho, distancia_total


def dfs(grafo, caminho_atual, estacao_atual, estacao_destino, tempo_total, melhor_caminho, melhor_tempo):
    # Adiciona a estação atual ao caminho
    caminho_atual.append(estacao_atual)

    # Se chegamos à estação de destino, verificamos se o caminho atual é o melhor
    if estacao_atual == estacao_destino:
        if tempo_total < melhor_tempo[0]:  # Se o tempo total é menor que o melhor tempo
            melhor_tempo[0] = tempo_total
            melhor_caminho.clear()
            melhor_caminho.extend(caminho_atual)
    else:
        # Explora as conexões da estação atual
        for vizinho, tempo in grafo.get(estacao_atual, []):  # Usa .get() para evitar KeyError
            if vizinho not in caminho_atual:  # Para evitar ciclos
                dfs(grafo, caminho_atual, vizinho, estacao_destino, tempo_total + tempo, melhor_caminho, melhor_tempo)
    
    # Remove a estação atual do caminho (backtracking)
    caminho_atual.pop()

# Função principal para encontrar o caminho mais rápido
def encontrar_caminho_mais_rapido(grafo, origem, destino):
    melhor_caminho = []  # Lista para armazenar o melhor caminho encontrado
    melhor_tempo = [float('inf')]  # Inicia com um tempo infinito
    # Chama a função DFS
    dfs(grafo, [], origem, destino, 0, melhor_caminho, melhor_tempo)
    
    # Verifica se o tempo encontrado não é infinito (ou seja, se encontrou um caminho)
    if melhor_tempo[0] == float('inf'):
        return [], "Caminho não encontrado"
    
    return melhor_caminho, melhor_tempo[0]


def reconstruir_caminho(caminho, destino):
    caminho_final = []
    estacao_atual = destino
    while estacao_atual is not None:
        caminho_final.append(estacao_atual)
        estacao_atual = caminho[estacao_atual]
    caminho_final.reverse()
    return caminho_final


def processaResposta(metodo, tempoExecucaoMetodo, origem, destino, trajetoria, tempoTrajetoria):
    print(f'\n{metodo}:')
    print(f'Tempo de Execução: {tempoExecucaoMetodo} segundos.')
    print(f"Menor caminho de {origem} até {destino}: {' -> '.join(trajetoria)}")
    print(f"Tempo total: {tempoTrajetoria} minutos.\n")

# Teste inicial: Camaragibe -> Cajueiro Seco
origem = input('Informe a origem: ')
destino = input('Informe o destino: ')
op = 0
while True:
  op = int(input('Insira uma opção:\n1- Grafo Ponderado\n2- Não Ponderado\n3- Sair\n'))
  if op == 1:
    #Dijkstra
    ini = time()
    caminho, tempo_total = dijkstra(metro_map, origem, destino)
    caminho_final = reconstruir_caminho(caminho, destino)
    fim = time()
    processaResposta('Dijkstra', (fim-ini), origem, destino, caminho_final, tempo_total)

    #BFS
    ini = time()
    caminho, tempo_total = bfs(metro_map, origem, destino)
    fim = time()
    processaResposta('BFS', (fim-ini), origem, destino, caminho, tempo_total)

    #DFS
    ini = time()
    caminho, tempo_total = encontrar_caminho_mais_rapido(metro_map, origem, destino)
    fim = time()
    processaResposta('DFS', (fim-ini), origem, destino, caminho, tempo_total)

  elif op == 2:
    #Dijkstra
    ini = time()
    distancias, caminho, tempo_total = dijkstra(metro_map_n_pond, origem, destino)
    caminho_final = reconstruir_caminho(caminho, origem, destino)
    fim = time()
    processaResposta('Dijkstra', (fim-ini), origem, destino, caminho_final, tempo_total)

    #BFS
    ini = time()
    caminho, distancia_total = bfs(metro_map_n_pond, origem, destino)
    fim = time()
    processaResposta('BFS', (fim-ini), origem, destino, caminho, tempo_total)

    #DFS
    ini = time()
    caminho, tempo = dfs(metro_map_n_pond, origem, destino)
    fim = time()
    processaResposta('DFS', (fim-ini), origem, destino, caminho, tempo_total)

  elif op == 3:
    print('Saindo.')
    break
  else:
    print('Opção Invalida, tente novamente.')

