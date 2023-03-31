import streamlit as st

class Sidebar:
    def __init__(self, df) -> None :
        self.sb = st.sidebar
        self.df = df
        self.area = df['지사명'].drop_duplicates().tolist()

    def create_sidebar(self) :
        self.sb.title('지역을 선택해주세요.')
        choice = s_bar.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', self.area, index = 10)



    # 사이드바
def side_bar(df) :
  for i in range(len(area)) : 
    if choice == area[i] : result = df[df['지사명'] == area[i]]
    else : pass

  search = s_bar.text_input('상세 검색 (시, 교명등의 키워드를 입력 :smile:)', value = '')
  result = df[(df['지사명'] == choice) & (df['시험장소'].str.contains(search))]
  result.index = np.arange(1, len(result) + 1)

  return result