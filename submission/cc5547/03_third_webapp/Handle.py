from Data import CreateData
from SideBar import Sidebar
from FuncTion import Function


def get_data() : return CreateData().result_data()
def get_sidebar() : return Sidebar().result_sidebar()
def get_function(data, blood, clst, hbit, gender, heart, age) : return Function(data, int(blood), int(clst), int(hbit), float(gender), int(heart), float(age)).result_model()