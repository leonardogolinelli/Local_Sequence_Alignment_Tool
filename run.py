#!/home/leonardo/miniconda3/envs/numpy_env/bin/python

from input import fetch_arguments
from fill_and_save_trace import fill_and_trace
from traceback_procedure import run_traceback
from write_alignment import write_alignment_fcn

scores, top_sequence, bottom_sequence = fetch_arguments()
matrix, traceback_dic = fill_and_trace(scores, top_sequence, bottom_sequence)
traceback_paths, best_score = run_traceback(scores, top_sequence, bottom_sequence, matrix, traceback_dic)
write_alignment_fcn(scores, top_sequence, bottom_sequence, matrix, traceback_dic, traceback_paths, best_score)