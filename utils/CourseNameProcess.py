import pandas as pd

# 从CSV文件加载数据集
data = pd.read_csv('t_cj_jsj15_22.csv')

# 剔除课程名中额外空格
data['课程名'] = data['课程名'].str.strip()

# 修改错误课程名
data['kcm'] = data['kcm'].str.replace('高等数学i1', '高等数学I-1')
data['kcm'] = data['kcm'].str.replace('高等数学i2', '高等数学I-2')
data['kcm'] = data['kcm'].str.replace('线性代数与解析几何', '线性代数与解析几何ii')
data['kcm'] = data['kcm'].str.replace('金工实习Ⅰ', '金工实习')
data['kcm'] = data['kcm'].str.replace('电工实习Ⅰ', '电工实习')
data['kcm'] = data['kcm'].str.replace('电子技术实验-2', '电子技术实验2')
data['kcm'] = data['kcm'].str.replace('大学物理ii1', '大学物理II-1')
data['kcm'] = data['kcm'].str.replace('大学物理ii2', '大学物理II-2')
data['kcm'] = data['kcm'].str.replace('大学物理实验i1', '大学物理实验I-1')
data['kcm'] = data['kcm'].str.replace('大学物理实验i2', '大学物理实验I-2')
data['kcm'] = data['kcm'].str.replace('工程制图', '工程制图iii')
# data['kcm'] = data['kcm'].str.replace('工程制图', '工程制图iii')

# 保存修改后的数据集到新的CSV文件
data.to_csv('t_cj_jsj15_22.csv', index=False)
