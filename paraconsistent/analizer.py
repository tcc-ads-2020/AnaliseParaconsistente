import numpy as np


def largest_and_smallest_elements(classes):
    largest_and_smallest = []

    for data_class in classes:
        smallest = np.array([])
        largest = np.array([])

        for array in np.transpose(data_class):
            largest = np.append(largest, np.max(array))
            smallest = np.append(smallest, np.min(array))

        largest_and_smallest.append(np.array([largest, smallest]))

    return np.array(largest_and_smallest)


def similarity_vectors(largest_and_smallest_values):
    vectors = []

    for values in largest_and_smallest_values:
        similarity_vector = []

        for largest_and_smallest in np.transpose(values):
            amplitude = largest_and_smallest[0] - largest_and_smallest[1]
            similarity_vector.append(1 - amplitude)

        vectors.append(similarity_vector)

    return np.array(vectors)


def alpha(classes):
    largest_and_smallest = largest_and_smallest_elements(classes)
    vectors = similarity_vectors(largest_and_smallest)
    means = [np.mean(similarity_vector) for similarity_vector in vectors]

    return np.min(means)
