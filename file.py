import os
class File:

    def __init__(self,filename,filesize):

        self._filename = filename
        self._filesize = filesize
        self._extension = os.path.splitext(filename)[1]

    def get_name(self):
        return self._filename

    def get_filesize(self):
        return self._filesize

    def get_extension(self):
        return self._extension