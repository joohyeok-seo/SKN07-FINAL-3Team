import streamlit as st
import os
import json
from openai import OpenAI

# ✅ 최신 openai 패키지 방식
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📂 JSONL 데이터 미리 읽기 (사용하진 않지만 포함)
with open("train_data.jsonl", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]
st.write(f"📄 불러온 JSON 샘플 수: {len(data)}")

# 🌐 GPT 챗봇 UI
st.title("💬 GPT-3.5 기본 식단 챗봇 (파인튜닝 전)")
user_input = st.text_input("질문을 입력하세요 (예: 고추잡채 단백질 몇g?)")

if st.button("질문하기") and user_input:
    with st.spinner("GPT 응답 생성 중..."):
        try:
            # 🔁 최신 방식으로 GPT 호출
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "너는 건강 식단을 추천해주는 전문가야."},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.success("✅ GPT 응답:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")