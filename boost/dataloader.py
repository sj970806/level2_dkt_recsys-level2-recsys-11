#opt/ml/data에서 불러오기
import os
import pandas as pd
from sklearn.model_selection import train_test_split



# 데이터 로드 함수(train, test) from directory
def get_data(args):
    train_data = pd.read_csv(os.path.join(args.data_dir, f'FE{args.fe_num}', 'train_data.csv'))
    test_data = pd.read_csv(os.path.join(args.data_dir, f'FE{args.fe_num}', 'test_data.csv'))
    return train_data, test_data


# 데이터 스플릿 함수
def data_split(train_data):
    X = train_data.drop(['answerCode'], axis=1)
    y = train_data['answerCode']

    X_train, X_valid, y_train, y_valid = train_test_split(
        train_data.drop(['answerCode'], axis=1),
        train_data.answerCode,
        test_size=0.3, # 일단 이 정도로 학습해서 추이 확인
        shuffle=True,
    )
    return X_train, X_valid, y_train, y_valid