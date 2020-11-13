#导包
import pandas as pd
import numpy as np
import pymysql
import time
import re
import traceback
def add_datepart(df, fldname, drop=True, time=False):
    """
    在时间上拆分特征数
    例如:
    ---------
     df = pd.DataFrame({ 'A' : pd.to_datetime(['3/11/2000', '3/12/2000', '3/13/2000'], infer_datetime_format=False) })
     df
        A
    0   2000-03-11
    1   2000-03-12
    2   2000-03-13
     add_datepart(df, 'A')
     df
        AYear AMonth AWeek ADay ADayofweek ADayofyear AIs_month_end AIs_month_start AIs_quarter_end AIs_quarter_start AIs_year_end AIs_year_start AElapsed
    0   2000  3      10    11   5          71         False         False           False           False             False        False          952732800
    1   2000  3      10    12   6          72         False         False           False           False             False        False          952819200
    2   2000  3      11    13   0          73         False         False           False           False             False        False          952905600
    """
    fld = df[fldname]
    fld_dtype = fld.dtype
    if isinstance(fld_dtype, pd.core.dtypes.dtypes.DatetimeTZDtype):
        fld_dtype = np.datetime64

    if not np.issubdtype(fld_dtype, np.datetime64):
        df[fldname] = fld = pd.to_datetime(fld, infer_datetime_format=True)
    targ_pre = re.sub('[Dd]ate$', '', fldname)
    attr = ['Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start']
    if time: attr = attr + ['Hour', 'Minute', 'Second']
    for n in attr: df[targ_pre + n] = getattr(fld.dt, n.lower())
    df[targ_pre + 'Elapsed'] = fld.astype(np.int64) // 10 ** 9
    if drop: df.drop(fldname, axis=1, inplace=True)

########################################################################################################
#建立mysql数据连接
#################                                      国内                            ###################
# 创建连接
conn = pymysql.connect(host="47.115.148.142",user="root",password="hht*LSL520",db="yq",charset="utf8")
sql = "SELECT * from chinahistory"
df1 = pd.read_sql(sql,conn)
conn.close()
df = df1[7:]
#重新分配索引
df=df.reset_index(drop=True)

#未来一周预测时间处理
n = 7
v = pd.to_datetime(df.ds.values[-1])
ds = pd.DataFrame(pd.date_range(v, v + pd.DateOffset(days=n), closed='right'),columns=['ds'])
ds.index = ds['ds']
ds1 = ds.sort_index(ascending=True, axis=0)
add_datepart(ds1, 'ds')
ds1.drop('dsElapsed', axis=1, inplace=True)  #过去的时间点

#按日期排序
data = df.sort_index(ascending=True, axis=0)
#取出数据
new_data = pd.DataFrame(index=range(0,len(df)),columns=['ds', 'confirm_add'])

for i in range(0,len(data)):
    new_data['ds'][i] = data['ds'][i]
    new_data['confirm_add'][i] = data['confirm_add'][i]

add_datepart(new_data, 'ds')
new_data.drop('dsElapsed', axis=1, inplace=True)  #过去的时间点

#new_data['ds'] = pd.to_datetime(new_data['ds'])
#划分训练集与验证集
train = new_data[:int(len(df)*0.8)]
valid = new_data[int(len(df)*0.8):]

x_train = train.drop('confirm_add', axis=1)
y_train = train['confirm_add']
x_valid = valid.drop('confirm_add', axis=1)
y_valid = valid['confirm_add']

##############                             线性回归                   ###########################
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)   #是不能得到得分的

# 做出预测   ，并算损失
preds = model.predict(x_valid)
#rms=np.sqrt(np.mean(np.power((np.array(y_valid)-np.array(preds)),2)))
#rms
# 做出预测   ，并算损失
preds1 = model.predict(ds1)
#rms=np.sqrt(np.mean(np.power((np.array(y_valid)-np.array(preds)),2)))
#rms

#建立未来索引
df[80:].index
ds[:].index

