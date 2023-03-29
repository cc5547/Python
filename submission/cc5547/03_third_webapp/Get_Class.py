from Data import CreateData
from FuncTion import Function
from SideBar import Sidebar

class Get:
    def __init__(self) -> None:
        pass
    def get_data():
        dt = CreateData()  # 객체 생성
        data = dt.create_data()
        return data

    # SideBar.py의 Sidebar 클래스의 sidebar()를 통해 사이드바 생성 및 기능 구현
    def get_sidebar():
        sb = Sidebar()  # 객체 생성
        result = sb.result_sidebar()
        return result

    # FuncTion.py의 Function클래스의 ment 받아 오기 // 추후 기능부로 수정하기
    def get_function(data, blood, clst, hbit, gender, heart, age):
        fc = Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age))  # 객체 생성 타입 형변환
        result = fc.create_model()
        return result