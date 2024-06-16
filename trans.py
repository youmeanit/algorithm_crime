import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='역삼 1동')

# CSV 파일로 저장
df.to_csv('역삼 1동', index=False)