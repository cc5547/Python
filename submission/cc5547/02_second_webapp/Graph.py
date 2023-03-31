import plotly.express as px
import plotly.graph_objects as go

class PlotlyGraph:
    def __init__(self, df_g1, df_g2) -> None :
        self.fig = go.Figure()
        self.df_g1 = df_g1
        self.df_g2 = df_g2

    def create_graph(self) :
        if self.df_g1 is not None :
            self.df_g1.iloc[:, 1:] = self.df_g1.iloc[:, 1:].apply(lambda x: x.str.rstrip('%')).astype(float)
            colors = px.colors.qualitative.Set3[:len(self.df_g1.columns)-1]
            for i, col in enumerate(self.df_g1.columns[1:]) :
                self.fig.add_trace(go.Bar(x=self.df_g1['Unnamed: 0'], y=self.df_g1[col], name=col, marker_color=colors[i]))
            # self.fig.add_trace(go.Scatter(x=new_x_values, y=new_y_values, name='New', mode='lines', line_color='red'))

            self.fig.update_layout(
                title='필기시험 합격률',
                xaxis_title='시험 분류',
                yaxis_title='합격률%',
                yaxis=dict(range=[0, 100]),
                plot_bgcolor='#e2f3ea', # 차트 배경색 지정
                width=1000,
                height=700,)
                
        elif self.df_g2 is not None :
            self.df_g2 = self.df_g2.drop(self.df_g2.columns[1], axis=1)
            years = self.df_g2.columns[1:]
            colors = px.colors.qualitative.Set3[:len(years)] # 연도별 색상 리스트 생성
            for i, year in enumerate(years):
                self.fig.add_trace(go.Bar(x=self.df_g2['구분'], y=self.df_g2[year], name=year, marker_color=colors[i]),)

            # 레이아웃 설정
            self.fig.update_layout(
                title='응시자 및 합격자',
                xaxis_title='시험 분류',
                yaxis_title='인원수',
                plot_bgcolor='#e2f3ea', # 차트 배경색 지정
                width=1000,
                height=700,)
        else : pass

        return self.fig

    def get_graph(self):
        return self.create_graph()