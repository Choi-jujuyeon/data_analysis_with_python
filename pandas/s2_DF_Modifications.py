# 차근차근 데이터 분석과 인공지능_with python

import pandas as pd
df = pd.read_excel("C:\AI\data_ai_with_python\pandas\data.xlsx")

# df의 '국어'와 '수학'컬럼 값을 더해서 '총점'이라는 새로운 컬럼으로 생성하기-> '+'
df['총점'] = df['국어'] + df['수학']
print(df)

# df에서 원본 데이터프렘은 변경하지 않은 채 '확인여부' 컬럼을 삭제한 결과 출력하기-> .drop()
# axis=0이면 행 삭제! axis=1이면 레코드 삭제 
print(df.drop('확인여부',axis=1))
print(df.drop(0,axis=0))

# df2을 생성하고 0을 모두 찾아 7로 바꾸기->replace()
print("------------------------")
df2 = pd.DataFrame({'기호':['a','b','c','d','e'],'단가':[100,0,0,400,500], '수량':[1,1,1,2,0]})
# print(df2)
print(df2.replace(0,7))

# df2에서 0은 6으로, 1은 100으로 변경
print(df2.replace({0:6, 1:100}))

# df2에서 '단가' 칼럼의 0은 100으로, '수량' 칼럼의 1은 1000으로 바꾸기
print(df2.replace({'단가':{0:100}, '수량':{1:1000}}))

