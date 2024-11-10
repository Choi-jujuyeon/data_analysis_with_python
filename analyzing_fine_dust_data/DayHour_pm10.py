import pandas as pd
# 계절별 미세먼지 농도 변화 시각화 (막대 그래프)
import matplotlib.pyplot as plt
import seaborn as sns

# 2022년도 데이터 불러오기
data = pd.read_excel('C:/AI/data_ai_with_python/analyzing_fine_dust_data/data/2022.xlsx')

# 결측치를 0으로 설정
data.fillna(0, inplace=True)

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 요일과 시간대 추출
data['weekday'] = data['일시'].dt.weekday  # 0=월요일, 6=일요일
data['hour'] = data['일시'].dt.hour        # 시간대

# 요일별 미세먼지 농도 분석
weekday_fine_dust = data.groupby('weekday')['미세먼지'].mean().reset_index()
# 요일별 미세먼지 농도 출력
print("\n요일별 평균 미세먼지 농도:")
print(weekday_fine_dust)

# 시간대별 미세먼지 농도 분석
hour_fine_dust = data.groupby('hour')['미세먼지'].mean().reset_index()
# 시간대별 미세먼지 농도 출력
print("\n시간대별 평균 미세먼지 농도:")
print(hour_fine_dust)

# 요일별 미세먼지 농도 시각화
sns.barplot(x='weekday', y='미세먼지', data=weekday_fine_dust)
plt.title('Average Fine Dust Concentration by Weekday')
plt.xlabel('Weekday (0=Monday, 6=Sunday)')
plt.ylabel('Average Fine Dust Concentration')
plt.show()

# 시간대별 미세먼지 농도 시각화
sns.barplot(x='hour', y='미세먼지', data=hour_fine_dust)
plt.title('Average Fine Dust Concentration by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Fine Dust Concentration')
plt.show()
