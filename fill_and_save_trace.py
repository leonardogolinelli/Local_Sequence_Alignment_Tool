
import numpy as np

def fill_and_trace(scores, top_sequence, bottom_sequence):
    def s(xi,xj):
        return scores["match"] if xi == xj else scores["mismatch"]

    def match_mismatch(i,j, xi, xj, matrix):
        return matrix[i-1,j-1] + s(xi, xj)

    #maxk=0…i-1F(k, j) - γ(i - k)
    def γ(n):
        return n * scores["gap"]

    def row_gaps_score(i,j):
        gap_scores = []
        for k in range((i)):
            gap_score = matrix[k,j] - γ(i-k)
            gap_scores.append(gap_score)
        
        max_score = np.max(gap_scores)
        kth_rows = tuple([k for k,value in enumerate(gap_scores) if value==max_score])
        #print(kth_rows)
        return max_score, kth_rows

    #maxk=0…j-1F(i, k) - γ(j - k),
    def col_gaps_score(i,j):
        gap_scores = []
        for k in range((j)):
            gap_score = matrix[i,k] - γ(j-k)
            gap_scores.append(gap_score)

        max_score = np.max(gap_scores)
        kth_cols = tuple([k for k,value in enumerate(gap_scores) if value==max_score])
        #print(kth_cols)
        return max_score, kth_cols

    n_rows = len(bottom_sequence)+1
    n_cols = len(top_sequence)+1

    matrix = np.zeros((n_rows, n_cols))
    traceback_dic = {}

    for i in range(1,n_rows):
        for j in range(1,n_cols):
            #print(f"i: {i}, j: {j}")
            xi = bottom_sequence[i-1]
            xj = top_sequence[j-1]
            score1 = match_mismatch(i,j, xi, xj, matrix)
            score2, kth_rows = row_gaps_score(i,j)
            score3, kth_cols = col_gaps_score(i,j)
            top_score = max(score1, 
                            score2, 
                            score3, 
                            0)
            
            matrix[i,j] = top_score

            top_idx = [t for t, value in enumerate([score1, score2, score3]) if value == top_score]
            traceback_dic[f"{i},{j}"] = []
            for idx in top_idx:
                #print(f"i,j: {i},{j}: ",end=" ")
                #print(traceback_dic[f"{i},{j}"])
                if top_score > 0:
                    if idx == 0:
                        traceback_dic[f"{i},{j}"].append((i-1,j-1))
                    elif idx == 1:
                        for k in kth_rows:
                            traceback_dic[f"{i},{j}"].append((k,j))
                    elif idx == 2:
                        for k in kth_cols:
                            traceback_dic[f"{i},{j}"].append((i,k))     

    return matrix, traceback_dic          

if __name__ == "__main__":
    _,_,_, matrix, traceback_dic = fill_and_trace()
    print(matrix)
    print(traceback_dic)

