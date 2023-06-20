# for every subfolder in c1, get name of each png file and save in a txt file

# query sub folders
import os
rootdir = './rpod3/c2'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".png"):
            print(filepath)
            filename = os.path.splitext(file)[0]
            print(filename)
            with open('c2.txt', 'a') as f:
                f.write("/"+filename+".png"+'\n')