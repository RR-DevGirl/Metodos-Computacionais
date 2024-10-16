# Quick -> Lucas
import math
from time import time
from datetime import datetime
import heapq


def conv(evento):
    return datetime.strptime(f"{evento['data']} {evento['hora']}", "%d/%m/%Y %H:%M")


def quicksort(eventos, esq, dir):
    if esq < dir:
        particao_pos = particao(eventos, esq, dir)
        quicksort(eventos, esq, particao_pos - 1)
        quicksort(eventos, particao_pos + 1, dir)


def particao(eventos, esq, dir):
    i = esq
    j = dir - 1
    pivo = conv(eventos[dir])

    while i < j:
        while i < dir and conv(eventos[i]) < pivo:
            i += 1
        while j > esq and conv(eventos[j]) >= pivo:
            j -= 1
        if i < j:
            eventos[i], eventos[j] = eventos[j], eventos[i]
    if conv(eventos[i]) > pivo:
        eventos[i], eventos[dir] = eventos[dir], eventos[i]
    return i


def conv(eventos):
    eventos_convertidos = []
    for data_hora, descricao in eventos:
        data_hora_formatada = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        eventos_convertidos.append((data_hora_formatada, descricao))
    return eventos_convertidos


def heapsort(eventos):
    n = len(eventos)
    start_time = time.time()
    heapq.heapify(eventos)

    eventos_ordenados = []
    while eventos:
        eventos_ordenados.append(heapq.heappop(eventos))

    end_time = time.time()

    tempo_execucao = end_time - start_time
    operacoes_estimadas = n * (n.bit_length() - 1)  # O(n log n) em termos de operações
    print(f"Tempo de execução do heapsort: {tempo_execucao:.6f} segundos")
    print(f"Complexidade do heapsort: O(n log n) com n = {n}")
    print(f"Número estimado de operações: {operacoes_estimadas}")

    return eventos_ordenados


def adicionar_evento(eventos, novos_eventos):
    for data_hora, descricao in novos_eventos:
        data_hora_formatada = datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
        heapq.heappush(eventos, (data_hora_formatada, descricao))


def remover_evento(eventos, descricao):
    eventos[:] = [evento for evento in eventos if evento[1] != descricao]
    heapq.heapify(eventos)


def exibir_eventos(eventos):
    for evento in eventos:
        print(evento[0].strftime("%d/%m/%Y %H:%M"), "-", evento[1])


lista = [
    {
        "nome": "Olha! Recife a Pé",
        "data": "27/09/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
    {
        "nome": "Olha! Recife no Rio",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Ilha de Deus",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Jardim Botânico",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "14:00",
        "local": "Instituto Ricardo Brennand",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "29/09/2024",
        "hora": "13:00",
        "local": "Fundação Gilberto Freyre",
    },
    {
        "nome": "Olha! Recife Pedalando",
        "data": "29/09/2024",
        "hora": "09:00",
        "local": "Antigos Cinemas do Recife",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "02/10/2024",
        "hora": "14:00",
        "local": "Pátio do Terço e Arredores",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "04/10/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
]
ini = time()
quicksort(lista, 0, len(lista) - 1)
fim = time()
complex_quick = len(lista) * math.log2(len(lista))
print("Lista Organizada")
for evento in lista:
    print(f"{evento['nome']} - {evento['data']} {evento['hora']} - {evento['local']}")
print(f"Tempo de execução: {fim-ini}")
print(f"Complexidade - {complex_quick}")

lista_add = [
    {
        "nome": "Olha! Recife a Pé",
        "data": "27/09/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
    {
        "nome": "Olha! Recife no Rio",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Ilha de Deus",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Jardim Botânico",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "14:00",
        "local": "Instituto Ricardo Brennand",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "29/09/2024",
        "hora": "13:00",
        "local": "Fundação Gilberto Freyre",
    },
    {
        "nome": "Olha! Recife Pedalando",
        "data": "29/09/2024",
        "hora": "09:00",
        "local": "Antigos Cinemas do Recife",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "02/10/2024",
        "hora": "14:00",
        "local": "Pátio do Terço e Arredores",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "04/10/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
    {
        "nome": "Olha! Recife Noturno",
        "data": "01/10/2024",
        "hora": "21:00",
        "local": "Tour Histórico",
    },
    {
        "nome": "Olha! Recife Pedalando",
        "data": "29/09/2024",
        "hora": "09:00",
        "local": "Antigos Cinemas do Recife",
    },
    {
        "nome": "Olha! Recife de Barco",
        "data": "26/09/2024",
        "hora": "12:00",
        "local": "Passeio no Capibaribe",
    },
]
ini = time()
quicksort(lista_add, 0, len(lista_add) - 1)
fim = time()
complex_quick = len(lista_add) * math.log2(len(lista_add))
print("\n\nLista Organizada")
for evento in lista_add:
    print(f"{evento['nome']} - {evento['data']} {evento['hora']} - {evento['local']}")
print(f"Tempo de execução: {fim-ini}")
print(f"Complexidade - {complex_quick}")


eventos_convertidos = conv(lista)
eventos_ordenados = heapsort(eventos_convertidos)

print("Eventos ordenados inicialmente:")
exibir_eventos(eventos_ordenados)

print("\nAdicionando novos eventos:")
adicionar_evento(eventos_ordenados, lista_add)
eventos_ordenados = heapsort(eventos_ordenados)  # Reordena após a adição
exibir_eventos(eventos_ordenados)

print("\nRemovendo evento:")
remover_evento(eventos_ordenados, "Olha! Recife no Rio – Ilha de Deus")
eventos_ordenados = heapsort(eventos_ordenados)  # Reordena após a remoção
exibir_eventos(eventos_ordenados)
