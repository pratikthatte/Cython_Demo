def cosine_similarity_cython(double[:] list1, double[:] list2):
    cdef int length = list1.shape[0]
    cdef double dot_product = 0.0
    cdef double magnitude1 = 0.0
    cdef double magnitude2 = 0.0
    cdef int i

    for i in range(length):
        dot_product += list1[i] * list2[i]
        magnitude1 += list1[i] * list1[i]
        magnitude2 += list2[i] * list2[i]

    magnitude1 = magnitude1 ** 0.5
    magnitude2 = magnitude2 ** 0.5

    return dot_product / (magnitude1 * magnitude2)
