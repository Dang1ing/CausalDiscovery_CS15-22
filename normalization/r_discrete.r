library(bnlearn)
data <- read.csv("cs15-22_discrete.csv")
discretized_data <- discretize(data, method = "interval", breaks = 5)
# discretized_data
# 将离散化后的数据保存到CSV文件
write.csv(discretized_data, file = "cs15-22_discretized_data.csv", row.names = FALSE)
