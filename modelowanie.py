from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = [".", "./atom_files"]

a = AutoModel(env, alnfile="dopasowanie.txt", knowns=("6F14", "3J4Q", "1CTP"), sequence="model",)
a.make()
a.write("wygenerowanaStruktura.pdb")
