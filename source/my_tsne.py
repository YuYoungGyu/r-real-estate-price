import pandas as pd
pd.options.mode.chained_assignment = None 
import numpy as np
import re
import nltk

from gensim.models import word2vec

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

class MyTsne:
    def __init__(self, model):
        "Creates and TSNE model and plots it"
        tokens = []
        self.labels = []
        self.words = []
        self.x = []
        self.y = []
        self.words = list(model.wv.index_to_key)
        for word in self.words:
            tokens.append(model.wv[word])
            self.labels.append(word)

        tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
        new_values = tsne_model.fit_transform(tokens)

        for value in new_values:
            self.x.append(value[0])
            self.y.append(value[1])

    def draw_tsne(self, save_file_name = 0):
        plt.figure(figsize=(24, 24)) 
        for i in range(len(self.x)):
            plt.scatter(self.x[i],self.y[i])
            plt.annotate(self.labels[i],
                         xy=(self.x[i], self.y[i]),
                         xytext=(5, 2),
                         textcoords='offset points',
                         ha='right',
                         va='bottom', )
        if save_file_name != 0:
            plt.savefig(f'../article/{save_file_name}.png', dpi=300)
        plt.show()

    def draw_tsne_with_specific_point (self, points_index, save_file_name = 0):
        plt.figure(figsize=(24, 24)) 
        for i in range(len(self.x)):
            if i in points_index:
                plt.scatter(self.x[i],self.y[i], s = 100, color = 'r')
            else:
                plt.scatter(self.x[i],self.y[i], color = 'b')
            plt.annotate(self.labels[i],
                         xy=(self.x[i], self.y[i]),
                         xytext=(5, 2),
                         textcoords='offset points',
                         ha='right',
                         va='bottom', )
        if save_file_name != 0:
            plt.savefig(f'../article/{save_file_name}.png', dpi=300)
        plt.show()

    def get_word_vector(self, find_words):
        fwv_dic = {}
        for fword in find_words:
            fwi = self.words.index(fword)
            fwv_dic[fword] = (self.x[fwi], self.y[fwi])
        return fwv_dic