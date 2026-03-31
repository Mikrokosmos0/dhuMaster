import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

import os
import matplotlib.font_manager as fm

# 强制加载 Windows 的字体文件（解决 Matplotlib 获取不到或缓存问题）
for path in ['C:/Windows/Fonts/simsun.ttc', 'C:/Windows/Fonts/simsun.ttf', 'C:/Windows/Fonts/times.ttf']:
    if os.path.exists(path):
        fm.fontManager.addfont(path)

# 设字体：英文和数字优先Times New Roman，遇到中文时自动回退为宋体
plt.rcParams['font.family'] = ['Times New Roman', 'SimSun', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题

# 设定的消融实验数据
N_values = [1, 2, 3, 4, 5]
dice_scores = [89.50, 91.10, 91.95, 91.80, 91.65]

# 创建图表，设置大小
plt.figure(figsize=(8, 5))

# 绘制折线图，采用虚线和空心圆点，模仿图3-5的学术风格
plt.plot(N_values, dice_scores, marker='o', linestyle='--', color='#2ca02c', 
         markerfacecolor='white', markeredgecolor='#2ca02c', markersize=8, linewidth=1.5)

# 坐标轴标签
plt.xlabel('滤波器基底维度 (N)', fontsize=12)
plt.ylabel('平均 DSC (%)', fontsize=12)

# 设置X轴刻度
plt.xticks(N_values)

# 添加Y轴方向的辅助网格线，增加学术感，颜色设为灰色
plt.grid(axis='y', linestyle='-', color='#cccccc')

# 调整边框和刻度线
ax = plt.gca()
# 左右边框竖线去掉
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# 上下边框线和中间网格线保持一样的灰色
ax.spines['top'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

# 去掉左侧Y轴刻度小短线
ax.tick_params(axis='y', left=False)
# 调整底部X轴刻度小短线为灰色，但保留数字为默认颜色
ax.tick_params(axis='x', color='#cccccc')

# 在数据点上方标注具体的数值
for i, txt in enumerate(dice_scores):
    plt.annotate(f"{txt:.2f}", (N_values[i], dice_scores[i]), 
                 textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# 设置Y轴范围，使折线变化更直观
plt.ylim(89.0, 92.5)

# 保存高分辨率图片，供论文使用
plt.savefig('ablation_N.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()