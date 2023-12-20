import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Info_UserData.csv', encoding='utf-8')
plt.rc('font', family='Microsoft JhengHei') # 讓 plt 可以顯示中文

def user_type():
    tf = ['老師', '學生']
    count = [0, 0]
    for i in df['is_self_coach']:
        if i == True:
            count[0] += 1
        elif i == False:
            count[1] += 1
    return count

def user_grade():
    count = []
    for i in range(12):
        count.append(int('0'))
    for i in df['user_grade']:
        count[i-1] += 1

def user_login():
    monthly_counts = defaultdict(int)

    for i in df['first_login_date_TW']:
        date_obj = datetime.strptime(i, '%Y-%m-%d')
        year_month = date_obj.strftime('%Y-%m')
        monthly_counts[year_month] += 1

    sorted_counts = dict(sorted(monthly_counts.items()))
    return sorted_counts

plt.pie(count, labels=tf, autopct='%1.1f%%', startangle=90)

plt.title('學生與老師人數分佈')

plt.show()