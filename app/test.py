import pandas as pd

# 데이터셋을 불러옵니다.
data = {
    'userId': [1, 1, 2, 2],
    'movieId': [1, 2, 1, 2],
    'rating': [4, 3, 5, 4]
}
df = pd.DataFrame(data)

# userId와 movieId를 범주형으로 변환합니다.
df['userId'] = df['userId'].astype('category')
df['movieId'] = df['movieId'].astype('category')

print(df)