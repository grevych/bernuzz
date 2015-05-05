# -*- encoding:utf-8 -*-

import abc



class Cluster(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename='data.in'):
        self.filename = filename
        self.objects = []

    def __call__(self):
        pass

    @abc.abstractmethod
    def run(self):
        #raise NotImplementedError("Please Implement this method")
        pass


class BasicObject(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        pass

    def __str__(self):
        return '%f, %f' % (self.x, self.y, )

    def __repr__(self):
        return '<%f, %f>' % (self.x, self.y, )


class NDimensionalObject(object):
    
    def __init__(self, identifier, values):
        self.id = identifier
        self.values = values

    def __str__(self):
        return '%s, %s' % (self.id, self.values, )

    def __repr__(self):
        return '%s:, %s' % (self.id, self.values, )
