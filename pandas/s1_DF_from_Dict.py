# 차근차근 데이터 분석과 인공지능_with python
# 110p-예제) 파이썬 딕셔너리를 이용하여 판다스 데이터 프레임 생성하기

# CVS 파일을 업로드할 경우 : read_cvs('cvs 파일명', encoding='UTF-8')
# excel 파일을 업로드 할 경우 : read_excel('파일명')

import pandas as pd

df = pd.DataFrame({'name':['Kim','Choi','Park'],'age':[27,33,19],'score':[92,98,87]})
print(df)