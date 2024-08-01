
from utils import draw_matrix_alignment

def write_alignment_fcn(
        scores, 
        top_sequence, 
        bottom_sequence, 
        matrix, 
        traceback_dic, 
        traceback_paths,
        best_score
    ):
        
    for num, key in enumerate(traceback_paths):
        i,j = key.split(",")
        i,j = int(i),int(j)
        top_seq = ""
        bot_seq = ""
        top_sequence_add = " " + top_sequence
        bottom_sequence_add = " " + bottom_sequence

        #print(top_sequence)
        #print(bottom_sequence)

        for it, idx_pair in enumerate(traceback_paths[f"{i},{j}"]):
            #print(it, idx_pair)
            i_new,j_new = idx_pair

            if it==0:
                i_old, j_old = i, j

            diff_top = j_old - j_new
            diff_bot = i_old - i_new
            #print(it, diff_bot, diff_top, i_new, j_new, i_old, j_old)
            #print(top_seq)
            #print(bot_seq)
            #test = (not top_sequence_add[j_old] == " ") and (not bottom_sequence_add[j_old] == " ") #and (not matrix[i_new, j_new] == 0)
            test = True
            if diff_top == diff_bot == 1:
                top_seq += top_sequence_add[j_old]
                bot_seq += bottom_sequence_add[i_old]
            elif diff_top >= 1 and diff_bot == 0:
                top_seq += (diff_top-1) * "-" + top_sequence_add[j_old] 
                bot_seq += diff_top * "-"
            elif diff_top == 0 and diff_bot >=1:
                #print("yes")
                top_seq += diff_bot * "-"
                bot_seq += (diff_bot-1) * "-" + bottom_sequence_add[i_old]
            else:
                #print(it, diff_top)
                #print(it, diff_bot)
                print(it)
                
            i_old, j_old = idx_pair

            #print(top_seq)
            #print(bot_seq)

        n_match = 0
        n_mismatch = 0
        n_gaps = 0

        for i,j in zip(top_seq, bot_seq):
            if i==j:
                n_match +=1
            elif i!=j:
                if i == "-" or j == "-":
                    n_gaps +=1
                else:
                    n_mismatch +=1

        n_top_seqs = len(list(traceback_paths.keys()))
        if  n_top_seqs > 1 and num==0:
            print("#### WARNING ####")
            print(f"Found {n_top_seqs} with the same (top) score")
            print("")

        print("######### SCORE MATRIX #########")
        if n_top_seqs > 1:
            print(f"top_sequence number {num+1}")
        print("The alignment is highlighted with \"!\" symbols")
        draw_matrix_alignment(matrix, traceback_paths[key], key, top_sequence, bottom_sequence)
        print("")

        print("######### ALIGNMENT RESULTS #########")
        if n_top_seqs > 1:
            print(f"top_sequence number {num+1}")
        print(f"max_score: {best_score}")
        print(f"alignment_length: {len(top_seq[::-1])}")
        print(top_seq[::-1])
        print(bot_seq[::-1])
        print(f"n_match: {n_match},\nn_mismatch: {n_mismatch},\nn_gaps: {n_gaps}")
        print("")
        print("")
