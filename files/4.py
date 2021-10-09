import os, sys

fname = input("Enter your file name : ")
if os.path.isfile(fname):
    f = open(fname, "r+")
    print("file exist")

else:

    print("file doesnot exist")
    sys.exit()
lc = 0
wc = 0
cc = 0
for line in f:
    lc += 1
    words = line.split()

    wc += len(words)
    cc += len(line)
print(cc, wc, lc)
