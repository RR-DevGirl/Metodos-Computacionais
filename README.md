# Projetos avaliativos para a cadeira de métodos computacionais
## Professora responsavel: Amanda
## Alunos: Lucas Alves, Lucas Eduardo e Rebeca Regina


# Projeto de Otimização das Rotas no Sistema de Metrô do Recife e Organização Dinâmica da Agenda do "Olha! Recife"

## Questão 1: Otimização das Rotas no Sistema de Metrô do Recife

### 1. Introdução

A cidade do Recife possui um sistema de metrô com várias estações interligadas. O atual mapa do metrô apresenta diversas possibilidades de rotas, e algumas conexões são mais rápidas do que outras. O objetivo é encontrar a rota mais rápida para viagens frequentes entre estações.

![enter image description here](./Otimização%20das%20Rotas%20no%20Sistema%20de%20Metrô%20do%20Recife/docs/mapa-metro-recife-simplificado.jpg)

### 2. Proposta de Problema

Modelar o sistema de metrô como um grafo:
- Cada estação é um nó.
- Cada conexão direta entre duas estações é uma aresta, com um peso associado representando o tempo de viagem entre elas.

### 3. Algoritmos a serem Utilizados

1. **Dijkstra**:
   - Utilizado em grafos ponderados, onde as arestas têm pesos que representam o tempo de viagem. Este algoritmo encontra o caminho mais curto considerando a soma dos pesos das arestas.

2. **BFS (Busca em Largura)**:
   - Ideal para grafos não ponderados. Explora todos os vizinhos de um nó antes de passar para o próximo nível, garantindo que o caminho encontrado tenha o menor número de arestas.


3. **DFS (Busca em Profundidade)**:
   - Explora o máximo possível ao longo de um caminho antes de retroceder. Pode encontrar um caminho, mas não garante que seja o menor em termos de arestas.


## 4. Análise dos Resultados

### Resultados dos Algoritmos

**Grafo Ponderado:**  
O menor caminho encontrado pelo algoritmo de Dijkstra foi:
- **Caminho:** Camaragibe → Cosme e Damião → Rodoviária → Curado → Alto do Céu → Coqueiral → Tejipió → Barro → Recife  
- **Tempo total:** 32 minutos.

**Grafo Não Ponderado:**  
O caminho encontrado foi:
- **Caminho:** Camaragibe → Cosme e Damião → Rodoviária → Curado → Alto do Céu → Coqueiral → Tejipió → Barro → Werneck → Santa Luzia → Mangueira → Ipiranga → Afogados → Joana Bezerra → Recife  
- **Tempo total:** 14 minutos.

### Comparação de Algoritmos

Ao realizar buscas entre os pontos definidos, os seguintes tempos de execução e resultados foram observados:

- **Dijkstra:**
  - **Tempo de Execução:** 0.000102519 segundos
  - **Menor caminho de Barro até Shopping:** Barro → Werneck → Santa Luzia → Mangueira → Ipiranga → Afogados → Imbiribeira → Antônio Falcão → Shopping  
  - **Tempo total:** 8 minutos.

- **Busca em Largura (BFS):**
  - **Tempo de Execução:** 4.887580e-05 segundos
  - **Menor caminho de Barro até Shopping:** Barro → Werneck → Santa Luzia → Mangueira → Ipiranga → Afogados → Imbiribeira → Antônio Falcão → Shopping  
  - **Tempo total:** 8 minutos.

- **Busca em Profundidade (DFS):**
  - **Tempo de Execução:** 5.173683e-05 segundos
  - **Menor caminho de Barro até Shopping:** Barro → Werneck → Santa Luzia → Mangueira → Ipiranga → Afogados → Imbiribeira → Antônio Falcão → Shopping  
  - **Tempo total:** 8 minutos.

### Análise das Diferenças entre Grafos Ponderados e Não Ponderados

#### Grafos Ponderados:
- **Características:**
  - As arestas possuem pesos diferentes, representando custos variados, como tempo de viagem ou distância.
  - O algoritmo de Dijkstra é utilizado para encontrar o menor caminho com base no custo total (tempo) associado a cada aresta.

- **Observações:**
  - Dijkstra considera o tempo de viagem como um fator crucial na determinação do caminho mais curto. 
  - Isso resulta em um caminho que pode ser mais longo em termos de distância, mas mais eficiente em termos de tempo, como evidenciado pelo caminho de Camaragibe a Recife.

#### Grafos Não Ponderados:
- **Características:**
  - As arestas têm o mesmo peso (custo igual), o que simplifica a análise do caminho.
  - O objetivo é minimizar a quantidade de arestas, ignorando o custo associado a cada aresta.

- **Observações:**
  - Os algoritmos BFS e DFS, utilizados em grafos não ponderados, focam na simplicidade e na exploração do espaço de busca sem levar em conta a duração da viagem. 
  - Isso frequentemente resulta em um caminho mais longo em termos de distância, mas o tempo total pode ser semelhante ao encontrado em um grafo ponderado, especialmente quando a estrutura do grafo é favorável.

