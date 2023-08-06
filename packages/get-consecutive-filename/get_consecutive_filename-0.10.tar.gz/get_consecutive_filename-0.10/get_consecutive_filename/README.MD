# Next consecutive filename in folder 


```python
# Tested with:
# Python 3.9.13
# Windows 10

$pip install get-consecutive-filename

from get_consecutive_filename import get_free_filename
# What is it for?
# You have a folder "F:\testfiles" with 2 files "00000.txt", "00001.txt"
# and you want to get the next consecutive filename.

fname = get_free_filename(folder="f:\\testfiles", fileextension=".txt", leadingzeros=5)
print(fname)
# f:\testfiles\00002.txt
	
```




