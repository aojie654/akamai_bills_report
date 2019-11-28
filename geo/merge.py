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

# import pathlib
import csv
import time
import os
import math
pass


def init_geo_codes():
    '''
    Initialize geo codes
    '''
    geo_codes_list = {'AD': ['安道尔共和国'], 'AE': ['阿拉伯联合酋长国'], 'AF': ['阿富汗'], 'AG': ['安提瓜和巴布达'], 'AI': ['安圭拉岛'], 'AL': ['阿尔巴尼亚'], 'AM': ['亚美尼亚'], 'AN': ['荷属安的列斯'], 'AO': ['安哥拉'], 'AQ': ['南极洲'], 'AR': ['阿根廷'], 'AS': ['美属萨摩亚'], 'AT': ['奥地利'], 'AU': ['澳大利亚'], 'AW': ['阿鲁巴'], 'AZ': ['阿塞拜疆'], 'BA': ['波黑'], 'BB': ['巴巴多斯'], 'BD': ['孟加拉国'], 'BE': ['比利时'], 'BF': ['布基纳法索'], 'BG': ['保加利亚'], 'BH': ['巴林'], 'BI': ['布隆迪'], 'BJ': ['贝宁'], 'BM': ['百慕大'], 'BN': ['文莱'], 'BO': ['玻利维亚'], 'BR': ['巴西'], 'BS': ['巴哈马'], 'BT': ['不丹'], 'BW': ['博茨瓦纳'], 'BY': ['白俄罗斯'], 'BZ': ['伯利兹'], 'CA': ['加拿大'], 'CC': ['科科斯（基林）群岛'], 'CD': ['刚果（金）'], 'CF': ['中非'], 'CG': ['刚果（布）'], 'CH': ['瑞士'], 'CI': ['科特迪瓦'], 'CK': ['库克群岛'], 'CL': ['智利'], 'CM': ['喀麦隆'], 'CN': ['中国'], 'CO': ['哥伦比亚'], 'CR': ['哥斯达黎加'], 'CU': ['古巴'], 'CV': ['佛得角'], 'CX': ['圣诞岛'], 'CY': ['塞浦路斯'], 'CZ': ['捷克'], 'DE': ['德国'], 'DJ': ['吉布提'], 'DK': ['丹麦'], 'DM': ['多米尼克'], 'DO': ['多米尼加'], 'DZ': ['阿尔及利亚'], 'EC': ['厄瓜多尔'], 'EE': ['爱沙尼亚'], 'EG': ['埃及'], 'ER': ['厄立特里亚'], 'ES': ['西班牙'], 'ET': ['埃塞俄比亚'], 'EU': [''], 'FI': ['芬兰'], 'FJ': ['斐济'], 'FK': ['福克兰群岛（马尔维纳斯）'], 'FM': ['密克罗尼西亚联邦'], 'FO': ['法罗群岛'], 'FR': ['法国'], 'GA': ['加蓬'], 'GB': ['英国'], 'GD': ['格林纳达'], 'GE': ['格鲁吉亚'], 'GF': ['法属圭亚那'], 'GH': ['加纳'], 'GI': ['直布罗陀'], 'GL': ['格陵兰'], 'GM': ['冈比亚'], 'GN': ['几内亚'], 'GP': ['瓜德罗普'], 'GQ': ['赤道几内亚'], 'GR': ['希腊'], 'GT': ['危地马拉'], 'GU': ['关岛'], 'GW': ['几内亚比绍'], 'GY': ['圭亚那'], 'HK': ['赫德岛和麦克唐纳岛'], 'HN': ['洪都拉斯'], 'HR': ['克罗地亚'], 'HT': ['海地'], 'HU': ['匈牙利'], 'ID': ['印度尼西亚'], 'IE': ['爱尔兰'], 'IL': ['以色列'], 'IN': ['印度'], 'IO': ['英属印度洋领地'], 'IQ': ['伊拉克'], 'IR': ['伊朗'], 'IS': ['冰岛'], 'IT': ['意大利'], 'JM': ['牙买加'], 'JO': ['约旦'], 'JP': ['日本'], 'KE': ['肯尼亚'], 'KG': ['吉尔吉斯斯坦'], 'KH': ['柬埔寨'], 'KI': ['基里巴斯'], 'KM': ['科摩罗'], 'KN': ['圣基茨和尼维斯'], 'KP': ['朝鲜'], 'KR': ['韩国'], 'KW': ['科威特'], 'KY': [
        '开曼群岛'], 'KZ': ['哈萨克斯坦'], 'LA': ['老挝'], 'LB': ['黎巴嫩'], 'LC': ['圣卢西亚'], 'LI': ['列支敦士登'], 'LK': ['斯里兰卡'], 'LR': ['利比里亚'], 'LS': ['莱索托'], 'LT': ['立陶宛'], 'LU': ['卢森堡'], 'LV': ['拉脱维亚'], 'LY': ['利比亚'], 'MA': ['摩洛哥'], 'MC': ['摩纳哥'], 'MD': ['摩尔多瓦'], 'MG': ['马达加斯加'], 'MH': ['马绍尔群岛'], 'MK': ['前南马其顿'], 'ML': ['马里'], 'MM': ['缅甸'], 'MN': ['蒙古'], 'MO': ['澳门'], 'MP': ['北马里亚纳'], 'MQ': ['马提尼克'], 'MR': ['毛利塔尼亚'], 'MS': ['蒙特塞拉特'], 'MT': ['马耳他'], 'MU': ['毛里求斯'], 'MV': ['马尔代夫'], 'MW': ['马拉维'], 'MX': ['墨西哥'], 'MY': ['马来西亚'], 'MZ': ['莫桑比克'], 'NA': ['纳米比亚'], 'NC': ['新喀里多尼亚'], 'NE': ['尼日尔'], 'NF': ['诺福克岛'], 'NG': ['尼日利亚'], 'NI': ['尼加拉瓜'], 'NL': ['荷兰'], 'NO': ['挪威'], 'NP': ['尼泊尔'], 'NR': ['瑙鲁'], 'NU': ['纽埃'], 'NZ': ['新西兰'], 'OM': ['阿曼'], 'PA': ['巴拿马'], 'PE': ['秘鲁'], 'PF': ['法属波利尼西亚'], 'PG': ['巴布亚新几内亚'], 'PH': ['菲律宾'], 'PK': ['巴基斯坦'], 'PL': ['波兰'], 'PM': ['圣皮埃尔和密克隆'], 'PR': ['波多黎各'], 'PT': ['葡萄牙'], 'PW': ['帕劳'], 'PY': ['巴拉圭'], 'QA': ['卡塔尔'], 'RE': ['留尼汪'], 'RO': ['罗马尼亚'], 'RU': ['俄罗斯联邦'], 'RW': ['卢旺达'], 'SA': ['沙特阿拉伯'], 'SB': ['所罗门群岛'], 'SC': ['塞舌尔'], 'SD': ['苏丹'], 'SE': ['瑞典'], 'SG': ['新加坡'], 'SH': ['圣赫勒拿'], 'SI': ['斯洛文尼亚'], 'SK': ['斯洛伐克'], 'SL': ['塞拉利昂'], 'SM': ['圣马力诺'], 'SN': ['塞内加尔'], 'SO': ['索马里'], 'SR': ['苏里南'], 'ST': ['圣多美和普林西比'], 'SV': ['萨尔瓦多'], 'SY': ['叙利亚'], 'SZ': ['斯威士兰'], 'TC': ['特克斯和凯科斯群岛'], 'TD': ['乍得'], 'TG': ['多哥'], 'TH': ['泰国'], 'TJ': ['塔吉克斯坦'], 'TK': ['托克劳'], 'TL': ['东帝汶'], 'TM': ['土库曼斯坦'], 'TN': ['突尼斯'], 'TO': ['汤加'], 'TR': ['土耳其'], 'TT': ['特立尼达和多巴哥'], 'TV': ['图瓦卢'], 'TW': ['台湾'], 'TZ': ['坦桑尼亚'], 'UA': ['乌克兰'], 'UG': ['乌干达'], 'US': ['美国'], 'UY': ['乌拉圭'], 'UZ': ['乌兹别克斯坦'], 'VA': ['梵蒂冈'], 'VC': ['圣文森特和格林纳丁斯'], 'VE': ['委内瑞拉'], 'VG': ['英属维尔京群岛'], 'VI': ['美属维尔京群岛'], 'VN': ['越南'], 'VU': ['瓦努阿图'], 'WF': ['瓦利斯和富图纳'], 'WS': ['萨摩亚'], 'YE': ['也门'], 'YT': ['马约特'], 'ZA': ['南非'], 'ZM': ['赞比亚'], 'ZW': ['津巴布韦']}

    return geo_codes_list


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


