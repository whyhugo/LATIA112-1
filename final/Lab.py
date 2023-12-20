import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Info_UserData.csv', encoding='utf-8')
plt.rc('font', family='Microsoft JhengHei') # 讓 plt 可以顯示中文

tf = ['老師', '學生']
count = [0, 0]
for i in df['is_self_coach']:
    if i == True:
        count[0] += 1
    elif i == False:
        count[1] += 1

plt.pie(count, labels=tf, autopct='%1.1f%%', startangle=90)

# 設定圖表標題
plt.title('學生與老師人數分佈')

# 顯示圖表
plt.show()