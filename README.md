# Projeto de Otimização das Rotas no Sistema de Metrô do Recife

## 1. Introdução

Neste projeto, analisamos o sistema de metrô do Recife modelando-o como um grafo. O objetivo é otimizar as rotas entre diferentes estações utilizando algoritmos de busca para determinar a rota mais eficiente em termos de tempo de viagem.

## 2. Resultados Obtidos

A diferença nos tempos totais entre **grafos ponderados** e **não ponderados** foi significativa, com um total de **32 minutos** para o grafo ponderado e **14 minutos** para o grafo não ponderado. Essa discrepância é causada pela forma como os algoritmos lidam com os pesos das arestas.

## 3. Grafos Ponderados

### 3.1. Definição

Em um grafo ponderado, cada aresta possui um valor (peso) que pode representar **distância**, **tempo**, **custo**, entre outros. Esses pesos impactam diretamente a escolha do caminho pelos algoritmos que consideram os pesos, como o Dijkstra.

### 3.2. Exemplo Ponderado

- O menor caminho encontrado por Dijkstra foi:  
  `Camaragibe -> Cosme e Damião -> Rodoviária -> Curado -> Alto do Céu -> Coqueiral -> Tejipió -> Barro -> Recife` com **32 minutos**.
- O algoritmo Dijkstra otimiza o caminho com base nos **tempos de viagem** (pesos), selecionando o que apresenta o menor **somatório de tempos**.

### 3.3. Funcionamento do Algoritmo Dijkstra

- Dijkstra analisa os **pesos das arestas** e determina o caminho com o menor somatório de pesos entre o ponto de partida e o destino.
- **DFS** e **BFS** não consideram os pesos, focando apenas na quantidade de nós ou na exploração do grafo. Isso pode resultar em soluções que não garantem o menor tempo ou custo.

## 4. Grafos Não Ponderados

### 4.1. Definição

Em grafos não ponderados, todas as arestas têm o mesmo valor ou são consideradas com um peso implícito de 1. Assim, os algoritmos buscam o menor caminho em termos de quantidade de arestas, sem considerar o tempo ou a distância.

### 4.2. Exemplo Não Ponderado

- O caminho encontrado foi:  
  `Camaragibe -> Cosme e Damião -> Rodoviária -> Curado -> Alto do Céu -> Coqueiral -> Tejipió -> Barro -> Werneck -> Santa Luzia -> Mangueira -> Ipiranga -> Afogados -> Joana Bezerra -> Recife` com **14 minutos**.
- O algoritmo buscou o menor caminho **em termos de quantidade de arestas**, o que pode não ser realista se estivermos considerando o tempo real de deslocamento.

### 4.3. Funcionamento dos Algoritmos em Grafos Não Ponderados

- **Dijkstra** em grafos não ponderados: O algoritmo se comporta de maneira semelhante ao BFS, encontrando o menor caminho em termos de arestas, pois todas têm o mesmo peso.
- **BFS**: Ideal para encontrar o menor caminho em termos de número de arestas, garantindo o menor número de "paradas".
- **DFS**: Também encontra um caminho, mas não garante que seja o menor em termos de arestas.

## 5. Análise dos Resultados

### 5.1. Comparação de Tempos

- **Grafos Ponderados**: O tempo total reflete o caminho com o menor somatório de pesos, proporcionando uma otimização mais realista baseada em tempo (32 minutos).
- **Grafos Não Ponderados**: O tempo total é menor, mas não reflete a realidade das viagens, já que os pesos não foram considerados (14 minutos).

### 5.2. Resumo das Diferenças

| Tipo de Grafo         | Características                                 | Exemplo de Tempo | Análise                                    |
|-----------------------|------------------------------------------------|------------------|--------------------------------------------|
| Grafo Ponderado       | Pesos variados nas arestas                     | 32 minutos       | Dijkstra prioriza rotas de menor peso total. |
| Grafo Não Ponderado   | Todas as arestas têm o mesmo valor            | 14 minutos       | O foco é minimizar a quantidade de arestas.   |

## 6. Conclusão

As diferenças entre grafos ponderados e não ponderados revelam a importância de considerar os pesos nas arestas ao otimizar rotas em sistemas de transporte como o metrô. Para problemas onde os custos (tempo, distância) variam entre as arestas, a utilização de grafos ponderados e o algoritmo de Dijkstra se mostram mais adequados. Já em situações em que todos os caminhos são equivalentes, grafos não ponderados podem ser utilizados para simplificar a busca.

## 7. Recomendações

- **Uso de Grafos Ponderados**: Para otimização em que o tempo de viagem ou custo varia.
- **Uso de Grafos Não Ponderados**: Quando a equivalência das arestas é uma suposição válida e o foco é minimizar o número de paradas.
