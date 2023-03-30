from Data import CreateData
from SideBar import Sidebar
from FuncTion import Function

# joblib불러오기
def get_data(self) : 
    return CreateData.result_data()

# SideBar.py의 Sidebar 클래스의 result_sidebar()를 통해 사이드바의 모든 입력값 return 받기
def get_sidebar(self) : 
    return Sidebar.result_sidebar()

def get_function(self, data, blood, clst, hbit, gender, heart, age) :
    return Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age)).result_model()
    # return FuncTion(data, blood, clst, hbit, gender, heart, age).result_model()