import csv
import argparse
import sys


DATA_IN_FILE_PATH = 'boxing.csv'

DATA_OUT_FILE_PATH = 'boxing_out.csv'

class RecordDesc:
    def __init__(self, row):
          self.row = row

    def name(self):
        return self.row[1]
    
    def weight(self):
        return self.row[7]
    
    def age(self):
        return self.row[6]
    
    def box_class(self):
        return self.row[8]
    
    def geRow(self):
         return self.row

global_map = {}

csv_hdr_row = None

with open(DATA_IN_FILE_PATH, newline='', mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    skip_desc_flag = False
    for row in csv_reader:
        if skip_desc_flag:
            rec_desc = RecordDesc(row=row)
            if rec_desc.age() not in global_map:
                    global_map[rec_desc.age()] = dict()
            if rec_desc.weight() not in global_map[rec_desc.age()]:
                    global_map[rec_desc.age()][rec_desc.weight()] = dict()
            if rec_desc.box_class() not in global_map[rec_desc.age()][rec_desc.weight()]:
                    global_map[rec_desc.age()][rec_desc.weight()][rec_desc.box_class()] = list()
            global_map[rec_desc.age()][rec_desc.weight()][rec_desc.box_class()].append(rec_desc)
        else:
            csv_hdr_row = row
            skip_desc_flag = True

with open(DATA_OUT_FILE_PATH, mode='w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    if csv_writer:
        csv_writer.writerow(csv_hdr_row)
        for age_key, l1 in global_map.items():
            for wight_key, l2 in l1.items():
                 for cls_key, l3 in l2.items():
                    for row_desc in l3:
                        csv_writer.writerow(row_desc.geRow())
                    csv_writer.writerow([]) # separator
        print('Completed')
