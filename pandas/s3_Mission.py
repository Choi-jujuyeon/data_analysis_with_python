# 차근차근 데이터 분석과 인공지능_with python

# 데이터프레임을 생성한 후 데이터프레임의 정보를 출력하시오.
import pandas as pd
df = pd.read_excel("C:/AI/data_ai_with_python/pandas/data2.xlsx")

# 대표국적별 영화 편수를 집계하시오.
df.groupby('대표국적')['영화편수'].sum()

# 대표국적이 '영국'인 데이터를 출력하시오.
df[df['대표국적'] =='영국']

# 대표 국적별 최상위 순위를 출력하시오.
df.sort_values(by="순위").groupby('대표국적')
