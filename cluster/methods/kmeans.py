# -*- encoding:utf-8 -*-


import os
import math
import random
import copy

from pprint import pprint

from cluster.settings import BASE_DIR
from . import Cluster, NDimensionalObject




class Kmeans(Cluster):
    THRESHOLD = 0.005

    def __init__(self, *args, **kwargs):
        self.k = int(kwargs.pop('clusters', 0))
        self.dataset = kwargs.pop('dataset', None)
        super(Kmeans, self).__init__(*args, **kwargs)
        self.clusters = {cluster: dict() for cluster in range(1, self.k + 1)}
        self.objects = []
        self.clusters_buffer = None

    def __call__(self):
        pass

    def create_centers(self):
        for index in self.clusters:
            self.clusters[index]['center'] = self.objects[int(random.uniform(0, self.objects.__len__()))].values
            self.clusters[index]['last'] = [0] * self.objects[0].values.__len__()
            self.clusters[index]['set'] = []
            self.clusters[index]['delta'] = 0
            print self.clusters[index]
        #exit()

    def load(self):
        if self.dataset:
            self.objects = [NDimensionalObject(element.get('user'), element.get('vector')) for element in self.dataset]
            return

        filename = os.path.join(BASE_DIR, self.filename)
        with open(filename) as dataset:
            for line in dataset:
                row = line.split()
                self.objects.append(NDimensionalObject(row[0], [float(index) for index in row[1:]]))

      
    @staticmethod
    def ecuclidean_distance(actual, last):
        return sum([pow(actual[index] - last[index] , 2) for index in range(0, actual.__len__())])
        #return pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)

    def check(self):
        sum_delta = 0
        for index in self.clusters:
            delta = math.sqrt(
                self.ecuclidean_distance(
                    self.clusters[index]['center'],
                    self.clusters[index]['last']))
            self.clusters[index]['delta'] = delta
            sum_delta += delta
        
        if sum_delta < self.THRESHOLD * self.clusters.__len__():
            return False
        return True

    def set_clusters(self):
        for element in self.objects:
            minimum = None
            index = None
            for cluster, values in self.clusters.iteritems():
                actual = self.ecuclidean_distance(element.values, values['center'])
                if minimum == None or minimum >= actual:
                    minimum = actual
                    index = cluster
            self.clusters[index]['set'].append(element)

    def set_centers(self):
        self.clusters_buffer = copy.deepcopy(self.clusters)
        for index in self.clusters:
            self.clusters[index]['last'] = self.clusters[index]['center']
            if self.clusters[index]['set'].__len__() != 0:
                self.clusters[index]['center'] = [
                    sum(map(lambda element: element.values[i], self.clusters[index]['set'])) / self.clusters[index]['set'].__len__() for i in range(0, self.objects[0].values.__len__())
                ]
            self.clusters[index]['set'] = []

    def run(self):
        self.load()
        self.create_centers()

        while self.check():
            self.set_clusters()
            pprint(self.clusters)
            self.set_centers()
        pprint(self.clusters)
        pprint(self.clusters_buffer)
        return self.clusters_buffer

            