import pandas as pd

# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='신사동')

# CSV 파일로 저장
df.to_csv('신사동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='압구정동')

# CSV 파일로 저장
df.to_csv('압구정동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='논현 1동')

# CSV 파일로 저장
df.to_csv('논현 1동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='논현 2동')

# CSV 파일로 저장
df.to_csv('논현 2동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='청담동')

# CSV 파일로 저장
df.to_csv('청담동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='삼성 1동')

# CSV 파일로 저장
df.to_csv('삼성 1동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='삼성 2동')

# CSV 파일로 저장
df.to_csv('삼성 2동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='역삼 1동')

# CSV 파일로 저장
df.to_csv('역삼 1동', index=False)
# 엑셀 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name='역삼 2동')

# CSV 파일로 저장
df.to_csv('역삼 2동', index=False)