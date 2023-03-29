from Data import CreateData
from FuncTion import Function
from SideBar import Sidebar

# Data, FuncTion, SideBar Class 들의 return 값들을 다 받아 오는 클래스 
class Get:
    def __init__(self) -> None:
        pass
        
    # joblib불러오기
    def get_data(self):
        dt = CreateData()
        data = dt.create_data()
        return data

    # SideBar.py의 Sidebar 클래스의 result_sidebar()를 통해 사이드바의 모든 입력값 return 받기
    def get_sidebar(self):
        sb = Sidebar()
        result = sb.result_sidebar()
        return result

    # FuncTion.py의 Function클래스의 return 받아 오기 // 추후 기능부로 수정하기
    def get_function(self, data, blood, clst, hbit, gender, heart, age):
        # 머신 러닝 <- 형변환
        fc = Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age))  # 객체 생성 타입 형변환
        result = fc.create_model()
        return result