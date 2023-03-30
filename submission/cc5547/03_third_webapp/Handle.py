from Data import CreateData
from SideBar import Sidebar
from FuncTion import Function

# Data, FuncTion, SideBar Class 들의 return 값들을 다 받아 오는 클래스 
class Get : # test
    def __init__(self) -> None:
        self.dt = CreateData()
        self.sb = Sidebar()
    # joblib불러오기
    def get_data(self) : 
        return self.dt.result_data()

    # SideBar.py의 Sidebar 클래스의 result_sidebar()를 통해 사이드바의 모든 입력값 return 받기
    def get_sidebar(self) : 
        return self.sb.result_sidebar()

    def get_function(self, data, blood, clst, hbit, gender, heart, age) :
        return Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age)).result_model()