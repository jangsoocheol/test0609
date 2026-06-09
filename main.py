import streamlit as st
import random

def rock_paper_scissors():
    choices = ["가위", "바위", "보"]
    print("=== 가위바위보 게임 ===")
    
    while True:
        user = input("\n가위, 바위, 보 중 하나를 입력하세요 (종료: q): ").strip()
        
        if user == "q":
            print("게임 종료!")
            break
        
        if user not in choices:
            print("올바른 값을 입력해주세요.")
            continue
        
        computer = random.choice(choices)
        print(f"컴퓨터: {computer}")
        
        if user == computer:
            print("무승부!")
        elif (user == "가위" and computer == "보") or \
             (user == "바위" and computer == "가위") or \
             (user == "보" and computer == "바위"):
            print("🎉 이겼습니다!")
        else:
            print("😢 졌습니다.")

rock_paper_scissors()
