import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 데이터 불러오기
data = pd.read_excel('C:/AI/data_ai_with_python/ML_practice_publicData/data/data.xlsx')

# 데이터 필터링: 발생건수와 검거건수만 선택
occurred = data[data['구분'] == '발생건수'].drop(columns=['구분'])
arrested = data[data['구분'] == '검거건수'].drop(columns=['구분'])

# '연도'를 인덱스로 설정
occurred.set_index('연도', inplace=True)
arrested.set_index('연도', inplace=True)

# 두 데이터를 병합
merged_data = pd.merge(occurred, arrested, left_index=True, right_index=True, suffixes=('_발생', '_검거'))

# 예시: '해킹(계정도용)'과 '해킹(단순침입)'을 이용하여 KNN 분석
# 특성(Feature)과 레이블(Label) 설정
X = merged_data[['해킹(계정도용)_발생', '해킹(단순침입)_발생']]  # 예시로 두 컬럼만 사용
y = merged_data['해킹(계정도용)_검거']  # 예시로 '해킹(계정도용)_검거'를 예측

# 데이터 나누기: 학습 데이터와 테스트 데이터
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 특성 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN 모델 학습
knn = KNeighborsClassifier(n_neighbors=3)  # k=3으로 설정
knn.fit(X_train, y_train)

# 예측
y_pred = knn.predict(X_test)

# 평가
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
