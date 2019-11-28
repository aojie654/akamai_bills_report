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

# Get the current date
cur_date = time.strftime("%Y-%m-%d", time.gmtime())

# Define the dir of files location
dir_path = '/Volumes/data/tmp/downloads/akamai_bills_geo'
# Define the name of customer
customer_name = input('Input the name of customer:')

# Name of files need to merge
files_list = get_file_list_name(dir_path)
# Name of final result
result_path = customer_name + '-bills-' + cur_date + '.csv'

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

def merge_csv_content(*args):
    '''
    Define the function that merge the content
    '''
    return 0


def read_csv_content(csv_file):
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
    # Change the work dir to $dir_path
    os.chdir(dir_path)
    # Merge the csv content
    merged_result = merge_csv_content(files_list)
    save_csv_content(merged_result)