### 5. Considerações Finais e melhorias no metro

A análise dos resultados demonstra claramente as diferenças de desempenho a depender dos algoritmos e quando aplicados a grafos ponderados e não ponderados. Para rotas em uma rede de transporte, a escolha do algoritmo e a estrutura do grafo (ponderado ou não) têm um impacto significativo na eficiência do trajeto final e no tempo de execução. Em cenários onde o tempo é crítico, a implementação de algoritmos como Dijkstra em grafos ponderados é preferível, enquanto grafos não ponderados podem ser utilizados para situações onde a simplicidade e a exploração são mais relevantes.
Com isso podemos concluir que esses sistemas quando melhores lapidados e treinados com mais dados de diferentes horários, poderia trazer uma leitura mais assertiva e dinamica dos melhores trajetos para cada hora além de ajudar na constante analise da eficiencia do atual sistema. Afinal só conseguimos tomar decisões com dados.

---

## Questão 2: Organização Dinâmica da Agenda do "Olha! Recife" com Algoritmos de Ordenação

### 1. Introdução

A iniciativa "Olha! Recife" possui uma agenda cheia de eventos turísticos que são frequentemente atualizados. Para garantir acesso a uma agenda organizada, é necessário implementar um sistema que ordene esses eventos em ordem cronológica automaticamente.

### 2. Lista de Eventos Agendados

- **Olha! Recife a Pé**: 27/09/2024, 09:30 h – Recife Walking Tour
- **Olha! Recife no Rio**: 28/09/2024, 09:00 h – Ilha de Deus
- **Olha! Recife de Ônibus**: 28/09/2024, 09:00 h – Jardim Botânico
- **Olha! Recife de Ônibus**: 28/09/2024, 14:00 h – Instituto Ricardo Brennand
- **Olha! Recife de Ônibus**: 29/09/2024, 13:00 h – Fundação Gilberto Freyre
- **Olha! Recife Pedalando**: 29/09/2024, 09:00 h – Antigos Cinemas do Recife
- **Olha! Recife a Pé**: 02/10/2024, 14:00 h – Pátio do Terço e Arredores
- **Olha! Recife a Pé**: 04/10/2024, 09:30 h – Recife Walking Tour

### 3. Tarefas a Serem Implementadas

1. **Implementar um Algoritmo de Ordenação**:
   - Utilize diferentes algoritmos de ordenação, como **Mergesort**, **Quicksort** e **Heapsort**, para organizar os eventos sempre que houver uma mudança.

2. **Ordenação da Lista Inicial**:
   - Ordene a lista inicial de eventos fornecida.

3. **Adicionar Novos Eventos**:
   - Adicione os seguintes novos eventos e reorganize a lista:
     - **Olha! Recife Noturno - Tour Histórico**: 01/10/2024, 21:00
     - **Olha! Recife Pedalando - Antigos Cinemas do Recife**: 29/09/2024, 09:00
     - **Olha! Recife de Barco - Passeio no Capibaribe**: 26/09/2024, 12:00

### 4. Análise de Desempenho

1. **Medir o Tempo de Execução**:
   - Compare o tempo de execução de cada algoritmo ao reorganizar a lista quando novos eventos são adicionados.

2. **Análise da Complexidade**:
   - Analise a complexidade dos algoritmos para listas que mudam frequentemente e sugira qual algoritmo seria o mais eficiente para manter a lista de eventos sempre atualizada.

3. **Justificativa da Importância da Ordenação Eficiente**:
   - Discuta como um sistema de ordenação eficiente pode melhorar a experiência do usuário ao visualizar a agenda atualizada.

### 5. Algoritmos de Ordenação

#### 5.1. Mergesort

- **Descrição**: Algoritmo de ordenação que utiliza a técnica de divisão e conquista, dividindo a lista em sublistas até que cada sublista tenha um único elemento e, em seguida, mesclando as sublistas de forma ordenada.
- **Complexidade**: O(n log n) em todos os casos.

#### 5.2. Quicksort

- **Descrição**: Um algoritmo que utiliza a técnica de divisão e conquista, escolhendo um "pivô" e particionando a lista em elementos menores e maiores que o pivô. Os sub-arranjos são então ordenados recursivamente.
- **Complexidade**: O(n log n) em média.

#### 5.3. Heapsort

- **Descrição**: Um algoritmo de ordenação baseado em estruturas de dados de heap. Ele transforma a lista em um heap e remove o maior elemento repetidamente.
- **Complexidade**: O(n log n) em todos os casos.

### 6. Considerações Finais

Um sistema de ordenação eficiente é crucial para garantir que os usuários tenham acesso a uma agenda atualizada e organizada. Isso melhora a experiência do usuário e assegura que os turistas possam planejar seus passeios de forma eficaz.

## Conclusão

As duas questões abordam a otimização e organização de informações, demonstrando a importância de algoritmos adequados em diferentes contextos. Tanto na otimização de rotas no metrô quanto na organização da agenda de eventos, a escolha do algoritmo adequado é fundamental para melhorar a eficiência e a experiência do usuário.
