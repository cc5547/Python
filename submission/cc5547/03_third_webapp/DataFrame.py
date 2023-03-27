import pandas as pd

# @st.cache
# df 생성
class CreateDataFrame:
    # df URL
    def __init__(self) -> None:
        self.df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
    
    # read
    def load_df(self):
        df = pd.read_csv(df_URL).iloc[:, 1:]
        
        return df

    # df 전처리 해줄 거 작성 하기
    def create_df(self) :
        df = self.load_df()
        df.index += 1
        
        return df

