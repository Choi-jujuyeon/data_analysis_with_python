import pandas as pd
# 계절별 미세먼지 농도 변화 시각화 (막대 그래프)
import matplotlib.pyplot as plt
import seaborn as sns

# 2022년도 데이터 불러오기
data = pd.read_excel('C:/AI/data_ai_with_python/analyzing_fine_dust_data/data/2022.xlsx')

# 데이터 구조 확인
# print(data.head())
# print(data.info())

# 각 열의 결측치 개수 확인
# missing_values = data.isnull().sum()
# print("\n각 속성의 결측치 개수:")
# print(missing_values)

# 결측치를 0으로 설정
data.fillna(0, inplace=True)

# 결측치 처리 후 데이터 확인
# print("\n결측치 처리 후 데이터:")
# print(data.head())
# print(data.info())

# '일시' 컬럼을 datetime 형식으로 변환
data['일시'] = pd.to_datetime(data['일시'])

# 날짜에서 월을 추출하여 계절을 매핑
# print(data)
# print(data['일시'])
# print(data['일시'].dt.month)
data['season'] = data['일시'].dt.month.map({
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall',
    12: 'Winter', 1: 'Winter', 2: 'Winter'
})

# 계절별 미세먼지 농도 분석
# '미세먼지' 컬럼을 사용하여 계절별 평균 미세먼지 농도 계산
seasonal_fine_dust = data.groupby('season')['미세먼지'].mean().reset_index()

# 각 계절별 미세먼지 농도 출력
print("\n각 계절별 평균 미세먼지 농도:")
print(seasonal_fine_dust)


# 계절 순서 지정 (Spring, Summer, Fall, Winter)
season_order = ['Spring', 'Summer', 'Fall', 'Winter']

# 막대그래프 시각화 (계절 순서 적용)
sns.barplot(x='season', y='미세먼지', data=seasonal_fine_dust, order=season_order)
plt.title('Average Fine Dust Concentration by Season')
plt.xlabel('Season')
plt.ylabel('Average Fine Dust Concentration')
plt.show()

