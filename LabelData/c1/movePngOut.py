# move event png files out of every subfolder into the main folder
#

import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # if the file is end with .png
        if name != "movePngOut.py" and name[-4:] == ".png":
            # check if the file has renamed already (remove ./ if it has
            newName = root[2:] + ".png"
            if name != newName:        
                os.rename(os.path.join(root, name), os.path.join(root, root + ".png"))
    # for name in dirs:
    #     os.rename(os.path.join(root, name), os.path.join(root, root))

    