ds['Predictions'] = 0
ds['Predictions'] = preds1
ds.index = ds[:].index
valid['Predictions'] = 0
valid['Predictions'] = preds
valid.index = df[int(len(df)*0.8):].index
train.index = df[:int(len(df)*0.8)].index

#筛选分析后的数据
Linear1_1 = train['confirm_add'].index.tolist()
Linear1_2 = train['confirm_add'].values.tolist()
Linear2_1 = valid['confirm_add'].index.tolist()
Linear2_2 = valid['confirm_add'].values.tolist()
Linear3_1 = valid['Predictions'].index.tolist()
Linear3_2 = valid['Predictions'].values.tolist()
Linear4_1 = ds['Predictions'].index.tolist()
Linear4_2 = ds['Predictions'].values.tolist()

#####################                            需要返回的数据                     #######################
#x的数据
china_Linear_dss = Linear1_1+Linear2_1+Linear4_1
yy = [0]*len(Linear1_2)
ss = [0]*len(Linear4_1)
china_Linear_zhen = yy+Linear2_2+ss
china_Linear_yuce = yy+Linear3_2+ss
#预测
kll = [0]*len(Linear1_1+Linear2_1)
china_Linear_frutrue = kll+Linear4_2


##############                 KNN                 #####################

#KNN
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

#标准化
x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)
x_valid_scaled = scaler.fit_transform(x_valid)
x_valid = pd.DataFrame(x_valid_scaled)
#使用gridsearch查找最佳参数
params = {'n_neighbors':[2,3,4,5,6,7,8,9]}
knn = neighbors.KNeighborsRegressor()
model = GridSearchCV(knn, params, cv=5)
#训练模型，并预测
model.fit(x_train,y_train)

preds = model.predict(x_valid)
preds1 = model.predict(ds1)

ds['Predictions'] = 0
ds['Predictions'] = preds1
ds.index = ds[:].index
valid['Predictions'] = 0
valid['Predictions'] = preds
valid.index = df[int(len(df)*0.8):].index
train.index = df[:int(len(df)*0.8)].index

#筛选预测后的数据
knn1_1 = train['confirm_add'].index.tolist()
knn1_2 = train['confirm_add'].values.tolist()
knn2_1 = valid['confirm_add'].index.tolist()
knn2_2 = valid['confirm_add'].values.tolist()
knn3_1 = valid['Predictions'].index.tolist()
knn3_2 = valid['Predictions'].values.tolist()
knn4_1 = ds['Predictions'].index.tolist()
knn4_2 = ds['Predictions'].values.tolist()

#####################                            需要返回的数据                     #######################
#x数据
china_knn_dss = knn1_1+knn2_1+knn4_1
yy = [0]*len(knn1_1)
ss = [0]*len(knn4_1)
china_knn_zhen = yy+knn2_2+ss
china_knn_yuce = yy+knn3_2+ss
#预测
kll = [0]*len(knn1_1+knn2_1)
china_knn_frutrue = kll+knn4_2

#####################                         LSTM                         ############################

# 导包
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# 创建Dataframe
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(df)), columns=['ds', 'confirm_add'])
for i in range(0, len(data)):
    new_data['ds'][i] = data['ds'][i]
    new_data['confirm_add'][i] = data['confirm_add'][i]

# 索引
new_data.index = new_data.ds
new_data.drop('ds', axis=1, inplace=True)

#new_data['ds'] = pd.to_datetime(new_data['ds'])
# 创建训练集与测试集
dataset = new_data.values
train = dataset[0:80, :]
valid = dataset[80:, :]

# 数据转换为 x_train and y_train
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []
for i in range(60, len(train)):
    x_train.append(scaled_data[i - 60:i, 0])
    y_train.append(scaled_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# 创建LSTM网络
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=12, batch_size=3, verbose=2)

# 过去60来预测
inputs = new_data[len(new_data) - len(valid) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60, inputs.shape[0]):
    X_test.append(inputs[i - 60:i, 0])

