library(huge)
data <- read.csv("cs15-22_continuous.csv")
# L = huge.generator(graph = "cluster", g = 5)
# Q <- huge.npn(L$data)
data_normalized <- huge.npn(data)

# 将经过npn方法处理的数据保存到CSV文件
write.csv(data_normalized, file = "cs15-22_continuous_normalized.csv", row.names = FALSE)
