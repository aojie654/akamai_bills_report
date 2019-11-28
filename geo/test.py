# encoding=utf8

import csv
import math


def file_read():
    inputs_file = '/Volumes/data/tmp/downloads/akamai_bills_geo/DSA_edge_bytes_by_country_area_1574238733.csv'
    outputs_file = '/Volumes/data/tmp/downloads/akamai_bills_geo/final_result.csv'

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


def read_csv_test(filenames_list):
    list_out = []
    for single_file in filenames_list:
        with open(single_file, newline='') as file_object:
            read_content_file_object = csv.reader(file_object)
            list_in = []
            for line in read_content_file_object:
                list_in.append(line)
            # print(list_in)
            list_out.append(list_in)
    for i in list_out:
        print(i)


def csv_to_list(filename):
    with open(filename, mode='r', encoding='utf-8') as file_object:
        file_read_content = file_object.read().split('\n')
    return file_read_content


def merge_to_geo_list(list_name, geo_codes_list):
    for list_line in list_name:
        key = list_line[0]
        value = list_line[1]
        geo_codes_list[key] = geo_codes_list[key] + [value]


def write_csv_test(file_csv_location):

    with open(file_csv_location, 'w', newline='') as csvfile:

        headers = ['Country Code', 'Country',
                   'DSA', 'DSD', 'Total', 'Total(MB)']

        values = [['CN', '中国', 694126208216690, 372656480774180], [
            'IN', '印度', 554993248641136, 109102983359088], ['FR', '法国', 251343040131381, 51101730512926]]

        for i in range(len(values)):
            total = values[i][2] + values[i][3]
            total_mb = math.ceil(total/1000/1000)
            list_extra = [total, total_mb]
            value_extrad = values[i] + list_extra
            values[i] = value_extrad

        writer = csv.DictWriter(csvfile, fieldnames=headers)

        writer.writeheader()
        for i in values:
            writer.writerow({headers[0]: i[0], headers[1]: i[1], headers[2]: i[2], headers[3]: i[3], headers[4]: i[4], headers[5]: i[5]})


if __name__ == "__main__":

    '''
    CSV Read Test
    '''
    # filenames_list = [
    #     '/Volumes/data/tmp/downloads/akamai_bills_geo/pure/DSA_edge_bytes_by_country_area_1574238733.csv', '/Volumes/data/tmp/downloads/akamai_bills_geo/pure/DSD_edge_bytes_by_country_area_1574237865.csv']
    # read_csv_test(filenames_list)

    '''
    CSV Write Test
    '''
    write_csv_test(
        '/Volumes/data/tmp/downloads/akamai_bills_geo/csv_write_test.csv')
