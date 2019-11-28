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


# get the date
import csv
import time
import os
cur_date = time.strftime("%Y-%m-%d", time.gmtime())

# define the path of files location
csv_path = '/Volumes/data/tmp/downloads/akamai_bills_geo'
# define the name of customer
customer_name = input('Input the name of customer:')

# name of files need to merge
files_list = ['DSA.csv', 'DSD.csv']
# name of final result
result_path = customer_name + 'bills'


def merge_csv_content(*args):
    '''
    define the function that merge the content
    '''
    return 0


def read_csv_content(csv_file):
    '''
    define the function that read the csv files
    '''
    return 0


def save_csv_content(*args):
    '''
    define the function that save the content to final result file
    '''
    return 0


if __name__ == "__main__":
    # change the work dir to $csv_path
    os.chdir(csv_path)
    # merge the csv content
    merged_result = merge_csv_content(files_list)
    save_csv_content(merged_result)
