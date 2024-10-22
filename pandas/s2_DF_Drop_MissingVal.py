# 차근차근 데이터 분석과 인공지능_with python

import pandas as pd
df = pd.read_excel('C:\AI\data_ai_with_python\pandas\data.xlsx')
print(df)
print("----------------------------------------------")
# inplace->True : 최근에 수정한 상태로 저장됌 (default: False)
# 데이터프레임명.dropna(axis=0/1, subset=['칼럼명'], inplace=True/False)
# axis-> 0이면 레코드 삭제, axis->1이면 칼럼 전체 삭제

# df에서 '국어'컬럼의 결측치가 있는 행을 삭제해서 새로운 df로 저장하기
df2=df.dropna(axis=0,subset=['국어'])    #inplace=True를 하지 않으면, 원본 수정x

# df에서 결측치가 있는 행을 삭제해서 새로운 데이터프레임으로 저장하기
df3=df.dropna()


# 원본 데이터프레임과 결측치를 처리한 데이터프레임의 반별 평균 비교
df.groupby('반')[['국어','수학']].mean()
df2.groupby('반')[['국어','수학']].mean()
df3.groupby('반')[['국어','수학']].mean()

# 원본 데이터프레임과 결측치를 처리한 데이터프레임의 결측치 개수 비교
print(df.isna().sum())


