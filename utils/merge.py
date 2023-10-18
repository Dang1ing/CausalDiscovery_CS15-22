import csv

# 读取CSV文件
input_file = 'cs15-22_t.csv'
output_file = 'cs15-22.csv'

with open(input_file, 'r', newline='', encoding='UTF-8') as infile, open(output_file, 'w', newline='', encoding='UTF-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取文件头
    header = next(reader)

    # 找到需要合并的两列的索引（假设这两列分别为"列1"和"列2"）
    col1_index = header.index("高等数学I-2")
    col2_index = header.index("高等数学i2")

    # 重新写入文件头，添加新列名
    new_header = [col for col in header if col not in ("列1", "列2")] + ["高等数学2"]
    writer.writerow(new_header)

    # 写入合并后的数据行
    for row in reader:
        col1_value = row[col1_index]
        col2_value = row[col2_index]

        # 如果两列都为零或为空，则合并列为空
        if not col1_value or float(col1_value) == 0.0:
            combined_value = col2_value
        elif not col2_value or float(col2_value) == 0.0:
            combined_value = col1_value
        else:
            # 如果两列都有非零值，你需要定义一个合并规则，例如将它们连接起来
            combined_value = col1_value
        # 更新行数据，添加合并列的值，同时删除原始两列
        new_row = [value for index, value in enumerate(
            row) if index not in (col1_index, col2_index)]
        new_row.append(combined_value)

        writer.writerow(new_row)

print("处理完成，结果保存在 '{}' 文件中".format(output_file))
