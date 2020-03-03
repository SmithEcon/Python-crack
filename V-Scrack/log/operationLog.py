﻿# -*- encoding: utf-8 -*-
'''

@author: SmthEcon
'''
import datetime


class operationLog(object):
    '''
    classdocs
    '''
    global filename
    filename = '../exp/operation.log'

    def __init__(self):
        pass

    @staticmethod
    def write(message):
        now = str(datetime.datetime.now())
        with open(filename, 'a') as file:
            file.write(now.split('.')[0] + ' ' + message + '\n')

    @staticmethod
    def write2file(message, dst_filename):
        now = str(datetime.datetime.now())
        with open(dst_filename, 'a') as file:
            file.write(now.split('.')[0] + ' ' + message + '\n')


if __name__ == '__main__':
    log = operationLog()
    log.write('test')
