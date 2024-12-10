import numpy as np

def cosine_similarity_numpy(list1, list2):
    dot_product = np.dot(list1, list2)
    magnitude1 = np.linalg.norm(list1)
    magnitude2 = np.linalg.norm(list2)

    return dot_product / (magnitude1 * magnitude2)