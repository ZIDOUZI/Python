from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(0, 8, 100, endpoint=True)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.plot(x, 3 * x ** 2 + 7 * x - 9)
plt.xlabel('x的取值')
plt.ylabel('y的值')
plt.title('我是图标题')
plt.legend(["我是图例"])
plt.text(2, -5, '我是曲线')
plt.show()
