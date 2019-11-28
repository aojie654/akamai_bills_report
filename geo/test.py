# encoding=utf8

import csv

inputs_file='/Volumes/data/tmp/downloads/akamai_bills_geo/DSA_edge_bytes_by_country_area_1574238733.csv'
outputs_file='/Volumes/data/tmp/downloads/akamai_bills_geo/final_result.csv'

with open(inputs_file, mode='r', encoding='utf-8') as file_object:
    file_content = file_object.read()
file_content_list = file_content.split('\n')
result_content_list = ""

list_length = len(file_content_list)
outputs_index_range = [20-1] + list(range(24-1, list_length-2))
for i in outputs_index_range:
    cur_line = file_content_list[i]
    pos_cur_line = cur_line.find(',')
    cur_line = cur_line[pos_cur_line+1:]
    # print(cur_line)
    if i != outputs_index_range[-1]:
        result_content_list = result_content_list+cur_line+'\n'
    else:
        result_content_list = result_content_list+cur_line
# print(result_content_list)

with open(outputs_file, mode='w+', encoding='utf-8') as file_object:
    file_object.write(result_content_list)
