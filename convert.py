# a script to convert pdf to png
# Path: convert.py .
from pdf2image import convert_from_path
import matplotlib.pyplot as plt

# for every subfolder in path argument, convert pdf to png and save in the same folder

# query sub folders
import os
import sys
from tqdm import tqdm
rootdir = sys.argv[1]


def convert_pdf_to_png(filepath, dirs, subdir):
    if filepath.endswith(".pdf"):
        # convert pdf to png
        pages = convert_from_path(filepath, dpi=300, single_file=True, first_page=0, last_page=1,
                                  fmt="png", poppler_path=r'C:\poppler-23.01.0\Library\bin')

        # save png to same folder of pdf
        pages[0].save(filepath.replace(".pdf", ".png"), "PNG")

        # # show png
        # plt.imshow(pages[0])
        # plt.show()


def main():
    # check argument is passed
    if len(sys.argv) < 2:
        print("Please provide path to folder")
        return

    # check path is valid
    if not os.path.isdir(rootdir):
        print("Path is not valid")
        return

    # for i in tqdm(range(0, 100), desc="Loading..."):
    # for subdir, dirs, files in os.walk(rootdir):
    for i, (subdir, dirs, files) in tqdm(enumerate(os.walk(rootdir)), desc="Loading…", ascii=False, ncols=75):
        print(subdir, dirs, files)
        for file in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            convert_pdf_to_png(filepath, dirs, subdir)


if __name__ == "__main__":
    main()
