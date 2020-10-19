
# todo
# gui
# procedural
# get from folder
# general algo for each type
# pyinstaller for executable script if using tkinter for gui

import cv2
import numpy as np
import random
from PIL import Image
from os import listdir
from os.path import isfile, join

# TODO
# class to for algorithms
# class to draw patterns
# class for ui
# class for shapes


class DefinedAlgorithms:
    # IDENTIFIED ALGORITHMS FROM THE DATA AS OBSERVED FROM THE STUDY
    # ALGORITHM BASED FROM THE RESULTS OF FINITE STATE MACHINE <<DO NOT OPTIMIZE OR CHANGE>>
    seq_container = []
    # n = number of recurrence ,  m = number of inner end shape, just 1 or 0
    def __int__(self, shapes, n, m):
        self.shapes = shapes
        self.num_iter = n
        self.has_extra = m # boolean

    def alternating_inner(self):
        self.seq_container.append(self.shapes[0])
        for i in range(self.num_iter):
            self.seq_container.append(self.shapes[1])
            self.seq_container.append(self.shapes[2])
        if self.has_extra:
            self.seq_container.append(self.shapes[1])
        self.seq_container.append(self.shapes[0])
        return self.seq_container

    def recurring_inner(self):
        self.seq_container.append(self.shapes[0])
        for i in range(self.num_iter):
            self.seq_container.append(self.shapes[1])
        self.seq_container.append(self.shapes[0])
        return self.seq_container

    def alternating(self):
        for i in range(self.num_iter):
            self.seq_container.append(self.shapes[0])
            self.seq_container.append(self.shapes[1])
        if self.has_extra:
            self.seq_container.append(self.shapes[0])
        return self.seq_container

    def unorganized(self):
        self.seq_container.append(self.shapes[0])
        self.seq_container.append(self.shapes[1])
        self.seq_container.append(self.shapes[2])
        self.seq_container.append(self.shapes[1])
        self.seq_container.append(self.shapes[3])
        self.seq_container.append(self.shapes[4])
        self.seq_container.append(self.shapes[2])
        self.seq_container.append(self.shapes[0])
        return self.seq_container


class ImageProcessing:
    def __init__(self):
        self.RES_DIR = 'resources/'
        self.dir_name = self.RES_DIR
        self.loaded_shapes = []

    def load_shape(self):
        dir_ls_shape = [f for f in listdir(self.dir_name) if isfile(join(self.dir_name, f))] #list of all shapes in the directory
        for raw_shape in dir_ls_shape:
            self.loaded_shapes.append(cv2.imread('{}{}'.format(self.RES_DIR, raw_shape), 1))

        return self.loaded_shapes

class ShapeSetting:
    # to set the shape
    def __init__(self, shape, scale):
        self.shape = shape
        self.scale = scale

    def set_shapes(self):
        shapes = self.scale_shape(self.scale)
        return shapes

    def scale_shape(self, scale):
        self.scale = scale
        return cv2.resize(self.shape, (0, 0), None, self.scale, self.scale)

    # TODO image set
    # TODO image import


class SequenceSettings:
    def __init__(self, n_value, m_value, seq_choice):
        self.n_value = n_value
        self.m_value = m_value
        self.seq_choice = seq_choice
        self.img_seeds = ImageProcessing()

    def set_sequence(self, shape_set):

        seq_algo = DefinedAlgorithms()
        seq_algo.shapes = shape_set
        seq_algo.num_iter = self.n_value
        seq_algo.has_extra = self.m_value

        if self.seq_choice == 'alt_in':
            val = seq_algo.alternating_inner()
        elif self.seq_choice == 'recur_in':
            val = seq_algo.recurring_inner()
        elif self.seq_choice == 'alt':
            val = seq_algo.alternating()
        elif self.seq_choice == 'unorg':
            val = seq_algo.unorganized()
        else:
            val = 'UNDEFINED'

        print(val[0])
        print('-----------------------')
        return val
        # TODO SHAPE SEQ SETTING FINISHED


    def set_shape(self, scale):
        # TODO manually select shapes rather than randomize

        shape_seed = self.img_seeds.load_shape()
        sel_shape = random.sample(shape_seed, len(shape_seed))
        print(sel_shape[0])
        print("------------------------")
        shape_set, r_shape = [], []

        for i in range(len(sel_shape)):
            # shape_set[i] = ShapeSetting(sel_shape[i], scale).scale_shape(scale)
            # r_shape[i] = shape_set[i].scale_shape(scale)
            shape_set.append(ShapeSetting(sel_shape[i], scale)) #initial scale set
            r_shape.append(shape_set[i].scale_shape(scale)) #editable scale
        print('NEW')
        return shape_set
        # return r_shape

class DrawSpace:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def set_draw_space(self):
        return np.zeros([self.row, self.col], dtype=object)

    def populate_draw_space(self, seq_ls):
        # # seq = np.hstack(seq_ls)
        # d_space = self.set_draw_space()
        # print(d_space)
        # for i in range(self.row):
        #     print("HI")
        #     for j in range(self.col):
        #         d_space[i][j] = seq_ls[0][j]
        #
        # return d_space

        # board = [[0 for x in range(self.col)] for y in range(self.row)]
        # for i in range(self.row):
        #     for j in range(self.col):
        #         board[i][j] = np.hstack(seq_ls[0][j])
        # return board
        # # board = np.arange(len(seq_ls)).reshape((len(seq_ls)/6),6)


        # TODO plot the sequences correctly using arrays
        board = np.zeros([self.row, self.col], dtype=object)
        print('------------------------------')
        for i in range(self.row):
            for j in range(self.col):
                board[i][j] = seq_ls[j]
        return board
        # TODO solve why array cant be showed

    def draw_patterns(self, seq_name, seq_ls):
        # TODO solve why array cant be showed
        # stacked_sequence = np.hstack(seq_ls)
        # seq_ls = np.asarray(seq_ls, dtype=np.float32)
        cv2.imshow('hio', seq_ls)
        cv2.waitKey(0)
        #return Image.fromarray(stacked_sequence)

    # TODO export image



def __main__():
    # inputs
    scale_val = .05
    algo_choice = ['alt_in','recur_in','alt','unorg']

    # set draw space
    draw_space = DrawSpace(row=2, col=6)

    # pattern setting
    seq = SequenceSettings(n_value=2, m_value=1, seq_choice=algo_choice[0])
    shp_scale = seq.set_shape(scale_val)
    seq = seq.set_sequence(shp_scale)

    # drawing
    seq_lay = draw_space.populate_draw_space(seq)
    # print(seq_lay)
    print ('Hello')
    draw_space.draw_patterns(algo_choice[0], seq_lay)



__main__()























