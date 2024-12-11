import timeit
import random
import numpy as np
from cosine_similarity_python import cosine_similarity_numpy
from cosine_similarity_cython import cosine_similarity_cython
def generate_test_data():
    return np.array(np.random.rand(1000000))
reps = 1000
if __name__ == "__main__":
    test_data_1 = generate_test_data()
    test_data_2 = generate_test_data()
    python_time = timeit.timeit(
        stmt="cosine_similarity_numpy(test_data_1,test_data_2)",
        setup="from __main__ import cosine_similarity_numpy, test_data_1, test_data_2",
        number=reps
    )
    cython_time = timeit.timeit(
        stmt="cosine_similarity_cython(test_data_1,test_data_2)",
        setup="from __main__ import cosine_similarity_cython, test_data_1, test_data_2",
        number=reps
    )
    
    print(f"Python implementation runtime for cosine_similarity: {python_time:.10f} seconds (average over {reps} runs)")
    print(f"Cython implementation runtime for cosine_similarity: {cython_time:.10f} seconds (average over {reps} runs)")

    speedup = python_time / cython_time
    print(f"Cython is approximately {speedup:.5f}x faster than Python")
