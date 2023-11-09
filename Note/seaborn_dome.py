# coding=utf-8
# coding=utf-8
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 生成模拟数据,6组数据
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5] * 6,
    'y': [11, 13, 15, 17, 19,
         21, 23, 25, 27, 29,
         31, 33, 35, 37, 39,
         41, 43, 45, 47, 49,
         51, 53, 55, 57, 59,
         61, 63, 65, 67, 69],
    'group': ['A', 'B', 'C', 'D', 'E', 'F'] * 5
})


# 使用seaborn绘制折线图,hue指定分组
sns.lineplot(data=data, x='x', y='y', hue='group')

# 添加标题等
plt.title('Seaborn Multiple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()