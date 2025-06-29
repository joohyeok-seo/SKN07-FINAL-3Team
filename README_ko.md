# 🥗 PUDAC: 개인 맞춤형 식단 추천 챗봇

> GPT 기반의 식단 추천 챗봇 서비스  
> RAG 구조, LLM 파인튜닝, 협업 필터링 기반  
> SK네트웍스 AI 부트캠프에서 최종적으로 단독 개발 완료

---

## 📌 프로젝트 개요

**푸닥(PUDAC)**은 사용자의 건강 목표, 알러지, 식습관 등을 바탕으로 개인 맞춤형 식단을 추천해주는 챗봇 서비스입니다.  
LLM 기반 문서 검색(RAG)과 식품 데이터베이스, 협업 필터링 알고리즘을 결합하여, 도시락 구독형 식단 추천에 적합한 답변을 제공합니다.

---

## 🔧 시스템 아키텍처

사용자 → 프론트엔드 (Streamlit/Chainlit)
→ 백엔드 (FastAPI)
→ ChromaDB 문서 검색
→ OpenAI Embedding API → FAISS 벡터 DB
→ OpenAI GPT API (파인튜닝 모델)

- **프론트엔드**: 실시간 챗 기반 UI  
- **백엔드**: 사용자 입력 처리 및 추천 로직 실행  
- **문서 검색**: FAISS + LangChain 기반 문서 유사도 탐색  
- **응답 생성**: GPT (도메인 데이터로 파인튜닝)

---

## 📂 데이터 수집 및 구성

- **데이터 출처**:
  - 식품의약품안전처 공개 식단 데이터
  - 네이버 백과사전 (일반 식품 정보)
  - 알러지 관련 공개 문서

- **DB 구조**:
  - 사용자 정보 (나이, 성별, 건강 목표, 알러지)
  - 음식/영양 데이터 (이름, 칼로리, 단백질 등)
  - 대화 히스토리 저장

---

## 🤖 추천 알고리즘 구성

### 1. LLM 기반 RAG 응답 시스템
- OpenAI Embedding → FAISS 검색 → LangChain → GPT 응답
- FastAPI 기반으로 전체 워크플로우 구성

### 2. 협업 필터링 기반 식단 추천
- 사용자 기반 CF: 비슷한 사용자들의 선호 식단 추천
- 아이템 기반 CF: 유사한 음식 간 추천
- Cold-start 문제 극복을 위해 GPT 응답과 혼합 사용

---

## 📈 성능 개선 전후 비교

| 상황 | 초기 GPT 응답 | 파인튜닝 GPT 응답 |
|------|----------------|--------------------|
| "다이어트 중인데 점심 추천해줘" | 샐러드나 과일을 드세요 | 닭구이(119kcal), 소라무침(122kcal), 오징어불고기(123kcal) 등 고단백 저지방 식단 추천 |

---

## 👨‍💻 나의 기여도

초기에는 4인 팀 프로젝트로 시작했지만,  
1명은 중도 탈퇴, 2명은 중간에 취업 확정으로 인해  
**최종 구현 및 발표 전반을 혼자 진행**하였습니다.

- 식단 데이터 수집 및 전처리  
- FastAPI 백엔드 구성 및 API 설계  
- GPT + FAISS + LangChain 기반 RAG 구조 구현  
- 협업 필터링 모델 설계  
- 챗봇 UI 구현 (Streamlit or Chainlit)  
- 최종 발표 자료 제작

---
