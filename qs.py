import time
import tracemalloc
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def benchmark_quicksort(arr):
    tracemalloc.start()
    start_time = time.time()
    
    sorted_arr = quicksort(arr)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    memory_usage = peak / 10**6  # Convert to MB
    
    return sorted_arr, execution_time, memory_usage

# Generar conjuntos de datos
small_data = [random.randint(0, 1000) for _ in range(100)]
medium_data = [random.randint(0, 1000) for _ in range(300)]
large_data = [random.randint(0, 1000) for _ in range(500)]

# Benchmarking
print("Conjunto pequeño (100 elementos):")
sorted_small, time_small, memory_small = benchmark_quicksort(small_data)
print(f"Tiempo de ejecución: {time_small:.6f} segundos")
print(f"Uso de memoria: {memory_small:.6f} MB")

print("\nConjunto mediano (300 elementos):")
sorted_medium, time_medium, memory_medium = benchmark_quicksort(medium_data)
print(f"Tiempo de ejecución: {time_medium:.6f} segundos")
print(f"Uso de memoria: {memory_medium:.6f} MB")

print("\nConjunto grande (500 elementos):")
sorted_large, time_large, memory_large = benchmark_quicksort(large_data)
print(f"Tiempo de ejecución: {time_large:.6f} segundos")
print(f"Uso de memoria: {memory_large:.6f} MB")
