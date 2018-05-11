import os
import glob
import time


def test1(size):
    """some text
more text
    """
    size = size+1
    return size


print(test1.__doc__)
print(__name__)


pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
(dirname, filename) = os.path.split(pathname)
print(dirname)
print(filename)

(shortname, extension) = os.path.splitext(filename)
print(shortname)
print(extension)


desktop = "C:/Users/ia.kudryashov/Desktop/"
print(glob.glob(desktop+'*66.xlsx'))

metadata = os.stat(desktop+'Rosgeo_FAS8200_85966.xlsx')
print(metadata.st_mtime)
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)

os.chdir('C:\\Users\\ia.kudryashov\\Desktop\\python')
import sys
sys.path.insert(0,'C:\\Users\\ia.kudryashov\\Desktop\\python')
import humansize
print(humansize.approximate_size(metadata.st_size))

print(os.path.realpath('humansize.py'))

os.chdir('C:\\Users\\ia.kudryashov\\Desktop')
print(glob.glob('*.xlsx'))
print([os.path.realpath(f) for f in glob.glob('*.xlsx')])
