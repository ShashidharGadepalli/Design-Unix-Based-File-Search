from folder import Folder
from criteria import Criteria

class FileSearcher:

    def search(self,folder:Folder, criteria: Criteria):
        res = []

        for file in folder.get_files():
            if criteria.matches(file):
                res.append(file)
        for subfolder in folder.get_folders():
            res.extend(self.search(subfolder,criteria))

        return res