X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
closing_price = model.predict(X_test)
closing_price = scaler.inverse_transform(closing_price)
# 损失
rms = np.sqrt(np.mean(np.power((valid - closing_price), 2)))

#筛选预测后的数据
train = new_data[:80]
valid = new_data[80:]
valid['Predictions'] = closing_price
lstm1_1 = train['confirm_add'].index.tolist()
lstm1_2 = train['confirm_add'].values.tolist()
lstm2_1 = valid['confirm_add'].index.tolist()
lstm2_2 = valid['confirm_add'].values.tolist()
lstm3_1 = valid['Predictions'].index.tolist()
lstm3_2 = valid['Predictions'].values.tolist()

################################   需要返回的数据         #######################
#x数据与预测数据
china_lstm_dss = lstm1_1+lstm2_1
yy = [0]*len(lstm1_1)
china_lstm_zhen = yy+lstm2_2
china_lstm_yuce = yy+lstm3_2






###################################################################################################


#                                                   国外
# 创建连接
conn = pymysql.connect(host="47.115.148.142",user="root",password="hht*LSL520",db="yq",charset="utf8")
sql = "SELECT * from globalhistory"
df2 = pd.read_sql(sql,conn)
conn.close()
df = df2[7:]
#重新分配索引
df=df.reset_index(drop=True)

#未来一周预测时间处理
n = 7
v = pd.to_datetime(df.ds.values[-1])
ds = pd.DataFrame(pd.date_range(v, v + pd.DateOffset(days=n), closed='right'),columns=['ds'])
ds.index = ds['ds']
ds1 = ds.sort_index(ascending=True, axis=0)
add_datepart(ds1, 'ds')
ds1.drop('dsElapsed', axis=1, inplace=True)  #过去的时间点

#按日期排序
data = df.sort_index(ascending=True, axis=0)
#取出数据
new_data = pd.DataFrame(index=range(0,len(df)),columns=['ds', 'confirm_add'])

for i in range(0,len(data)):
    new_data['ds'][i] = data['ds'][i]
    new_data['confirm_add'][i] = data['confirm_add'][i]

add_datepart(new_data, 'ds')
new_data.drop('dsElapsed', axis=1, inplace=True)  #过去的时间点

#new_data['ds'] = pd.to_datetime(new_data['ds'])
#划分训练集与验证集
train = new_data[:int(len(df)*0.8)]
valid = new_data[int(len(df)*0.8):]

x_train = train.drop('confirm_add', axis=1)
y_train = train['confirm_add']
x_valid = valid.drop('confirm_add', axis=1)
y_valid = valid['confirm_add']

##############                             线性回归                   ###########################
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)   #是不能得到得分的

# 做出预测   ，并算损失
preds = model.predict(x_valid)
#rms=np.sqrt(np.mean(np.power((np.array(y_valid)-np.array(preds)),2)))
#rms
# 做出预测   ，并算损失
preds1 = model.predict(ds1)
#rms=np.sqrt(np.mean(np.power((np.array(y_valid)-np.array(preds)),2)))
#rms

#建立未来索引
df[80:].index
ds[:].index

ds['Predictions'] = 0
ds['Predictions'] = preds1
ds.index = ds[:].index
valid['Predictions'] = 0
valid['Predictions'] = preds
valid.index = df[int(len(df)*0.8):].index
train.index = df[:int(len(df)*0.8)].index

#筛选分析后的数据
Linear1_1 = train['confirm_add'].index.tolist()
Linear1_2 = train['confirm_add'].values.tolist()
Linear2_1 = valid['confirm_add'].index.tolist()
Linear2_2 = valid['confirm_add'].values.tolist()
Linear3_1 = valid['Predictions'].index.tolist()
Linear3_2 = valid['Predictions'].values.tolist()
Linear4_1 = ds['Predictions'].index.tolist()
Linear4_2 = ds['Predictions'].values.tolist()

