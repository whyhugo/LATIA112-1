# 均一教育平台使用者概況資料分析圖表網頁
學習分析工具實務應用 HW4
## 作業要求
1. 同一個網頁中有這三種圖
2. 資料是真實資料 / 教育相關
3. GitHub Pages 方法來產生網址
4. 網頁上要有資料與圖表說明

## 完成作品
### 資料來源
- Junyi Academy Online Learning Activity Dataset - Kaggle
  > https://www.kaggle.com/datasets/junyiacademy/learning-activity-public-dataset-by-junyi-academy
  - About Dataset
    The importance and popularity of online learning have increased a lot as the world is moving into an information era. The current COVID-19 situation shows that online learning acts both as a promising medium for equitable quality education, and an essential component for the education system when campuses shut down.
    Junyi Academy Foundation, a non-profit organization based in Taiwan that aims to provide all children equitable quality education by technology, is eager to support our learning community during this pandemic. We release a dataset consisting of over 16 million exercise attempt logs on our platform from more than 72,000 students over the course of a year (from 2018/08 to 2019/07). We hope our dataset could empower the research of creating a better and personalized learning experience for students, and further encourage broader participation for contributing to the future of online learning from interdisciplinary experts.
### 分析目標
使用這份資料集當中提供的使用者數據，分析以下三項：
1. **各年級用戶人數分布**長條圖
2. **使用者當中老師與學生的占比**圓餅圖
3. **資料統計區間個月份新用戶登入人數**折線圖

### 分析工具
1. Python：將 Info_UserData.csv 進行 Pandas 資料統計（data_processing/Lab.py），提取出繪製分析目標圖表所需要的資料，並轉為 JSON 格式。
2. JS & Plotly：將資料儲存於 data.js；main.js 用於進行 plotly.js 繪製圖表。
3. HTML：index.html 將圖表布局在網頁上的主要結構。
4. CSS：style.css 設定圖表樣式與網頁排版。

最終運用 GitHub Pages 部署網站。
> https://whyhugo.github.io/LATIA112-1/plotly.js/HW4/index.html

下圖為網頁運行畫面。
![ing](https://whyhugo.github.io/LATIA112-1/plotly.js/HW4/網頁截圖.png)
![ing](https://whyhugo.github.io/LATIA112-1/plotly.js/HW4/網頁截圖_全.png)