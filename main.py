import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="가위 바위 보",
    page_icon="✊",
    layout="centered"
)

# CSS 스타일
st.markdown("""
<style>
    .main { background-color: #1a1a2e; }
    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        color: #e94560;
        margin-bottom: 0.2rem;
        letter-spacing: 0.1em;
    }
    .subtitle {
        text-align: center;
        color: #a8a8c0;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .score-box {
        background: #16213e;
        border-radius: 16px;
        padding: 1.2rem 2rem;
        text-align: center;
        border: 1px solid #0f3460;
    }
    .score-label {
        color: #a8a8c0;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.15em;
    }
    .score-number {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
    }
    .result-box {
        background: #16213e;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        border: 2px solid #0f3460;
        margin: 1.5rem 0;
    }
    .choice-display {
        font-size: 5rem;
        line-height: 1.2;
    }
    .vs-text {
        color: #e94560;
        font-size: 1.5rem;
        font-weight: 800;
        margin: 0 1rem;
    }
    .result-text-win {
        color: #4ecca3;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 1rem;
    }
    .result-text-lose {
        color: #e94560;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 1rem;
    }
    .result-text-draw {
        color: #f5a623;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 1rem;
    }
    .btn-container button {
        font-size: 2.5rem !important;
        height: 90px !important;
        border-radius: 16px !important;
        background: #16213e !important;
        border: 2px solid #0f3460 !important;
        transition: all 0.2s ease !important;
    }
    .btn-container button:hover {
        border-color: #e94560 !important;
        transform: scale(1.05) !important;
    }
    .history-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.4rem;
        background: #16213e;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0
if "history" not in st.session_state:
    st.session_state.history = []
if "last_result" not in st.session_state:
    st.session_state.last_result = None

# 게임 로직
CHOICES = {"가위": "✌️", "바위": "✊", "보": "🖐️"}
WIN_MAP = {"가위": "보", "바위": "가위", "보": "바위"}  # key가 이기는 상대

def play(user_choice):
    computer_choice = random.choice(list(CHOICES.keys()))
    if user_choice == computer_choice:
        result = "draw"
        st.session_state.draws += 1
    elif WIN_MAP[user_choice] == computer_choice:
        result = "win"
        st.session_state.wins += 1
    else:
        result = "lose"
        st.session_state.losses += 1

    st.session_state.last_result = {
        "user": user_choice,
        "computer": computer_choice,
        "result": result,
    }
    # 기록 최대 5개 유지
    st.session_state.history.insert(0, st.session_state.last_result)
    st.session_state.history = st.session_state.history[:5]

# --- UI ---
st.markdown('<div class="title">가위 바위 보</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">컴퓨터와 대결하세요!</div>', unsafe_allow_html=True)

# 점수판
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="score-box">
            <div class="score-label">승리</div>
            <div class="score-number" style="color:#4ecca3">{st.session_state.wins}</div>
        </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="score-box">
            <div class="score-label">무승부</div>
            <div class="score-number" style="color:#f5a623">{st.session_state.draws}</div>
        </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="score-box">
            <div class="score-label">패배</div>
            <div class="score-number" style="color:#e94560">{st.session_state.losses}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 선택 버튼
st.markdown("**무엇을 내시겠어요?**")
st.markdown('<div class="btn-container">', unsafe_allow_html=True)
b1, b2, b3 = st.columns(3)
with b1:
    if st.button("✌️\n가위", use_container_width=True):
        play("가위")
with b2:
    if st.button("✊\n바위", use_container_width=True):
        play("바위")
with b3:
    if st.button("🖐️\n보", use_container_width=True):
        play("보")
st.markdown('</div>', unsafe_allow_html=True)

# 결과 표시
if st.session_state.last_result:
    r = st.session_state.last_result
    user_emoji = CHOICES[r["user"]]
    comp_emoji = CHOICES[r["computer"]]

    if r["result"] == "win":
        result_html = '<div class="result-text-win">🎉 이겼습니다!</div>'
    elif r["result"] == "lose":
        result_html = '<div class="result-text-lose">😢 졌습니다...</div>'
    else:
        result_html = '<div class="result-text-draw">🤝 무승부!</div>'

    st.markdown(f"""
        <div class="result-box">
            <div style="display:flex; justify-content:center; align-items:center; gap:1rem;">
                <div>
                    <div class="choice-display">{user_emoji}</div>
                    <div style="color:#a8a8c0; font-size:0.85rem; text-align:center;">나</div>
                </div>
                <div class="vs-text">VS</div>
                <div>
                    <div class="choice-display">{comp_emoji}</div>
                    <div style="color:#a8a8c0; font-size:0.85rem; text-align:center;">컴퓨터</div>
                </div>
            </div>
            {result_html}
        </div>
    """, unsafe_allow_html=True)

# 최근 기록
if st.session_state.history:
    st.markdown("**최근 기록**")
    result_label = {"win": "✅ 승", "lose": "❌ 패", "draw": "➖ 무"}
    for h in st.session_state.history:
        st.markdown(f"""
            <div class="history-item">
                <span>{CHOICES[h['user']]} {h['user']} vs {CHOICES[h['computer']]} {h['computer']}</span>
                <span>{result_label[h['result']]}</span>
            </div>
        """, unsafe_allow_html=True)

# 초기화 버튼
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔄 점수 초기화", use_container_width=True):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.history = []
    st.session_state.last_result = None
    st.rerun()
