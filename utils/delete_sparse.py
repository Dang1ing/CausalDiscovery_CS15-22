import csv

# 读取CSV文件
input_file = 'jsj15-22_all.csv'
output_file = 'csj15-22.csv'

# 定义阈值（30%）
threshold = 70

with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取文件头
    header = next(reader)
    xh_index = header.index("xh")  # 找到"xh"列的索引

    # 初始化一个字典，用于统计每一列的零值数量和总行数
    zero_counts = {}
    total_rows = 0

    # 统计每一列的零值数量
    for col_index, col_name in enumerate(header):
        if col_index != xh_index:
            zero_counts[col_index] = 0

    for row in reader:
        total_rows += 1
        for col_index, value in enumerate(row):
            if col_index != xh_index and float(value) == 0.0:  # 排除"xh"列并检查是否为零
                zero_counts[col_index] += 1

    # 根据零值数量计算每一列的零值占比，决定是否保留
    columns_to_keep = [header[xh_index]]  # 保留"xh"列的值
    for col_index, zero_count in zero_counts.items():
        zero_percentage = (zero_count / total_rows) * 100
        if zero_percentage < threshold:
            columns_to_keep.append(header[col_index])

    # 重新写入文件头和符合条件的列
    writer.writerow(columns_to_keep)

    # 写入符合条件的行数据
    infile.seek(0)  # 回到文件开头
    next(reader)  # 跳过第一行
    for row in reader:
        row_to_write = [row[xh_index]]  # 保留"xh"列的值
        for col_index, col_name in enumerate(header):
            if col_index != xh_index and col_name in columns_to_keep:
                row_to_write.append(row[col_index])
        writer.writerow(row_to_write)

print("处理完成，结果保存在 '{}' 文件中".format(output_file))
