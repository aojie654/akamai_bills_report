# 地理位置(国家)流量合并

## 思路

1. 将文件使用文本方式进行读取
2. 删除非tittle和data行
3. 删除geoid列
4. 保存为新文件
5. 合并内容

    1. 读取DSA文件, 使用split('\n')分割为列表list_dsa

        遍历list_dsa, 用line_dsa[0]做key, append到geo_code_list相应的value
            key = line_dsa[0]
            dsa = line_dsa[1]
            geo_code_list[key] = geo_code_list[key] + [dsa]

    2. 同样的方法, 追加DSD流量

    3. 将key和value整合为列表, 并追加Total 和Total MB
        value = geo_code_list[key]
        dsa = geo_code_list[key][1]
        dsd = geo_code_list[key][2]
        total = dsa+dsd
        total_mb = math.ceil(total/1000/1000)
        [key] + [geo_code_list[key]], dsa, dsd, total, total_mb]

    4. 使用csv.DictWriter写入
