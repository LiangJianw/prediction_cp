# 导入机器学习库, 线性回归模型
from sklearn import linear_model
# 导入交叉验证库
from sklearn.model_selection import cross_validate, train_test_split
# 导入数值计算库
import numpy as np
# 导入科学计算库
import pandas as pd
# 导入图标库
import matplotlib.pyplot as plt


df = pd.DataFrame(pd.read_excel("./data/prediction_cp.xls"))

# 将Times设置为x的值
x = np.array(df[["Times"]])
y = np.array(df["First"])

# 查看自变量、因变量的行数
print(x.shape, y.shape)

# 绘制散点图
# 设置字体
plt.rc("font", family="STXihei", size=15)
# 绘制散点图，广告成本X，点击量Y，设置颜色，标记点样式和透明度等参数
plt.scatter(x, y, 60, color='blue', marker='o', linewidth=3, alpha=0.8)
# 添加x轴标题
plt.xlabel('Times')
# 添加y轴标题
plt.ylabel('Nums')
# 添加图表标题
plt.title('彩票开奖期数与开奖号码')
# 设置背景网格线颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)
# 显示图表
plt.show()

# 分训练集、测试集， 测试集占40%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)

# 查看训练集的行数
print(x_train.shape, y_train.shape)

# 训练集代入模型
clf = linear_model.LinearRegression()
clf.fit(x_train, y_train)

# 得到相关数据：斜率，截距
print(clf.coef_, clf.intercept_)

# 判定系数R Square
print(clf.score(x_train, y_train))
print()
# 预测结果
print(clf.predict(x_test))
print(y_test)