def pure_csv_content(inputs_source_file):
    '''
    Delete the extra message in single csv
    '''

    # Create pure folder if not exists
    pure_folder = '../pure/'
    if os.path.exists(pure_folder) == False:
        os.mkdir(pure_folder)

    # Define the outputs pure name
    outputs_pure_file = pure_folder + inputs_source_file

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

    return inputs_source_file + " precessed success, pured file saved as " + outputs_pure_file + "."


def pure_csv_list(source_csv_list):
    '''
    Pure the csv file list via loop
    '''
    for csv_file in source_csv_list:
        print(pure_csv_content(csv_file))

    return "inputs_source_file"


def csv_to_list(filename):
    '''
    Read csv content and convert to list
    '''

    # Open filename and using split('\n') to list
    with open(filename, mode='r', encoding='utf-8') as file_object:
        file_read_content = file_object.read().split('\n')

    return file_read_content


def merge_to_geo_list(list_name, geo_codes_list):
    '''
    Merge the DSA and DSD data to geo_codes_list
    '''

    # Traversal the list_name then merge the origin value adn list_line value to one list
    for list_line in list_name:
        key = list_line[0]
        value = list_line[1]
        geo_codes_list[key] = geo_codes_list[key] + [value]


def final_result_write(customer_name, cur_date, list_dsa, list_dsd):
    '''
    Calculator the extra fields and write to file.
    '''

    # Name of final result
    result_filename = customer_name + '-bills-' + cur_date + '.csv'

    with open(result_filename, 'w', newline='') as csvfile:

        headers = ['Country Code', 'Country', 'DSA', 'DSD', 'Total', 'Total(MB)']

        list_dsa = csv_to_list(
            '/Volumes/data/tmp/downloads/akamai_bills_geo/pure/DSA_edge_bytes_by_country_area_1574238733.csv')
        list_dsd = csv_to_list(
            '/Volumes/data/tmp/downloads/akamai_bills_geo/pure/DSD_edge_bytes_by_country_area_1574237865.csv')

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

    return "Merged success."


