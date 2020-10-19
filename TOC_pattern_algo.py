import cv2
import numpy as np
import random
from PIL import Image
from os import listdir
from os.path import isfile, join

MY_PATH = "resources/"
FILE_LIST = [f for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))]
IMG_SIZE = .1

def __main__():
    # CHOOSE FROM THESE
    # seq_patterns = [
    #     "abbbba",
    #     "ab",
    #     "abcbcbcba",
    #     "abababa",
    #     "abcbdeca",
    #     "abcbcbcbcbcba",
    #     "abcbcbca",
    #     "abcbcba",
    #     "abba",
    #     "abcbcba"
    # ]
    # CHOOSE PATTERN FROM LIST ABOVE
    for i in range(6):
        input_pattern = "abcbcba"
        chosen_shapes = choose_shapes(FILE_LIST, input_pattern)
        stacked_pattern = get_pattern_sequence(chosen_shapes, input_pattern)
        print(stacked_pattern)
        img = draw_stacked_patterns("FILIPINO TEXTILE PATTERN || Pattern of " + input_pattern, stacked_pattern)
        # TODO dir Image.open()
        img.save("{}_{}.jpeg".format(input_pattern, i))




def choose_shapes(sel_shape, pattern_type):
    # choosing the shapes to use
    shape_num = len(set(pattern_type))
    shapes = []
    shape_chosen = random.sample(sel_shape, shape_num) # select random shapes
    for shape in shape_chosen:# read
        shapes.append(cv2.imread('resources/{}'.format(shape), 1))
    shapes = resize_shape(shapes)
    return shapes

def resize_shape(shapes):
    # resizing shapes
    for i in range(len(shapes)):
        shapes[i] = cv2.resize(shapes[i], (0,0), None, IMG_SIZE, IMG_SIZE)
    return shapes

def get_pattern_sequence(use_shape, sequence):
    object_shape = []
    for i in use_shape:
        object_shape.append(i)
    pattern_sequence = []
    pattern_sequence = set_pattern_sequence(sequence, object_shape, pattern_sequence)

    return pattern_sequence

def set_pattern_sequence(seq, obj_shp, pat_seq):
    pattern_num = len(seq)
    for i in range(len(seq)):
        if seq == "abbbba":
            pat_seq = pattern_abbbba(pat_seq, obj_shp, i)
        elif seq == "ab":
            pat_seq = [obj_shp[0], obj_shp[1]]
        elif seq == "abcbcbcba":
            pat_seq = pattern_abcbcbcba(pat_seq, obj_shp, i)
        elif seq == "abababa":
            pat_seq = pattern_abababa(pat_seq, obj_shp, i)
        elif seq == "abcbdeca":
            pat_seq = pattern_abcbdeca(pat_seq, obj_shp, i)
        elif seq == "abcbcbcbcbcba":
            pat_seq = pattern_abcbcbcbcbcba(pat_seq, obj_shp, i)
        elif seq == "abcbcbca":
            pat_seq = pattern_abcbcbca(pat_seq, obj_shp, i)
        elif seq == "abcbcba":
            pat_seq = pattern_abcbcba(pat_seq, obj_shp, i)
        elif seq == "abba":
            pat_seq = pattern_abba(pat_seq, obj_shp, i)

    return  pat_seq

# test this out
def seq_alt_inner(arr_state, n, m, shape):
    arr_state.append(shape[0])
    for i in range(n):
        arr_state.append(shape[1])
        arr_state.append(shape[2])
    if m == 1:
        arr_state.append(shape[1])
    arr_state.append(shape[0])

def seq_recur_inner(arr_state, n, shape):
    arr_state.append(shape[0])
    for i in range(n):
        arr_state.append(shape[1])
    arr_state.append(shape[0])

def seq_alternating(arr_state, n, shape):
    for i in range(n):
        if n % 2 == 0:
            arr_state.append(shape[0])
        else:
            arr_state.append(shape[1])

def seq_unorganized(arr_state, n, shape):
    arr_state.append(shape[0])
    for i in range(n):
        if n == 0 or n == 3:
            arr_state.append(shape[1])
        elif n == 2 or n == 6:
            arr_state.append(shape[2])
        elif n == 4:
            arr_state.append(shape[3])
        else:
            arr_state.append(shape[4])
    arr_state.append(shape[0])

def pattern_abbbba(pat_seq, obj_shp, i):
    if i not in (0,5):
        pat_seq.append(obj_shp[1])
    else:
        pat_seq.append(obj_shp[0])
    return pat_seq

def pattern_abcbcbcba(pat_seq, obj_shp, i):
    if i in range(1, 8):
        if i % 2 != 0:  # get odd numbers
            pat_seq.append(obj_shp[1])
        else:
            pat_seq.append(obj_shp[2])
    else:
        pat_seq.append(obj_shp[0])
    return pat_seq

def pattern_abababa(pat_seq, obj_shp, i):
    if i % 2 != 0:  # odd numbers
        pat_seq.append(obj_shp[0])
    else:
        pat_seq.append(obj_shp[1])
    return pat_seq

def pattern_abcbdeca(pat_seq, obj_shp, i):
    if i in (0, 7):
        pat_seq.append(obj_shp[0])
    elif i in (1, 3):
        pat_seq.append(obj_shp[1])
    elif i in (2, 6):
        pat_seq.append(obj_shp[2])
    elif i == 4 : pat_seq.append(obj_shp[3])
    else: pat_seq.append(obj_shp[4])
    return pat_seq

def pattern_abcbcbcbcbcba(pat_seq, obj_shp, i):
    if i == 0 : pat_seq.append(obj_shp[0])
    else:
        if i % 2 != 0:  pat_seq.append(obj_shp[1])
        else:  pat_seq.append(obj_shp[2])
    if i == 12: pat_seq.append(obj_shp[0])
    return pat_seq

def pattern_abcbcbca(pat_seq, obj_shp, i):
    if i == 0 : pat_seq.append(obj_shp[0])
    else:
        if i % 2 != 0:  pat_seq.append(obj_shp[1])
        else:  pat_seq.append(obj_shp[2])
    if i == 7 : pat_seq.append(obj_shp[0])
    return pat_seq

def pattern_abcbcba(pat_seq, obj_shp, i):
    if i == 0 : pat_seq.append(obj_shp[0])
    else:
        if i % 2 != 0:  pat_seq.append(obj_shp[1])
        else:  pat_seq.append(obj_shp[2])
    if i == 6: pat_seq.append(obj_shp[0])
    return pat_seq

def pattern_abba(pat_seq, obj_shp, i):
    if i not in (0,3):
        pat_seq.append(obj_shp[1])
    else:
        pat_seq.append(obj_shp[0])
    return pat_seq

def draw_stacked_patterns(pattern_name, stacked_pattern):
    pattern_sequence = np.hstack(stacked_pattern)
    # drawing the pattern
    cv2.imshow(pattern_name, pattern_sequence)
    # TODO export image
    #fpath = 'D:\SCHOOL\Theory_of_computation\research paper\resources\Figures\exported_new_pattern'
    #cv2.imwrite('export_test', pattern_sequence)
    im = Image.fromarray(pattern_sequence)
    #return im
    cv2.waitKey()


__main__()






