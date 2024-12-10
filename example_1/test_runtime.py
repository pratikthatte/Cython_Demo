import timeit
import random
from python_example_1 import count_number_of_increases
from cython_example_1 import count_number_of_increases_cy
def generate_test_data(size):
    return [random.randint(0, 1000) for _ in range(size)]
reps = 100
if __name__ == "__main__":
    test_data = generate_test_data(10000)
    python_time = timeit.timeit(
        stmt="count_number_of_increases(test_data)",
        setup="from __main__ import count_number_of_increases, test_data",
        number=reps
    )
    cython_time = timeit.timeit(
        stmt="count_number_of_increases_cy(test_data)",
        setup="from __main__ import count_number_of_increases_cy, test_data",
        number=reps
    )

    print(f"Python implementation runtime: {python_time:.10f} seconds (average over {reps} runs)")
    print(f"Cython implementation runtime: {cython_time:.10f} seconds (average over {reps} runs)")

    speedup = python_time / cython_time
    print(f"Cython is approximately {speedup:.5f}x faster than Python")
