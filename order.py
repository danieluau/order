import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def test_sorting_algorithm(algorithm, scenario, size):
    arr = generate_scenario(scenario, size)

    start_time = time.time()
    algorithm(arr)
    end_time = time.time()

    return end_time - start_time

def generate_scenario(scenario, size):
    if scenario == 'crescente':
        return list(range(size))
    elif scenario == 'decrescente':
        return list(range(size, 0, -1))
    elif scenario == 'aleatorio':
        return random.sample(range(size), size)

scenarios = ['crescente', 'decrescente', 'aleatorio']
sizes = [1000, 5000, 10000, 20000, 30000]
algorithms = [bubble_sort, insertion_sort, selection_sort]

for algorithm in algorithms:
    for scenario in scenarios:
        times = []
        for size in sizes:
            time_taken = test_sorting_algorithm(algorithm, scenario, size)
            times.append(time_taken)
            print(f'{algorithm.__name__} - {scenario} - {size} elementos: tempo = {time_taken:.6f} segundos')

        plt.plot(sizes, times, label=f'{algorithm.__name__} - {scenario}')

    plt.xlabel('tamanho do vetor')
    plt.ylabel('tempo (segundos)')
    plt.title('desempenho dos algoritmos de ordenação')
    plt.legend()
    plt.savefig(f'{algorithm.__name__}_performance.png')
    plt.clf()  # Limpar a figura para o próximo algoritmo

print("gráficos salvos com sucesso!")
