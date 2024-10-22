# 차근차근 데이터 분석과 인공지능_with python

import pandas as pd
df = pd.read_excel("C:\AI\data_ai_with_python\pandas\data.xlsx") #이렇게 해야 파일 불러와짐..

# df에서 숫자값을 갖는 칼럼들에 대한 전체 기본 통계 출력하기-> .describe()
print(df.describe())
print("-------------------------------")

# df에서 '반' 컬럼의 값별로 데이터 개수 출력하기-> .value_counts()
print(df['반'].value_counts())
print("-------------------------------")

# df에서 '국어'컬럼의 합계 출력하기-> .sum()
print(df['국어'].sum())
print("-------------------------------")

# df에서 '국어'칼럼의 평균 출력하기-> .mean()
print(df['국어'].mean())
print("-------------------------------")

# df에서 '반 별 데이터 합계 출력하기 ->반끼리 묶어야함 == .groupby()
print(df.groupby('반').sum())       #이것도 가능: print(df.groupby('반')[['국어', '수학']].sum())
print("-------------------------------")

# df에서 '반'별 데이터의 평균 출력하기
print(df.groupby('반')[['국어', '수학']].mean())
