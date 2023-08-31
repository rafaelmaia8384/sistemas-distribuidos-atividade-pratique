from multiprocessing import Pool
import time


# Função para calcular o produto escalar de dois sub-vetores
def dot_product(args):
    sub_vector_a, sub_vector_b = args
    return sum(a * b for a, b in zip(sub_vector_a, sub_vector_b))


# Função para calcular o produto escalar de forma sequencial
def sequential_dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))


if __name__ == "__main__":
    # Definindo os vetores
    vector_a = [1, 2, 3, 4, 5] * 10000000  # Tamanho 5000
    vector_b = [5, 4, 3, 2, 1] * 10000000  # Tamanho 5000

    # Calculando o produto escalar de forma sequencial e medindo o tempo
    start_time = time.time()
    result_sequential = sequential_dot_product(vector_a, vector_b)
    end_time = time.time()
    sequential_time = end_time - start_time

    # Dividindo os vetores em partes menores
    # Atribuindo a cada processo uma parte dos vetores para calcular
    step = len(vector_a) // 4  # Dividindo o vetor em 4 partes
    sub_vectors = [
        (vector_a[i : i + step], vector_b[i : i + step])
        for i in range(0, len(vector_a), step)
    ]

    # Calculando o produto escalar de forma paralela e medindo o tempo
    start_time = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(dot_product, sub_vectors)
    end_time = time.time()
    parallel_time = end_time - start_time

    # Somando os resultados de cada processo para obter o resultado final
    result_parallel = sum(results)

    # Comparando os resultados
    print("Resultado sequencial:", result_sequential)
    print("Resultado paralelo:", result_parallel)
    print("Os resultados são iguais:", result_sequential == result_parallel)

    # Comparando os tempos de execução
    print(f"Tempo de execução sequencial: {sequential_time:.4f} segundos")
    print(f"Tempo de execução paralela: {parallel_time:.4f} segundos")
