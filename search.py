import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

# CSV 파일에서 데이터 로드 및 파싱
def load_and_parse_csv(file_path, region_name):
    df = pd.read_csv(file_path)
    
    # 거리 데이터 파싱
    distance_start_idx = df.index[df.iloc[:, 0].fillna('').str.contains(region_name)].tolist()[0]
    distance_data = df.iloc[distance_start_idx+1:distance_start_idx+5, 1:5]
    distance_data.index = df.iloc[distance_start_idx+1:distance_start_idx+5, 0]
    distance_data.columns = df.iloc[distance_start_idx, 1:5]
    
    # 범죄 데이터 파싱
    crime_start_idx = df.index[df.iloc[:, 0].fillna('').str.contains(f"{region_name} 범죄")].tolist()[0]
    crime_data = df.iloc[crime_start_idx+1:crime_start_idx+4, 1:4]
    crime_data.index = df.iloc[crime_start_idx+1:crime_start_idx+4, 0]
    crime_data.columns = df.iloc[crime_start_idx, 1:4]
    
    return distance_data, crime_data

# 범죄 가중치 계산
def calculate_crime_weights(crime_data):
    crime_data = crime_data.apply(pd.to_numeric)
    crime_data.loc['가중치'] = crime_data.loc['강력범죄'] * 5 + crime_data.loc['중범죄'] * 3 + crime_data.loc['경범죄'] * 1
    return crime_data

# 가장 가까운 세부 구역 5개 선택
def find_nearest_subregions(start_subregion, distance_data):
    distances = distance_data.loc[start_subregion].astype(int)
    nearest_subregions = distances.sort_values().index[:5]
    return nearest_subregions

# 순찰 시간 할당
def allocate_patrol_time(crime_weights, total_time):
    patrol_times = (crime_weights.loc['가중치'] / crime_weights.loc['가중치'].sum()) * total_time
    return patrol_times

# 최적 경로 계산 (순서만 결정)
def calculate_optimal_route(distance_matrix):
    row_ind, col_ind = linear_sum_assignment(distance_matrix)
    return row_ind, col_ind

def main():
    # 데이터 로드
    region_files = {
        "신사동": '신사동.csv',
        "압구정동": '압구정동.csv',
        "논현 1동": '논현 1동.csv',
        "논현 2동": '논현 2동.csv',
        "청담동": '청담동.csv',
        "삼성 1동": '삼성 1동.csv',
        "삼성 2동": '삼성 2동.csv',
        "역삼 1동": '역삼 1동.csv',
        "역삼 2동": '역삼 2동.csv',
                
        # 다른 동의 데이터를 여기에 추가
    }
    
    region_data = {}
    for region_name, file_path in region_files.items():
        distance_data, crime_data = load_and_parse_csv(file_path, region_name)
        region_data[region_name] = {
            'distance': distance_data,
            'crime': crime_data,
            'weights': calculate_crime_weights(crime_data)
        }
    
    # 사용자 입력
    start_region = input("시작동 입력: ")
    start_subregion = input("시작 세부지역 입력: ")
    total_patrol_time = int(input("총 순찰시간 (분): "))
    
    # 시작 동의 데이터 로드
    distance_data = region_data[start_region]['distance']
    crime_weights = region_data[start_region]['weights']
    
    # 가장 가까운 세부 구역 5개 선택
    nearest_subregions = find_nearest_subregions(start_subregion, distance_data)
    
    # 범죄 가중치가 높은 3개 구역 선택
    top_crime_subregions = nearest_subregions[:3]
    
    # 최적 경로 계산
    distance_matrix = distance_data.loc[top_crime_subregions, top_crime_subregions].values.astype(int)
    row_ind, col_ind = calculate_optimal_route(distance_matrix)
    optimal_route = [top_crime_subregions[i] for i in row_ind]
    
    # 순찰 시간 할당
    patrol_times = allocate_patrol_time(crime_weights, total_patrol_time)
    
    # 결과 출력
    for subregion in optimal_route:
        print(f"{subregion} ({patrol_times[subregion]:.2f}분)")

if __name__ == "__main__":
    main()
