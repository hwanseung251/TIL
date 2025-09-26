📊 관심 종목 토론 데이터 수집·분석 (Django + Selenium + OpenAI)

작성일: 2025-09-26
프로젝트명: 04_pjt
목적: 관심 종목 토론 댓글을 자동 수집·저장하고 웹에서 출력·삭제·분석까지 제공하는 시스템 구축

1. 🎯 목표 및 개요

본 프로젝트는 관심 종목 토론 댓글 자동 수집 → 저장 → 출력 → 삭제 → 감성분석 및 시각화까지 전 과정을 Django 기반으로 구현했습니다.
심화 기능으로 OpenAI API 기반 감성분석과 로고 마스크 워드클라우드 시각화를 추가하여 분석 결과를 직관적으로 확인할 수 있도록 했습니다.

2. 🛠 개발 환경 및 준비 사항

언어/프레임워크: Python 3.11+, Django 5.x

크롤링: Selenium, BeautifulSoup4, Requests

데이터베이스: SQLite (개발용)

기타:

Chrome + ChromeDriver (Selenium)

OpenAI Python SDK (심화 기능)

VS Code

3. 🔄 작업 프로세스

기능명세서 분석 및 필수/심화 요구사항 정리

역할 분담 및 구현 범위 확정

Django 앱 구조 설계 → Selenium 크롤러 구현

DB 모델/DAO 작성 → 저장/조회/삭제 연동

심화: OpenAI 감성분석 + 워드클라우드 구현

소스/산출물 정리 → Git 업로드 및 문서화

4. ✅ 기능 구현 내역
A. 종목 입력 (F01)

경로: /crawlings/index/

회사명 입력 폼 및 검색 버튼 제공

제출 시 서버로 종목명 전달 → 크롤링 단계로 진행

B. 종목 데이터 크롤링 (F02)

Selenium으로 토스증권 접속 → 검색 → 최상단 종목 선택 → 커뮤니티 탭 이동

수집 데이터: 회사명, 종목코드(선택), 댓글, 저장일자

DB 저장: bulk_create(ignore_conflicts=True) 사용 (중복 방지 & 성능 최적화)

C. 댓글 출력 (F03)

경로: /crawlings/comments/?name=삼성전자

종목별 필터 조회, 전체 목록 출력 가능

템플릿에서 리스트 형태로 표시

D. 댓글 삭제 (F04)

댓글 우측에 삭제 버튼 배치

클릭 시 해당 댓글 삭제 → redirect로 동일 페이지 재로딩

E. 감성분석 + 워드클라우드 (F05)

감성분석: OpenAI API로 상위 N개 댓글만 분석 (기본 60개)

출력: 긍·중·부 비율 요약 + 각 댓글 라벨/점수 배지

워드클라우드: 토스 로고 마스크 적용, 한글 폰트 지정

안정성: API 실패 시 중립 처리 폴백

5. 📑 비기능 요구사항 이행

NF01 문서화: 본 README 및 보고서 작성

NF02 Git 관리: .gitignore 적용, 불필요/민감 파일 제외

NF03 유지보수: DB, 크롤러, OpenAI 연동 코드 분리로 확장성 확보

6. 🏗 시스템 아키텍처

프론트:

index.html (입력)

comments.html (출력/삭제/시각화)

백엔드(Views):

crawling → Selenium 크롤링 & 저장

printing → DB 조회 & 분석 & 워드클라우드 생성

delete → 댓글 단건 삭제

7. 🗄 데이터 모델
class Comment(models.Model):
    company_name = models.CharField(max_length=100)
    stock_code   = models.CharField(max_length=20, blank=True)
    text         = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)

8. 🔑 주요 구현 상세

크롤링: 스크롤/더보기 반복 → DB bulk_create 저장

감성분석: 상위 N개만 API 호출, 실패 시 중립 처리

워드클라우드: 흑백 마스크 이진화 후 시각화

9. ▶ 실행 방법
# 마이그레이션 & 서버 실행
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


접속 흐름:

http://127.0.0.1:8000/crawlings/index/ → 종목명 입력

크롤링 완료 → /crawlings/comments/?name=종목명 이동

감성분석 결과 및 워드클라우드 확인

10. 🧪 테스트/예외 처리

크롤링 실패 시 사용자 메시지 출력

신규 댓글 없음 → 경고 표시

감성분석 오류 시 중립 처리 후 정상 출력

컬러 마스크도 자동 이진화 처리

11. 🔧 한계 및 개선 계획

종목코드 자동 수집/정규화 로직 보강

감성분석 모델/프롬프트 고도화

댓글 수집 안정성(로딩 대기 강화)

Chart.js 기반 도넛 차트/시계열 시각화 추가

캐시 및 페이징 UX 개선

12. 📂 디렉토리 구조 (요약)
project_root/
├─ crawlings/
│  ├─ models.py
│  ├─ views.py
│  ├─ SA.py
│  ├─ templates/
│  │  ├─ index.html
│  │  └─ comments.html
│  └─ static/crawlings/
│     ├─ fonts/Paperlogy-8ExtraBold.ttf
│     └─ toss_logo.png
└─ .env
