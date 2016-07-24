import tkinter
from tkinter import filedialog
import os
import re

# Get the directory containing the jpgs to be renumbered.  (All jpgs which fit the pattern will be renumbered.)
root = tkinter.Tk()
root.withdraw()
dirname=filedialog.askdirectory()

# Get a list of all the filenames of the jpgs in that directory, sorted alphabetically
os.chdir(dirname)
filelist=os.listdir(".")
filelist=[f for f in filelist  if os.path.splitext(f)[1] == ".jpg"]
filelist.sort(reverse=True)

# The filenames we care about are of the form <text>p<digits>.jpg
# They always start numbered sequentially starting with 1.
# The pages are always a single page, N double pages, and a final single page.  We want all double page spreads to be labelled with their left-hand page's number.
# So we want to rename 1, 2, 3, 4, 5 to 1, 2, 4, 6, 8.  I.e., 1 maps to 1 and the rest map to 2(n-1)
# We need to rename from the highest to the lowest to avoid conflicts
pattern=re.compile("^([\w\W]*)p([0-9]*)\.jpg$") # Regex pattern to match page names we want to renumber

for name in filelist:
    g=pattern.match(name).groups()
    if g == None:
        print("Jpeg with non-standard name. Ignored: '"+name+"'")
        continue
    if int(g[1]) == 0:  # 1 is a special case which we can skip since it's already right
        continue
    seq=2*(int(g[1])-1)
    seqstr=str(seq).rjust(2, '0')
    newname=g[0]+"p"+seqstr+".jpg"
    print(name+ " --> " +newname)
    os.rename(name, newname)

