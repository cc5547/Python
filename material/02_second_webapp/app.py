# streamlit 라이브러리 호출
# 상대경로 복사 : material/02_second_webapp/app.py

# , use_column_width = True << 가운데 정렬
# st.number_input(label, value) << 데이터 입력

# 은행 이자 계산기
import streamlit as st

start_ment = "# 은행 이자 계산기"
picture_URL = "https://i.imgur.com/D7uu8FN.jpg" 
# , width = 300, height = 200


 with st.container():
  st.write(start_ment)
  st.image(picture_URL)


# st.write(
#   start_ment
#   )


# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg", width=800, height= 500)



# 적금 사진 링크

# start_img = "https://i.imgur.com/D7uu8FN.jpg"
# st.image(
#   "https://i.imgur.com/D7uu8FN.jpg"  width="300" height="200"

    
#     use_column_width=True
#     # 유튜브 사진 // "https://blog.kakaocdn.net/dn/JvPqb/btqAiWpd8sf/Ah9IYr6lDRBb8oxSCJYQyK/img.png"
#   )
