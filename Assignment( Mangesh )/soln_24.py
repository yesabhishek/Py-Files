from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(C\:\\\Users\achoud3\Py Files):
    f.extend(filenames)
    break
