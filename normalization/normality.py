import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import probplot, shapiro, kstest, anderson

# 指定plt字体为宋体
plt.rcParams['font.sans-serif'] = ['SimSun']

data = pd.read_csv('cs18.csv')
print(data)
# 将零值替换为NaN
# data.replace(0, pd.NA, inplace=True)
# data.to_csv('cs15_22_NULL.csv', index=False)
# 获取数据集中的所有数值型变量列
# numeric_columns = data.columns
# numeric_columns = data.select_dtypes(include=['float', 'int'])

# 遍历每个数值型变量
for column_name in data.columns:
    # 提取当前变量的数据列
    column_data = data[column_name]
    column_data = column_data.dropna()

    # ------------ 执行Shapiro-Wilk正态性检验 --------------#
    statistic, p_value = shapiro(column_data)

    # 输出检验统计量和p-value
    print(f'{column_name}:')
    print('  Shapiro-Wilk统计量：', statistic)
    print('  p-value：', p_value)

    # 输出检验结果
    if statistic < 0.8:
        print("  不符合正态分布")
    else:
        print("  符合正态分布")
    # ------------ 生成 Q-Q 图 --------------#

    qq_plot = probplot(column_data, dist="norm", plot=plt)
    # plt.plot(qq_plot[0], qq_plot[0], color='red', linestyle='--')
    plt.title(f"{column_name}的Q-Q图")
    plt.show()

    # ------------ 执行Kolmogorov-Smirnov正态性检验 --------------#
    # ks_statistic, p_value = kstest(column_data, 'norm')

    # # 输出检验统计量和p-value
    # print('Kolmogorov-Smirnov统计量：', ks_statistic)
    # print('p-value：', p_value)

    # # 输出检验结果
    # if p_value < 0.05:
    #     print("数据不符合正态分布")
    # else:
    #     print("数据符合正态分布")

    # ------------ Anderson-Darling检验 --------------#
    # # 进行正态性评估
    # result = anderson(column_data, 'norm')

    # # 输出检验统计量和临界值
    # print('Anderson-Darling统计量：', result.statistic)
    # print('临界值：', result.critical_values)

    # # 输出检验结果
    # if result.statistic < result.critical_values[2]:
    #     print("数据符合正态分布")
    # else:
    #     print("数据不符合正态分布")