#####################                            需要返回的数据                     #######################
#x的数据
global_Linear_dss = Linear1_1+Linear2_1+Linear4_1
yy = [0]*len(Linear1_2)
ss = [0]*len(Linear4_1)
global_Linear_zhen = yy+Linear2_2+ss
global_Linear_yuce = yy+Linear3_2+ss
#预测
kll = [0]*len(Linear1_1+Linear2_1)
global_Linear_frutrue = kll+Linear4_2


##############                 KNN                 #####################

#KNN
from sklearn import neighbors
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

#标准化
x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)
x_valid_scaled = scaler.fit_transform(x_valid)
x_valid = pd.DataFrame(x_valid_scaled)
#使用gridsearch查找最佳参数
params = {'n_neighbors':[2,3,4,5,6,7,8,9]}
knn = neighbors.KNeighborsRegressor()
model = GridSearchCV(knn, params, cv=5)
#训练模型，并预测
model.fit(x_train,y_train)

preds = model.predict(x_valid)
preds1 = model.predict(ds1)

ds['Predictions'] = 0
ds['Predictions'] = preds1
ds.index = ds[:].index
valid['Predictions'] = 0
valid['Predictions'] = preds
valid.index = df[int(len(df)*0.8):].index
train.index = df[:int(len(df)*0.8)].index

#筛选预测后的数据
knn1_1 = train['confirm_add'].index.tolist()
knn1_2 = train['confirm_add'].values.tolist()
knn2_1 = valid['confirm_add'].index.tolist()
knn2_2 = valid['confirm_add'].values.tolist()
knn3_1 = valid['Predictions'].index.tolist()
knn3_2 = valid['Predictions'].values.tolist()
knn4_1 = ds['Predictions'].index.tolist()
knn4_2 = ds['Predictions'].values.tolist()


#####################                            需要返回的数据                     #######################
#x数据
global_knn_dss = knn1_1+knn2_1+knn4_1
yy = [0]*len(knn1_1)
ss = [0]*len(knn4_1)
global_knn_zhen = yy+knn2_2+ss
global_knn_yuce = yy+knn3_2+ss
#预测
kll = [0]*len(knn1_1+knn2_1)
global_knn_frutrue = kll+knn4_2

#####################                         LSTM                         ############################

# 导包
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# 创建Dataframe
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0, len(df)), columns=['ds', 'confirm_add'])
for i in range(0, len(data)):
    new_data['ds'][i] = data['ds'][i]
    new_data['confirm_add'][i] = data['confirm_add'][i]

# 索引
new_data.index = new_data.ds
new_data.drop('ds', axis=1, inplace=True)

#new_data['ds'] = pd.to_datetime(new_data['ds'])
# 创建训练集与测试集
dataset = new_data.values
train = dataset[0:80, :]
valid = dataset[80:, :]

# 数据转换为 x_train and y_train
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

x_train, y_train = [], []
for i in range(60, len(train)):
    x_train.append(scaled_data[i - 60:i, 0])
    y_train.append(scaled_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# 创建LSTM网络
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, epochs=12, batch_size=3, verbose=2)

# 过去60来预测
inputs = new_data[len(new_data) - len(valid) - 60:].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.transform(inputs)

X_test = []
for i in range(60, inputs.shape[0]):
    X_test.append(inputs[i - 60:i, 0])

X_test = np.array(X_test)

X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
closing_price = model.predict(X_test)
closing_price = scaler.inverse_transform(closing_price)
# 损失
rms = np.sqrt(np.mean(np.power((valid - closing_price), 2)))

#筛选预测后的数据
train = new_data[:80]
valid = new_data[80:]
valid['Predictions'] = closing_price
lstm1_1 = train['confirm_add'].index.tolist()
lstm1_2 = train['confirm_add'].values.tolist()
lstm2_1 = valid['confirm_add'].index.tolist()
lstm2_2 = valid['confirm_add'].values.tolist()
lstm3_1 = valid['Predictions'].index.tolist()
lstm3_2 = valid['Predictions'].values.tolist()

################################   需要返回的数据         #######################
#x数据与预测数据
global_lstm_dss = lstm1_1+lstm2_1
yy = [0]*len(lstm1_1)
global_lstm_zhen = yy+lstm2_2
global_lstm_yuce = yy+lstm3_2



