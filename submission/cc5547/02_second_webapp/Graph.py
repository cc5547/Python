# 그래프 생성
def create_graph(df_g1, df_g2):
  fig = go.Figure()

  # 그래프_1
  if df_g1 is not None:
    # 문자열에서 % 기호 제거 및 실수 타입으로 변환
    df_g1.iloc[:, 1:] = df_g1.iloc[:, 1:].apply(lambda x: x.str.rstrip('%')).astype(float)

    # 연도별 색상 지정
    colors = px.colors.qualitative.Set3[:len(df_g1.columns)-1]

    for i, col in enumerate(df_g1.columns[1:]):
        fig.add_trace(go.Bar(x=df_g1['Unnamed: 0'], y=df_g1[col], name=col, marker_color=colors[i]))

    # 레이아웃 설정
    fig.update_layout(
        title='필기시험 합격률',
        xaxis_title='시험 분류',
        yaxis_title='합격률%',
        yaxis=dict(range=[0, 100]),
        plot_bgcolor='#e2f3ea', # 차트 배경색 지정
        width=1000,
        height=700,)

  # 그래프_2
  elif df_g2 is not None:
    df_g2 = df_g2.drop(df_g2.columns[1], axis=1)
    years = df_g2.columns[1:]
    colors = px.colors.qualitative.Set3[:len(years)] # 연도별 색상 리스트 생성
    for i, year in enumerate(years):
        fig.add_trace(go.Bar(x=df_g2['구분'], y=df_g2[year], name=year, marker_color=colors[i]),)

    # 레이아웃 설정
    fig.update_layout(
        title='응시자 및 합격자',
        xaxis_title='시험 분류',
        yaxis_title='인원수',
        plot_bgcolor='#e2f3ea', # 차트 배경색 지정
        width=1000,
        height=700,)
  else : pass

  return fig