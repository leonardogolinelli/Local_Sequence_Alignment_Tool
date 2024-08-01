#!/home/leonardo/miniconda3/envs/numpy_env/bin/python
def draw_matrix_alignment(matrix, coordinates, key, top_sequence, bottom_sequence):
    # Step 1: Ensure the matrix elements are integers
    matrix = matrix.astype(int)
    
    # Step 2: Convert the matrix to a string representation
    str_matrix = matrix.astype(str)
    
    # Step 3: Update the coordinates list
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