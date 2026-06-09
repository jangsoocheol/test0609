import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Plotly 실습", page_icon="📈", layout="wide")

st.title("📈 Plotly 차트 실습")
st.caption("사이드바에서 차트 종류를 바꿔보며 plotly.express 사용법을 익혀보세요.")

# ── 샘플 데이터 ─────────────────────────────────────────
df = pd.DataFrame({
    "월":   ["1월","2월","3월","4월","5월","6월"] * 3,
    "매출": [120,135,150,140,160,175,
             85, 90,110,125,130,145,
             200,210,195,220,230,215],
    "지역": ["서울"]*6 + ["부산"]*6 + ["대구"]*6,
})

# ── 사이드바: 차트 선택 ────────────────────────────────
with st.sidebar:
    st.header("⚙️ 차트 설정")
    chart = st.radio(
        "차트 종류",
        ["막대(bar)", "선(line)", "산점도(scatter)", "원형(pie)", "박스(box)"],
    )
    if chart != "원형(pie)":
        color_on = st.checkbox("지역별 색상 구분", value=True)

st.divider()

# ── 차트 + 코드 나란히 ────────────────────────────────
col_chart, col_code = st.columns([3, 2])

if chart == "막대(bar)":
    fig = px.bar(
        df, x="월", y="매출",
        color="지역" if color_on else None,
        barmode="group",
        title="지역별 월간 매출",
    )
    code = '''\
fig = px.bar(
    df, x="월", y="매출",
    color="지역",     # 색상으로 구분
    barmode="group",  # "stack" 으로 바꾸면 누적
    title="지역별 월간 매출",
)'''

elif chart == "선(line)":
    fig = px.line(
        df, x="월", y="매출",
        color="지역" if color_on else None,
        markers=True,
        title="매출 추이",
    )
    code = '''\
fig = px.line(
    df, x="월", y="매출",
    color="지역",
    markers=True,   # 꼭짓점에 점 표시
    title="매출 추이",
)'''

elif chart == "산점도(scatter)":
    fig = px.scatter(
        df, x="월", y="매출",
        color="지역" if color_on else None,
        size="매출",
        title="매출 산점도",
    )
    code = '''\
fig = px.scatter(
    df, x="월", y="매출",
    color="지역",
    size="매출",    # 점 크기를 값으로 표현
    title="매출 산점도",
)'''

elif chart == "원형(pie)":
    total = df.groupby("지역")["매출"].sum().reset_index()
    fig = px.pie(
        total, values="매출", names="지역",
        hole=0.4,
        title="지역별 총 매출 비중",
    )
    code = '''\
total = df.groupby("지역")["매출"].sum().reset_index()
fig = px.pie(
    total, values="매출", names="지역",
    hole=0.4,   # 도넛 크기 (0~1)
    title="지역별 총 매출 비중",
)'''

else:  # box
    fig = px.box(
        df, x="지역", y="매출",
        color="지역" if color_on else None,
        points="all",
        title="지역별 분포",
    )
    code = '''\
fig = px.box(
    df, x="지역", y="매출",
    color="지역",
    points="all",   # 원본 데이터 점 표시
    title="지역별 분포",
)'''

# ── 렌더링 ─────────────────────────────────────────────
with col_chart:
    st.plotly_chart(fig, use_container_width=True)

with col_code:
    st.markdown("**이 차트를 만든 코드**")
    st.code(code, language="python")
    st.markdown("**공통 패턴**")
    st.code('''\
import plotly.express as px

fig = px.bar(df, x="열이름", y="열이름")
st.plotly_chart(fig, use_container_width=True)
''', language="python")

# ── 원본 데이터 ─────────────────────────────────────────
with st.expander("📋 사용한 데이터 보기"):
    st.dataframe(df, use_container_width=True)
