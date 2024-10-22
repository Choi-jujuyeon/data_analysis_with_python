# 차근차근 데이터 분석과 인공지능_with python

import pandas as pd
df = pd.read_excel('C:\AI\data_ai_with_python\pandas\data.xlsx')
print(df)

# inplace->True : 최근에 수정한 상태로 저장됌 (default: False)

# df에서 결측치 여부를 확인하기-> .isna()=>>없으면:False, 있으면: True
print(df.isna())

# df에서 각 컬럼별 결측치의 개수를 출력하기-> .isna().sum()
print(df.isna().sum())

# df의 '국어' 컬럼의 결측치를 '테스트중'로 채우기-> .fillna({'어떤 컬럼에서':'어떤 값으로 채울지'})
print(df.fillna({'국어':'미확인테스트중'}))

# df의 전체 컬럼에서 결측치를 0으로 채우기-> .fillna(동일하게 채울 값)
print(df.fillna('*'))
