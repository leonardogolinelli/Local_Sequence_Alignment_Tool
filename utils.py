#!/home/leonardo/miniconda3/envs/numpy_env/bin/python
def draw_matrix_alignment(matrix, coordinates, key, top_sequence, bottom_sequence):
    matrix = matrix.astype(int)
    
    str_matrix = matrix.astype(str)
    
    coords = coordinates.copy()
    i, j = key.split(",")
    i, j = int(i), int(j)
    coords.append((i, j))
    
    for x, y in coords:
        str_matrix[x, y] = '!' + str_matrix[x, y]
    
    row_names = '0' + bottom_sequence  
    col_names = '0' + top_sequence  
    
    print('  ' + ' '.join(col_names[:str_matrix.shape[1] + 1]))
    
    for i, row in enumerate(str_matrix):
        print(row_names[i] + ' ' + ' '.join(row))