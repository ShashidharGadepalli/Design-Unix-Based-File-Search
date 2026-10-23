from file import File
class Folder:

    def __init__(self,name):
        self._name = name
        self._files = []
        self._folders = []

    def get_name(self):
        return self._name

    def add_files(self,file:File):
        self._files.append(file)

    def add_folder(self,folder):
        self._folders.append(folder)

    def get_files(self):
        return self._files

    def get_folders(self):
        return self._folders
    
    
