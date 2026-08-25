# OPIC Study

오픽 음악 주제 스크립트와 음성 파일 모음입니다.

## 현재 구성

- `index.html`: 음악 6문항 학습 페이지
- `script.txt`: 음악 관련 질문 6개와 답변 스크립트 원본
- `themes/self-introduction/regular/q1/`: 자기소개
- `themes/park/describe/q1/`: 공원 묘사
- `themes/park/experience/q1/`: 최근 공원 방문
- `themes/park/compare/q1/`: 아이들, 어른들 공원 비교
- `themes/park/issue/q1/`: 공원 문제
- `themes/park/experience/q2/`: 기억에 남는 공원
- `themes/movie/describe/q1/`: 좋아하는 장르, 좋아하는 배우 묘사
- `themes/movie/regular/q1/`: 영화관 갈때 루틴
- `themes/movie/experience/q1/`: 영화 취향 변화
- `themes/movie/experience/q2/`: 가장 흥미롭게 본 영화
- `themes/movie/compare/q1/`: 영화 변화 비교
- `themes/movie/issue/q1/`: 영화에 대한 이슈
- `themes/cafe/regular/q1/`: 보통 언제 카페가? 뭐 주문해? 거기서 뭐해?
- `themes/cafe/describe/q1/`: 너가 제일 좋아하는 카페 묘사해봐
- `themes/cafe/experience/q1/`: 카페 처음간 경험
- `themes/cafe/compare/q1/`: 카페 변화
- `themes/cafe/experience/q2/`: 카페 기억나는 경험
- `themes/home/describe/q1/`: 집 묘사하기
- `themes/home/regular/q1/`: 집 일상 루틴
- `themes/home/compare/q1/`: 집 옛날/현재 비교
- `themes/home/experience/q1/`: 집 문제
- `themes/home/chores/q1/`: 집안일 루틴
- `themes/home/chores/q2/`: 하지못한 집안일
- `themes/home/chores/q3/`: 어렸을때 집안일
- `themes/home/issue/q1/`: 한국의 집 이슈
- `themes/cooking/describe/q1/`: 요리하기 좋아하는 음식
- `themes/cooking/experience/q1/`: 최근에 한 요리
- `themes/cooking/experience/q2/`: 요리하다 망한 경험
- `themes/music/describe/q1/`: 좋아하는 음악/가수 묘사
- `themes/music/regular/q1/`: 음악 언제들어
- `themes/music/experience/q1/`: 음악 취향 변화
- `themes/music/experience/q2/`: 기억나는 콘서트
- `themes/music/compare/q1/`: 두 장르간 비교
- `themes/music/regular/q2/`: 음악 가젯/도구

각 문항 폴더는 `script.txt`와 `audio.wav`를 포함합니다.
`script.txt`는 첫 줄에 질문 제목을 두고, 그 아래는 영어 문장과 영어 어순 한국어 해석을 `EN:` / `KR:`로 짝지어 작성합니다.

```text
질문 제목
EN: Well... / I listen to music / on my phone.
KR: 음... / 나는 음악을 듣는다 / 내 휴대폰으로.
```

## 테마 추가 방식

새 테마는 아래처럼 `themes/{theme}/{type}/q{number}/` 구조로 추가합니다.

```text
themes/
  music/
    describe/q1/script.txt
    describe/q1/audio.wav
  travel/
    experience/q1/script.txt
    experience/q1/audio.wav
```

`index.html`의 `studyLibrary` 배열에 테마와 문항의 `scriptFile`, `audioFile` 경로를 추가하면 상단에 테마 탭과 문항 탭이 자동으로 표시됩니다.

## 듣기 기능

- `테마 전체 듣기`: 현재 선택한 테마의 문항 오디오를 위에서 아래 순서대로 재생합니다.
- `전체 반복`: 테마의 마지막 문항까지 재생한 뒤 다시 첫 문항부터 반복합니다.
- `문항 반복`: 각 문항 카드에서 해당 오디오만 반복 재생합니다.

## Google AI Studio Prompt

### Scene

OPIc speaking practice for a beginner English learner.  
The speaker is answering an OPIc question naturally, but at a very slow learner-friendly pace for shadowing practice.

### Sample Context

Read this very slowly and clearly for pronunciation shadowing practice.

Speak at about 80-90% of normal conversational speed.  
Use long pauses between sentences (1-2 seconds).  
Pause naturally within long sentences by phrase chunks so I can repeat after each chunk.  
Pronounce every word clearly and do not reduce sounds too much.  
Use a warm, calm conversational voice.

### Important

- Much slower than normal conversation
- Slower than typical audiobook narration
- One thought group at a time
- Leave enough silence for repetition practice
