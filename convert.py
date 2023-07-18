from pdf2image import convert_from_path
import matplotlib.pyplot as plt

# for every subfolder in c1, convert pdf to png and save in the same folder

# query sub folders
import os
rootdir = './rpod5/c1'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".pdf"):
            print(filepath)
            filename = os.path.splitext(file)[0]
            print(filename)
            page = 0
            PDF_PATH = filepath
            convert_from_path(PDF_PATH, dpi=300, single_file=True, first_page=page, last_page=page+1, output_folder=rootdir+'/'+filename,
                              output_file=filename, fmt="jpg", poppler_path=r'C:\poppler-23.01.0\Library\bin')
            # plt.imshow(img)
            # plt.show()

# page = 0
# PDF_PATH = './LabelData/c1/bib-BangPaIn2-sm-dbds-1/bib-BangPaIn2-sm-dbds-1.pdf'
# convert_from_path(PDF_PATH, dpi=300, first_page=page, last_page=page+1, output_folder="./",
#                             output_file=filename, fmt="png", poppler_path=r'C:\poppler-23.01.0\Library\bin')
