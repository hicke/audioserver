#!/usr/bin/python


class DumpList(object):
    """docstring for DumpList"""
    def __init__(self, stop):
        self.stop = stop
    def Looper(self):
        return self.stop

DumpList(2).Looper()
# class FileLooper()
#     def main(self):
#         text_file = open("Output.txt", "w")
#         for i in range(1, 32):
#             print "Dag: " + str(i) + '\n'
#     text_file.close()
