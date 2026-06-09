import streamlit as st

st.set_page_config(page_title="BMI 정보", page_icon="📖")

st.title("📖 BMI 기준표")

st.write("BMI는 몸무게(kg)를 키(m)의 제곱으로 나눈 값입니다.")

st.table({
    "구분":  ["저체중", "정상",    "과체중",  "비만"],
    "BMI":   ["18.5 미만", "18.5 ~ 22.9", "23 ~ 24.9", "25 이상"],
})
