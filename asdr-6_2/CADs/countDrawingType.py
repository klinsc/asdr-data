# count the drawing type of pdf files in a folder
# the drawing type is behind the last dash in the pdf file name
# for example: klb-Kalasin2-m-h.pdf, the drawing type is h, cmf-ChiangMai6-m-dbsb.pdf, the drawing type is dbsb

import os
import sys
import re


def countDrawingType(path):
    drawing_type = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                # get characters after the last dash
                type = re.search(r'(?<=-)[a-zA-Z]+(?=\.pdf)', file)
                print(type)

                drawing_type[type.group()] = drawing_type.get(
                    type.group(), 0) + 1

    return drawing_type


def main():
    if len(sys.argv) < 2:
        print("Usage: python countDrawingType.py [path]")
        sys.exit(1)
    path = sys.argv[1]
    drawing_type = countDrawingType(path)
    for key, value in drawing_type.items():
        print(key, value)

    # print total
    print("Total: ", sum(drawing_type.values()))

    # save as csv file
    with open('drawing_type.csv', 'w') as f:

        # write header
        f.write("drawing_type,count\n")

        for key, value in drawing_type.items():
            f.write("%s,%s\n" % (key, value))

        # write total
        f.write("Total,%s\n" % sum(drawing_type.values()))

if __name__ == '__main__':
    main()