def save_csv_content(result_csv_content, result_filename):
    '''
    Define the function that save the content to final result file
    '''

    # Create result folder if not exists
    result_folder = '../result/'
    if os.path.exists(result_folder) == False:
        os.mkdir(result_folder)

    # Define the outputs result name
    outputs_result_file = result_folder + result_filename

    # Open result file then write and save
    with open(outputs_result_file, newline='') as file_object:
        file_object.write(result_csv_content)

    return result_filename + " saved success."


if __name__ == "__main__":

    # Define the name of customer
    # customer_name = input('Input the name of customer:')
    customer_name = "Shein"

    # Define the dir of files location
    # dir_path = input("Inputs the directory which csv files was included:")
    dir_path = '/Volumes/data/tmp/downloads/akamai_bills_geo/source'
    
    # Define the filename of DSA and DSD report csv file
    filename_dsa = 'DSA.csv'
    filename_dsd = 'DSD.csv'

    # Get the current date
    cur_date = time.strftime("%Y-%m-%d", time.gmtime())

    # Get geo codes
    geo_codes_dict = init_geo_codes()

    # Change the work dir to $dir_path
    os.chdir(dir_path)

    # Pure the source csv files
    filenames_list = [filename_dsa, filename_dsd]
    filenames_list = pure_csv_content(filenames_list)
    
    # Read the file content and convert to list
    content_list_dsa = csv_to_list(filename_dsa)
    content_list_dsd = csv_to_list(filename_dsd)

    # Merge the file content and save result to $merged_result
    merge_to_geo_list(content_list_dsa, geo_codes_dict)
    merge_to_geo_list(content_list_dsd, geo_codes_dict)

    # Generator the final result and save to file
    merged_infomations = final_result_write(customer_name, cur_date, content_list_dsa, content_list_dsd)
    print(merged_infomations)