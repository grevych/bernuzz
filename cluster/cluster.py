# -*- encoding:utf-8 -*-

import sys

from methods.kmeans import Kmeans





if __name__ == '__main__':
    filename = 'data.in'    
    clusters = 20
    cluster = Kmeans(clusters=clusters, filename=filename)
    cluster.run()
