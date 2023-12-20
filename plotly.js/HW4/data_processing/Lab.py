import pandas as pd
from collections import defaultdict
from datetime import datetime

df = pd.read_csv('Info_UserData.csv', encoding='utf-8')

tf = ['老師', '學生']
count = [0, 0]
for i in df['is_self_coach']:
    if i == True:
        count[0] += 1
    elif i == False:
        count[1] += 1

count = []
for i in range(12):
    count.append(int('0'))
for i in df['user_grade']:
    count[i-1] += 1

import csv
import json


monthly_counts = defaultdict(int)

for i in df['first_login_date_TW']:
    date_obj = datetime.strptime(i, '%Y-%m-%d')
    year_month = date_obj.strftime('%Y-%m')
    monthly_counts[year_month] += 1

sorted_counts = dict(sorted(monthly_counts.items()))

result_data = [{'month': month, 'count': count} for month, count in sorted_counts.items()]

