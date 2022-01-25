from PIL import Image
import os
import sys

directory = r"C:\Users\Benjamin Huth\PycharmProjects\SnackTime\LeagueSquares"

for file_name in os.listdir(directory):
    print("Processing %s" % file_name)
    image = Image.open(os.path.join(directory, file_name))

    x,y = image.size
    new_dimensions = (60, 60)  # dimension set here
    output = image.resize(new_dimensions, Image.ANTIALIAS)

    output_file_name = os.path.join(directory, "small_" + file_name)
    output.save(output_file_name, "PNG", quality = 95)

print("All done")