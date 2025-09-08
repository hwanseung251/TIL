# 프로젝트 전 공부 정리

## 기본 개념

- **마진 상쇄(Margin Collapse)**
    - `block` 요소끼리만 발생
    - `inline-block` 은 발생하지 않음
    - `inline(span 등)`은 margin으로 밀리지 않음 → 이미지 배치 시 주의
- **body 태그**
    - 브라우저 기본 margin 존재 → Bootstrap의 reset CSS가 초기화시켜줌

---

## 구조 설계

- 메뉴가 7개 → `div*7` 로 단순 반복 X (검색엔진 최적화, 시맨틱 태그 필요)
- **시맨틱 태그 활용**
    
    
    | 태그 | 의미 | 사용 예시 |
    | --- | --- | --- |
    | `<header>` | 문서/섹션의 머리글 | 로고, 내비게이션 |
    | `<nav>` | 내비게이션 링크 | 메뉴, 사이트맵 |
    | `<main>` | 주요 콘텐츠 영역 | 본문 콘텐츠 |
    | `<section>` | 관련 콘텐츠 묶음 | 기사, 챕터 |
    | `<article>` | 독립적 콘텐츠 | 블로그 글, 뉴스 |
    | `<aside>` | 보조 콘텐츠 | 광고, 관련 링크 |
    | `<footer>` | 문서/섹션의 바닥글 | 저작권, 연락처 |
- **Emmet 약어 예시**
    
    
    | 입력 | 결과 |
    | --- | --- |
    | `div*7` | `<div></div>` 7개 생성 |
    | `ul>li*3` | `<ul><li></li><li></li><li></li></ul>` |
    | `.box` | `<div class="box"></div>` |
    | `header>nav>ul>li*5` | 기본 내비게이션 구조 |

---

## CSS & 반응형

- **코드 정리** : `Alt + Shift + F` → 자동 들여쓰기 (Prettier)
- **폰트 적용** : Google Fonts → CSS에 import
- **반응형 CSS** : `@media` 사용
    
    ```css
    @media (max-width: 768px) {
      body { background: lightblue; }
    }
    
    ```
    
- **그리드 시스템 (Bootstrap)**
    - 한 줄을 12칸으로 나눔
    - Breakpoints (예시: `sm`, `md`, `lg`, `xl`)

---

## 꾸미기 효과 정리

| 기능 | CSS 예시 | 설명 |
| --- | --- | --- |
| Hover 효과 | `a:hover { color: red; }` | 마우스 올렸을 때 색 변경 |
| Transform 이동 | `transform: translateX(20px);` | 요소 위치 변경 |
| 회전 | `transform: rotate(45deg);` | 요소 회전 |
| 확대/축소 | `transform: scale(1.2);` | 크기 변화 |
| Transition | `transition: all 0.3s ease;` | 부드러운 애니메이션 |
| 애니메이션 | `@keyframes fadeIn { from{opacity:0;} to{opacity:1;} }` | 단계적 효과 |
| 타이핑 효과 | JS/라이브러리 사용 (`typed.js`) | 글자 입력 애니메이션 |

---

# 도서 페이지 UI 구현

## 1) 오늘 한 것

1. **폰트 적용**
    - Google Fonts를 불러오고, 전용 클래스(예: `.font-book`)를 만들어 특정 `div`에만 적용.
    - 본문 중 일부 강조는 `span`에 별도 색상 클래스를 부여해 처리.
2. **Navbar 구성 (Bootstrap)**
    - 부트스트랩 기본 네비바를 베이스로 아이템 구조를 정리.
    - Hover 시 포인트 컬러 적용: `.nav-link:hover { color: #fe4a51; }`
3. **커스텀 반응형 브레이크포인트**
    - Bootstrap의 미리 정의된 브레이크포인트(`sm=576px` 등) 대신, **직접 `@media`로 412px 기준**을 마련.
    - 화면 크기에 따라 메뉴 배치/토글러/글자 크기/여백이 바뀌도록 구현.
4. **반응형 줄바꿈**
    - `<br class="d-412-break">`를 넣고, 412px 이하에서만 보이게 해서 문장 가독성 확보.

---

## 2) 구현 상세 & 코드 해석

### A. 메뉴 레이아웃의 기본 상태(> 412px 가정)