########################     导数据到mysql         ###################

def get_conn():
	#建立连接
	conn = pymysql.connect(host="47.115.148.142", user="root", password="hht*LSL520", db="datafrom_hive", charset="utf8")
	#创建游标
	cursor = conn.cursor()
	return conn,cursor

def close_conn(conn,cursor):
	if cursor:
		cursor.close()
	if conn:
		conn.close()


#########################   规整当前数据         ##########################
china_preds = []
for i in range(len(china_Linear_dss)):
    china_preds.append([china_Linear_dss[i],china_Linear_zhen[i],china_Linear_yuce[i],china_Linear_frutrue[i],china_knn_zhen[i],china_knn_yuce[i],china_knn_frutrue[i]])

global_preds = []
for i in range(len(global_Linear_dss)):
    global_preds.append([global_Linear_dss[i],global_Linear_zhen[i],global_Linear_yuce[i],global_Linear_frutrue[i],global_knn_zhen[i],global_knn_yuce[i],global_knn_frutrue[i]])

china_lstm_preds = []
for i in range(len(china_lstm_dss)):
    china_lstm_preds.append([china_lstm_dss[i],china_lstm_zhen[i],china_lstm_yuce[i]])

global_lstm_preds = []
for i in range(len(global_lstm_dss)):
    global_lstm_preds.append([global_lstm_dss[i],global_lstm_zhen[i],global_lstm_yuce[i]])


#####################     插入数据到mysql              #############################

#插入china_preds数据
def update_china_preds():
	cursor = None
	conn = None
	try:
		conn,cursor = get_conn()
		sql = "insert into china_preds(china_dss,china_Linear_zhen,china_Linear_yuce,china_Linear_frutrue,china_knn_zhen,china_knn_yuce,china_knn_frutrue) values(%s,%s,%s,%s,%s,%s,%s)"
		
		print(f"{time.asctime()}开始更新china预测数据")
		for item in china_preds:
			cursor.execute(sql,item)
		conn.commit()
		print(f"{time.asctime()}china预测更新到最新数据")
	except:
		traceback.print_exc()
	finally:
		close_conn(conn,cursor)

update_china_preds()

#插入global_preds数据
def update_global_preds():
    cursor = None
    conn = None
    try:
        conn,cursor = get_conn()
        sql = "insert into global_preds(global_dss,global_Linear_zhen,global_Linear_yuce,global_Linear_frutrue,global_knn_zhen,global_knn_yuce,global_knn_frutrue) values(%s,%s,%s,%s,%s,%s,%s)"
        
        print(f"{time.asctime()}开始更新global预测数据")
        for item in global_preds:
            cursor.execute(sql,item)
        conn.commit()
        print(f"{time.asctime()}global预测更新到最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)
        
update_global_preds()


#插入china_lstm_preds数据
def update_china_lstm_preds():
    cursor = None
    conn = None
    try:
        conn,cursor = get_conn()
        sql = "insert into china_lstm_preds(china_lstm_dss,china_lstm_zhen,china_lstm_yuce) values(%s,%s,%s)"
        
        print(f"{time.asctime()}开始更新china_lstm_preds预测数据")
        for item in china_lstm_preds:
            cursor.execute(sql,item)
        conn.commit()
        print(f"{time.asctime()}china_lstm_preds预测更新到最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)
        
update_china_lstm_preds()


#插入china_lstm_preds数据
def update_global_lstm_preds():
    cursor = None
    conn = None
    try:
        conn,cursor = get_conn()
        sql = "insert into global_lstm_preds(global_lstm_dss,global_lstm_zhen,global_lstm_yuce) values(%s,%s,%s)"
        
        print(f"{time.asctime()}开始更新global_lstm_preds预测数据")
        for item in global_lstm_preds:
            cursor.execute(sql,item)
        conn.commit()
        print(f"{time.asctime()}global_lstm_preds预测更新到最新数据")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn,cursor)
        
update_global_lstm_preds()