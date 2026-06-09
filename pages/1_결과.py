import streamlit as st

st.set_page_config(page_title="결과", page_icon="📋")

st.title("📋 내 BMI 결과")

# main.py 에서 저장한 값을 여기서 읽음
if "bmi" not in st.session_state:
    st.warning("먼저 홈에서 계산을 해주세요!")
    st.stop()

bmi = st.session_state["bmi"]

st.metric("내 BMI", bmi)

if bmi < 18.5:
    st.error("저체중입니다.")
elif bmi < 23:
    st.success("정상입니다.")
elif bmi < 25:
    st.warning("과체중입니다.")
else:
    st.error("비만입니다.")
