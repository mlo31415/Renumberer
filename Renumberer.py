import sys
from tkinter import filedialog
import os
import re
import datetime
import base64

dirname=filedialog.askdirectory()

# Get all the filenames of jpgs in that directory sorted alphabetically
filelist=os.listdir(dirname)
filelist=[f for f in filelist  if os.path.splitext(f)[1] == ".jpg"]
filelist.sort()

# The filenames of the form <text>p<digits>.jpg
# Create lists for each value of <text>
pattern=re.compile("^([\w\W]*)p([0-9]*)\.jpg$")

filegroups=[]
filegroupname=""
filegroup=[]
for name in filelist:
    g=pattern.match(name).groups()
    if g == None:
        print("No group found: '"+name+"'")
        continue
    if (g[0] == filegroupname):
        filegroup.append(name)
    else:
        if len(filegroup) > 0:
            filegroups.append(filegroup)
        filegroup=[]
        filegroup.append(name)
        filegroupname=g[0]

if len(filegroup) > 0:
    filegroups.append(filegroup)

# We have a list of filenames with sequential numbers
# We want to rename 1, 2, 3, 4, 5 to 1, 2, 4, 6, 8.  I.e., 1 maps to 1 and the rest map to 2(n-1)
# We need to rename from the highest to the lowest to avoid conflicts
for filegroup in filegroups:
    filegroup.sort(reverse=True)
    for filename in filegroup:
        g=pattern.match(filename).groups()
        seq=2*(int(g[1])-1)
        if seq == 0:    #1 is a special case
            seq=1
        seqstr=str(seq).rjust(2, '0')
        newname=g[0]+"p"+seqstr+".jpg"
        print(filename+ " --> " +newname)
i=0



