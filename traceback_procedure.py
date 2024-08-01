#!/home/leonardo/miniconda3/envs/numpy_env/bin/python
import numpy as np


def run_traceback(scores, top_sequence, bottom_sequence, matrix, traceback_dic):
    def recursive_traceback(matrix, traceback_dic, traceback_paths, i,j, i0,j0):
        while matrix[i0,j0] > 0:
            i0,j0 = traceback_dic[f"{i0},{j0}"][0] #fetches the first element, prioritizes diagonal > up > left
            traceback_paths[f"{i},{j}"].append((i0,j0))

    sorted_score_set = np.sort(list(set(matrix.flatten())))[::-1]
    best_score = sorted_score_set[0]
    second_best_score = sorted_score_set[1] #not used or shown for code simplicity
    max_indices = np.argwhere(matrix == best_score)
    max_indices
    traceback_paths = {}
    for idx_pair in max_indices:
        i,j = idx_pair
        traceback_paths[f"{i},{j}"] = []

        recursive_traceback(matrix, traceback_dic, traceback_paths, i,j, i0=i,j0=j)

    return traceback_paths, best_score

if __name__ == "__main__":
    _, _, _, _, _, traceback_paths, best_score = run_traceback()
    print(best_score)
    print(traceback_paths)
