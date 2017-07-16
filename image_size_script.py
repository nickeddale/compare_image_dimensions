import urllib2
import get_image_info
import csv

#open csv file and put in a list

with open('images.csv', 'rU') as f:
  reader = csv.reader(f)
  file_list = list(reader)

for y in file_list[1:]:
    print(y[3])
    print(y[4])
    img_data = urllib2.urlopen(y[3])
    image_type_1, width_1, height_1 = get_image_info.getImageInfo(img_data)
    img_data = urllib2.urlopen(y[4])
    image_type_2, width_2, height_2 = get_image_info.getImageInfo(img_data)
    print(width_1, width_2)


