from extensioncriteria import Extension
from namecriteria import Name
from sizegreater import SizeGreter
from filesearcher import FileSearcher
from file import File
from folder import Folder
from notcriteria import NotCriteria
from andcriteria import AndCriteria
from orcriteria import OrCriteria


photos = Folder("Photos")
photos2 = Folder("DecVacation")
photos.add_folder(photos2)
photos2.add_files(File("Christmas.pdf",2000))
photos2.add_files(File("Newyear.png",1000))
photos2.add_files(File("Christ.txt",3000))
photos2.add_files(File("Same.txt",3500))

photos2.add_files(File("Same.jpg",4500))

searcher = FileSearcher()

namecheck = Name("pdf")

ans = searcher.search(photos,namecheck)
print([f.get_name() for f in ans])
sizecheck = SizeGreter(2000)
ans2 = searcher.search(photos,sizecheck)
print([f.get_name() for f in ans2])


extcheck = Extension(".png")
ans3 = searcher.search(photos2,extcheck)
print([f.get_name() for f in ans3])

n1 = NotCriteria(Name(".pdf"))
ans4  = searcher.search(photos,n1)
print([f.get_name() for f in ans4])

or1 = OrCriteria(Name("Sam"),Name("Chris"))
ans5  = searcher.search(photos,or1)
print([f.get_name() for f in ans5])

and1 = AndCriteria(SizeGreter(3000),Extension(".txt"))
ans6  = searcher.search(photos,and1)
print([f.get_name() for f in ans6])
