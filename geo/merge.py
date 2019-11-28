# encoding: utf-8
'''
@File    :   merge.py
@Time    :   2019/11/20 20:01:16
@Author  :   aojie654
@Contact :   aojie654@live.cn
@Desc    :   Merge the GEO traffic report of Akamai
'''

'''
Notes:
1. Billing tittle in line 20 and data begin from line 24 in csv's content
'''

# Import the libs
# The following pass is using to avoid the formate issue
import csv
import time
import os
import pathlib
pass


def get_file_list_name(dir_path):
    '''
    Define the function to get the name of csv files
    '''
    # Set the current path to pathlib.Path
    path_object = pathlib.Path('.')
    # Get the object of files list
    files_object = path_object.glob("*.csv")
    # Put the files objects to list
    files_object_list = list(files_object)
    # convert the files_object_list to strings and store them to a new list
    files_name_list = []
    for file_object in files_object_list:
        file_name = file_object.name
        files_name_list.append(file_name)

    return files_name_list


def merge_csv_content(file_content_list):
    '''
    Define the function that merge the content
    '''
    return 0


def read_csv_content(filenames_list):
    '''
    Define the function that read the csv files
    '''
    return 0


def save_csv_content(*args):
    '''
    Define the function that save the content to final result file
    '''
    return 0


if __name__ == "__main__":

    # Define the name of customer
    customer_name = input('Input the name of customer:')
    # customer_name = "Shein"

    # Get the current date
    cur_date = time.strftime("%Y-%m-%d", time.gmtime())
    # Define the dir of files location
    dir_path = input("Inputs the directory which csv files was included:")
    # dir_path = '/Volumes/data/tmp/downloads/akamai_bills_geo'
    # Name of final result
    result_filename = customer_name + '-bills-' + cur_date + '.csv'

    # Change the work dir to $dir_path
    os.chdir(dir_path)

    # Get the name of files need to merge
    filenames_list = get_file_list_name(dir_path)

    # Read the file content and save them to list
    content_list = read_csv_content(filenames_list)

    # Merge the file content and save result to $merged_result
    merged_result = merge_csv_content(content_list)

    # Write the merged_result to final result file
    save_csv_content(merged_result)
