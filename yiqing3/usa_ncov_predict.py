import numpy as np
import requests
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import datetime as dt


parameter_K = None
parameter_r = None


def logistic_function(t, P0):
    exp_r = np.exp(parameter_r * t)
    return parameter_K * P0 * exp_r / (parameter_K + P0 * (exp_r - 1))


# 1、获取历史数据
def get_url_message():
    url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'
    response = requests.get(url)
    usa_day_list = response.json()['data']

    x_data_date = []
    y_data = []
    for item in usa_day_list:
        y_data.append(item['confirm'])
        x_data_date.append(item['date'])
    # 可不可以是字符串？不可以！整数
    x_data = np.arange(0, len(y_data))
    print('天数为: ', x_data)
    print('确诊人数为: ', y_data)
    return usa_day_list, x_data_date, x_data, y_data


# 2、通过获取的确诊数据，进行拟合，求出Logistic方程中的参数
def get_right_num(x_data, y_data):
    # 遍历K的区间和r的区间
    K_range = np.arange(460000, 1000000, 1000)
    r_range = np.arange(0, 1, 0.01)

    loss = float('inf')
    optimal_K = None
    optimal_r = None
    optimal_P0 = None
    i = 0

    def logistic_function(t, P0):
        exp_r = np.exp(parameter_r * t)
        return parameter_K * P0 * exp_r / (parameter_K + P0 * (exp_r - 1))

    for K_ in K_range:
        for r_ in r_range:
            parameter_K = K_
            parameter_r = r_
            popt, pcov = curve_fit(logistic_function, x_data, y_data)
            # 我们需要从这 len(K_range) * len(r_range) 循环次数中，
            # 找出最优的一次（最优的K和最优的r），让logistic_function最符合预测
            # 如何评判是最优的一次呢？
            # 均方误差这个概念
            # 讲解一下两个参数
            # y_true:真实数据（疫情真实确诊人数）
            # y_pred:预测数据（通过logistic_function函数返回的值）
            loss_ = mean_squared_error(y_data, logistic_function(x_data, popt))
            if loss_ < loss:
                loss = loss_
                optimal_K = K_
                optimal_r = r_
                optimal_P0 = popt
            i += 1

            print('\r拟合进度：{0}{1}%'.format('▉' * int(10 * i / len(K_range) / len(r_range)),
                                          int(100 * i / len(K_range) / len(r_range))), end='')
    print('\noptimal_K: ', optimal_K)
    print('optimal_r: ', optimal_r)
    print('optimal_P0: ', optimal_P0)

    parameter_K = optimal_K
    parameter_r = optimal_r
    return parameter_K, parameter_r, optimal_P0


# 3、进行预测，把未来的天数输入到预测模型中，获取天数对应的预测确诊数
# 预测日期，从第一天到第100天，截止到4月11日，美国疫情开始第75天。可以预测后面的25天的发展趋势
def predict(optimal_P0):
    x_data_predict = np.arange(0, 100)
    y_data_predict = logistic_function(x_data_predict, optimal_P0)
    y_data_predict = y_data_predict.astype('int64')
    print('y_data_predict: ', y_data_predict)
    return y_data_predict


# 4、可视化
def screen(usa_day_list, x_data_date, y_data):
    # 获取第一天
    month, day = usa_day_list[0]['date'].split('.')
    # 字符串 转成 datetime
    first_date = dt.datetime.strptime('2020-' + month + '-' + day, '%Y-%m-%d')
    x_data_predict_date = [(first_date + (dt.timedelta(days=i))).strftime("%m.%d") for i in range(100)]
    # 解决中文乱码的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 指定画布大小
    plt.figure(figsize=(20, 6), dpi=300)
    # 预测确诊，注意：横坐标列表长度 要和 纵坐标列表长度 一致
    plt.plot(x_data_predict_date, y_data_predict, linewidth='1.5', color='red', label='预测确诊')
    # 现实确诊
    plt.scatter(x_data_date, y_data, s=35, color='dimgrey', label='实际确诊')
    # 显示图例，指定位置，防止图片被覆盖
    plt.legend(loc='upper left')
    plt.xticks(rotation=60)
    # 显示网格
    plt.grid()
    plt.ylabel('确诊人数')
    plt.savefig('usa_ncov_predict.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    # 1、获取历史数据
    usa_day_list, x_data_date, x_data, y_data = get_url_message()
    # 2、通过获取的确诊数据，进行拟合，求出Logistic方程中的参数
    parameter_K, parameter_r, optimal_P0 = get_right_num(x_data, y_data)
    # 3、进行预测，把未来的天数输入到预测模型中，获取天数对应的预测确诊数
    y_data_predict = predict(optimal_P0)
    # 4、可视化界面
    screen(usa_day_list, x_data_date, y_data)
