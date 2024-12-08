import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

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

# 결측값 처리 (NaN 값이 있을 경우 0으로 대체)
merged_data.fillna(0, inplace=True)

# 군집화할 특성 선택
X = merged_data[['해킹(계정도용)_발생', '해킹(단순침입)_발생', '해킹(자료유출)_발생', '서비스거부공격_발생']]

# 특성 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans 군집화 (K=3으로 설정)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# 군집 예측 결과
y_pred = kmeans.predict(X_scaled)

# 군집의 중심 확인
centroids = kmeans.cluster_centers_

# 실루엣 점수로 군집화 성능 평가
silhouette_avg = silhouette_score(X_scaled, y_pred)

print("Cluster Centers:")
print(centroids)
print("\nSilhouette Score:", silhouette_avg)
