from multiprocessing import Pool, cpu_count

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        return pool.map(factorize, numbers)

if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    results = factorize_parallel(numbers)
    for result in results:
        print(result)
