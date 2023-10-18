library(pcalg)
# 从混合型数据集中选择连续型和离散型变量
continuous_vars <- c("var1", "var2") # 连续型变量名称
discrete_vars <- c("var3", "var4") # 离散型变量名称

# 使用pc.stable函数学习贝叶斯网络结构
pc_result <- pc.stable(data, continuous = continuous_vars, discrete = discrete_vars)

# 打印学习到的网络结构
print(pc_result)

# 可以根据需要进行进一步分析，如参数估计和推断
