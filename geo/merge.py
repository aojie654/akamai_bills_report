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
1. tittle_line=20
2. data_line=[24:-2]
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
    # # Set the current path to pathlib.Path
    # path_object = pathlib.Path('.')
    # # Get the object of files list
    # files_object = path_object.glob("*.csv")
    # # Put the files objects to list
    # files_object_list = list(files_object)
    # # convert the files_object_list to strings and store them to a new list
    # files_name_list = []
    # for file_object in files_object_list:
    #     file_name = file_object.name
    #     files_name_list.append(file_name)

    # Init csv file list
    files_name_list = []
    
    # list all files
    for i in os.listdir():
        # Append the filename to file_name_list if end with .csv
        if i[-4:] == '.csv':
            files_name_list.append(i)

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


def pure_csv_content(inputs_source_file):
    '''
    Delete the extra message in single csv
    '''

    # Create pure folder if not exists
    pure_folder = '../pure/'
    if os.path.exists(pure_folder) == False:
        os.mkdir(pure_folder)
    
    # Define the outputs pure name 
    outputs_pure_file = pure_folder+inputs_source_file

    # Open the source file and read
    with open(inputs_source_file, mode='r', encoding='utf-8') as file_object:
        file_content = file_object.read()
    file_content_list = file_content.split('\n')

    # Init the reasult content
    result_content_string = ""

    # Get the length of file ceontent lines count
    list_length = len(file_content_list)

    # Determind which line to output
    # In this case, the title line is 20(index19), data lines begin with 24 to ops 3(index 23:list_length-2)
    outputs_index_range = [20-1] + list(range(24-1, list_length-2))
    for i in outputs_index_range:
        # Get the current lines content
        cur_line = file_content_list[i]
        # Find the first ',' and strip to delete the $geoid row
        pos_cur_line = cur_line.find(',')
        cur_line = cur_line[pos_cur_line+1:]
        # Append current line to result and append a '\n' if it was not the last line
        if i != outputs_index_range[-1]:
            result_content_string = result_content_string+cur_line+'\n'
        else:
            result_content_string = result_content_string+cur_line

    # Open the outputs file and save the result
    with open(outputs_pure_file, mode='w+', encoding='utf-8') as file_object:
        file_object.write(result_content_string)


def pure_csv_list(source_csv_list):
    '''
    Pure the csv file list via loop
    '''
    for csv_file in source_csv_list:
        pure_csv_content(csv_file)


if __name__ == "__main__":

    # Define the name of customer
    # customer_name = input('Input the name of customer:')
    customer_name = "Shein"

    # Get the current date
    cur_date = time.strftime("%Y-%m-%d", time.gmtime())

    # Define the dir of files location
    # dir_path = input("Inputs the directory which csv files was included:")
    dir_path = '/Volumes/data/tmp/downloads/akamai_bills_geo/source'

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
