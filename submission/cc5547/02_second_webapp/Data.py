import pandas as pd

class Create:
    def __init__(self) -> None :
        self.path = ["https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv", \
                    "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_1.csv", \
                    "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_2.csv"]

        self.df, \
        self.df_g1, \
        self.df_g2 = self.create_data()

    def create_data(self) :
        try : 
            df = pd.read_csv(self.path[0]).iloc[:, 1:]
            df_g1 = pd.read_csv(self.path[1])
            df_g2 = pd.read_csv(self.path[2])
            df.index += 1
            return df, df_g1, df_g2

        except Exception as e : 
            return st.error(e)

    def get_data(self) : return self.df, self.df_g1, self.df_g2