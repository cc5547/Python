import pandas as pd

class Create:
    def __init__(self) -> None :
        self.df_URL = "submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
        self.df_URL_g1 = "submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_1.csv"
        self.df_URL_g2 = "submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_2.csv"

    def create_df(self) :
        self.df = pd.read_csv(self.df_URL).iloc[:, 1:].index += 1
        self.df_g1 = pd.read_csv(self.df_URL_g1)
        self.df_g2 = pd.read_csv(self.df_URL_g2)
        return df, df_g1, df_g2

    def get_data(self) :
        return self.create_df()