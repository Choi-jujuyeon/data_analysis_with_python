import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data = pd.read_excel('C:/AI/data_ai_with_python/analyzing_fine_dust_data/data/2022.xlsx')

# 결측치 처리
data.fillna(0, inplace=True)

# 초미세먼지(PM2.5)와 미세먼지(PM10) 데이터
pm25 = data['초미세먼지']
pm10 = data['미세먼지']

# 히스토그램 그리기
plt.figure(figsize=(12, 6))

# 초미세먼지와 미세먼지의 히스토그램을 각각 그리기
plt.hist(pm25, bins=30, alpha=0.5, label='Fine Dust (PM2.5)', color='blue')
plt.hist(pm10, bins=30, alpha=0.5, label='Ultrafine Dust (PM10)', color='red')

# 그래프 제목과 축 레이블
plt.title('Distribution Comparison between Fine Dust (PM2.5) and Ultrafine Dust (PM10)')
plt.xlabel('Concentration')
plt.ylabel('Frequency')

# 범례 추가
plt.legend()

# 그리드 추가
plt.grid(True)

# 그래프 출력
plt.show()
