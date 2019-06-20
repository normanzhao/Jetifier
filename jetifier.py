import csv
import os
import glob2
import sys

mappings = [];

with open('mappings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        mappings.append(row)
        
mappings = mappings [1:]

node_dir = "node_modules/"
extensions = ["java", "kt", "xml"]
reverse = sys.argv[1] == "-r"

for ex in extensions:
    current_count = 0
    current_total = len(glob2.glob(node_dir+'/**/*.'+ex, recursive=True))
    for file_to_change in glob2.glob(node_dir+'/**/*.'+ex, recursive=True):
        try:
            contents = open(file_to_change).read()
            for mapping in mappings:
                if !reverse:
                    contents = contents.replace(mapping[0], mapping[1])
                else:
                    contents = contents.replace(mapping[1], mapping[0])

            f = open(file_to_change, 'w')
            f.write(contents)
            f.close()
            current_count += 1
            print ("Changing file for extensions {}: {} ({}/{}) \n".format(ex, file_to_change, current_count, current_total)) 
        except: 
            pass