```css
.expand-412 {
  display: flex;
  flex-direction: row;       /* 메뉴를 가로로 배치 */
  justify-content: flex-end; /* 메뉴를 우측 정렬 */
  font-size: 0.5rem;         /* 큰 화면 기준 기본 폰트(상대적으로 작게) */
}
nav {
  margin: 0 3rem;            /* 좌우 여백 확보로 시각적 균형 */
}

/* (권장) 큰 화면에서 토글러 숨김 */
@media (min-width: 413px) {
  .navbar-toggler { display: none; }
}

```

- **핵심:** `.expand-412`가 **플렉스 컨테이너**이며, 기본은 **가로 정렬 + 우측 정렬**입니다. 큰 화면에서 메뉴가 한 줄로 정돈되고, `nav`에 가로 여백을 넣어 답답하지 않게 보입니다.

### B. 412px 이하(휴대폰)에서의 전환

```css
@media (max-width: 411.9px) {
  .expand-412 {
    display: flex;
    flex-direction: column;  /* 세로로 쌓기 */
    align-items: flex-end;   /* 우측 정렬 유지 */
    margin-right: 20px;      /* 화면 가장자리와 간격 */
    font-size: 0.7rem;       /* 작은 화면에서 가독성↑ */
  }
  .expand-412 > a {
    padding: 4px 0;          /* 메뉴 간 터치 영역 확보 */
  }
}

```

- **왜 411.9px?** Bootstrap 문서에서도 **소수점 단위**로 경계를 끊어 라운딩 이슈(디바이스 픽셀 비율)를 피하는 패턴을 사용합니다.
- 작은 화면에선 **세로 스택 + 우측 정렬**로 손가락 접근성이 좋아지고, 폰트와 패딩을 키워 **가독성/터치 편의**를 높였습니다.

### C. 모바일 전용 줄바꿈

```css
@media (max-width: 412px) { .d-412-break { display: block; } }
@media (min-width: 413px) { .d-412-break { display: none; } }

```

- `<br class="d-412-break">` 를 문장 중간에 넣어두면, **412px 이하는 개행**, 그 이상은 **숨김**

### D. Hover 컬러

```css
.nav-link:hover { color: #fe4a51; }
```

- 기본 색 대비 호버 시 **시각 피드백** 제공. 접근성을 위해 `:focus`에도 같은 스타일을 주면 키보드 사용자에게도 친화적입니다.
    
    ```css
    .nav-link:hover, .nav-link:focus { color: #fe4a51; }
    ```
    

---

## 3) 어려웠던 점

1. **문제:** Bootstrap의 반응형은 `sm(576px)` 이상부터 프리셋이 있어 **412px 기준 전환이 어려움**
    
    **해결:** 직접 `@media (max-width: 411.9px)`와 `(min-width: 413px)`를 정의해 **커스텀 브레이크포인트**를 운용.
    
    → 결과적으로 **원하는 지점(412px)**에서 메뉴가 가로↔세로로 자연스럽게 전환.
    
2. **문제:** 작은 화면에서 메뉴 간격/폰트가 너무 촘촘
    
    **해결:** 모바일 구간에서 `.expand-412 > a { padding: 4px 0 }`, `font-size: 0.7rem`로 **터치 영역/가독성 개선**.
    
3. **문제:** 토글러와 메뉴가 큰 화면에서도 동시에 보여 깔끔하지 않음
    
    **해결(권장):** `@media (min-width: 413px) { .navbar-toggler { display: none; } }`로 **큰 화면에서 토글러 숨김**.
    
    (반대로 작은 화면에서는 부트스트랩의 collapse 기능을 그대로 활용)
    
4. **문제:** 반응형 줄바꿈이 필요
    
    **해결:** `<br class="d-412-break">` + `@media`의 `display` 전환으로 **상황별 개행 제어**.
    

---

## 4) 배운 점

- Bootstrap **프리셋 브레이크포인트와 직접 `@media`*의 역할 차이를 이해했고, **디바이스 특화 UX**를 위해 커스텀 브레이크포인트를 쓸 수 있음을 체득.
- Flexbox의 `direction`, `justify-content`, `align-items`를 **반응형 전환 포인트에서 다르게 주는 패턴**을 익힘.
- 접근성 관점에서 **hover와 focus 동시 지원**의 필요성을 확인.
- **사소한 오타(`None` vs `none`)도 즉시 UI에 영향**을 준다는 점을 재확인