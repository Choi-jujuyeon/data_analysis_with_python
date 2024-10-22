# 차근차근 데이터 분석과 인공지능_with python
# 109p-예제) 파이썬 2차원 리스트를 이용하여 판다스 데이터 프레임 생성하기

# CVS 파일을 업로드할 경우 : read_cvs('cvs 파일명', encoding='UTF-8')
# excel 파일을 업로드 할 경우 : read_excel('파일명')

import pandas as pd

df = pd.DataFrame([['Kim', 27, 92],['Choi',33,98],['Park',19,87]])

print(df)