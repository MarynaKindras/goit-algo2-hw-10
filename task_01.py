import time
import random
from colorama import Fore, Style, init
import matplotlib.pyplot as plt

# Initialize colorama for colored console output
init(autoreset=True)

def randomized_quick_sort(arr):
    """
    Sorts an array using the randomized QuickSort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    """
    Sorts an array using the deterministic QuickSort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def generate_random_array(size):
    """
    Generates a random array of integers.

    Args:
        size (int): The size of the array to generate.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(0, 100000) for _ in range(size)]

def measure_sorting_time(sort_function, arr):
    """
    Measures the time taken to sort an array using a given sorting function.

    Args:
        sort_function (function): The sorting function to use.
        arr (list): The array to sort.

    Returns:
        float: The time taken to sort the array in seconds.
    """
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    """
    Main function to compare the performance of randomized and deterministic QuickSort.
    """
    sizes = [10000, 50000, 100000, 500000]
    results = {"randomized": [], "deterministic": []}

    for size in sizes:
        random_times = []
        deterministic_times = []

        for _ in range(5):
            arr = generate_random_array(size)
            random_time = measure_sorting_time(randomized_quick_sort, arr.copy())
            deterministic_time = measure_sorting_time(deterministic_quick_sort, arr.copy())
            random_times.append(random_time)
            deterministic_times.append(deterministic_time)

        avg_random_time = sum(random_times) / 5
        avg_deterministic_time = sum(deterministic_times) / 5

        results["randomized"].append(avg_random_time)
        results["deterministic"].append(avg_deterministic_time)

        print(f"{Fore.GREEN}Array size: {size}")
        print(f"{Fore.BLUE}Randomized QuickSort: {avg_random_time:.4f} seconds")
        print(f"{Fore.RED}Deterministic QuickSort: {avg_deterministic_time:.4f} seconds")
        print(Style.RESET_ALL)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results["randomized"], label="Randomized QuickSort", marker='o')
    plt.plot(sizes, results["deterministic"], label="Deterministic QuickSort", marker='s')
    plt.xlabel("Array Size")
    plt.ylabel("Average Time (seconds)")
    plt.title("Comparison of Randomized and Deterministic QuickSort")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()