import streamlit as st

st.set_page_config(page_title="BMI 계산기", page_icon="⚖️")

st.title("⚖️ BMI 계산기")
st.write("키와 몸무게를 입력하면 BMI를 계산해 드립니다.")

키 = st.number_input("키 (cm)", min_value=100, max_value=250, value=170)
몸무게 = st.number_input("몸무게 (kg)", min_value=20, max_value=200, value=65)

if st.button("계산하기"):
    bmi = 몸무게 / (키 / 100) ** 2

    # session_state 에 저장 → 다른 페이지에서도 읽을 수 있음
    st.session_state["bmi"] = round(bmi, 1)
    st.session_state["키"] = 키
    st.session_state["몸무게"] = 몸무게

    st.success(f"내 BMI는 **{bmi:.1f}** 입니다. 왼쪽 사이드바에서 결과를 확인해 보세요!")
