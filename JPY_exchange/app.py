import pandas as pd 
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def formPage():
    # 檔案抓取，注意編碼格式
    df = pd.read_csv("https://www.taifex.com.tw/data_gov/taifex_open_data.asp?data_name=DailyForeignExchangeRates", encoding='cp950')
    # 確認資料是否有空值
    df.isnull().sum()
    # 刪除不必要的資料
    df.drop(df.iloc[:, 5:], axis=1, inplace=True)
    df.drop(df.iloc[:, 2:4], axis=1, inplace=True)
    # 重新命名欄位名稱為英文
    df.columns = ["date", "usd-twd", "usd-jpy"]
    df.head()
    # 新增需求欄位
    df['twd-jpy'] = df['usd-twd'] / df['usd-jpy']
    # 刪除不必要的欄位與資料
    df.drop(df.iloc[:, 1:3],axis=1,inplace=True)
    df.info()
    # 轉換為日期時間格式
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    # 再轉換為字串，準備輸出至前端
    df['date'] = df['date'].astype(str)
    # 轉換為JSON格式
    result =df.to_json(orient="records")
    # 送至前端
    return render_template('index.html', exchangeData=result)
    
if __name__ == "__main__":
    app.run()