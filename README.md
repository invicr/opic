# OPIC Study

정적 HTML 한 장으로 동작하는 오픽 학습 페이지 시안입니다.

## 실행

브라우저에서 `index.html`을 열거나, GitHub 저장소에 올린 뒤 GitHub Pages로 배포하면 됩니다.

## 현재 구성

- `index.html`: 학습 UI
- `themes/transportation/describe/q1/script.txt`: 현재 문항 스크립트
- `themes/transportation/describe/q1/audio.wav`: 현재 문항 오디오
- `themes/restaurant/experience/q1/script.txt`: 새로 추가된 레스토랑 문항 스크립트
- `themes/restaurant/experience/q1/audio.wav`: 새로 추가된 레스토랑 문항 오디오
- `themes/restaurant/roleplay/q1/script.txt`: 새로 추가된 레스토랑 롤플레이 문항 스크립트
- `themes/restaurant/roleplay/q1/audio.wav`: 새로 추가된 레스토랑 롤플레이 문항 오디오
- `themes/restaurant/roleplay/q2/script.txt`: 새로 추가된 레스토랑 롤플레이 문항 스크립트
- `themes/restaurant/roleplay/q2/audio.wav`: 새로 추가된 레스토랑 롤플레이 문항 오디오

## 다음 확장 방식

`index.html` 안의 `studyLibrary` 배열에 테마와 문항을 추가하면 됩니다.

문항 하나는 아래 2개 파일을 기준으로 묶습니다.

- `scriptFile`: 문제 텍스트
- `audioFile`: 반복 재생할 `wav`

현재는 아래 구조를 기준으로 관리합니다.

```text
themes/
  transportation/
    describe/
      q1/
        script.txt
        audio.wav
```

테마와 유형이 늘어나면 아래처럼 확장하면 됩니다.

```text
themes/
  transportation/
    describe/
      q1/
        script.txt
        audio.wav
      q2/
        script.txt
        audio.wav
    experience/
      q1/
        script.txt
        audio.wav
  travel/
    describe/
      q1/
        script.txt
        audio.wav
```

그 구조로 가면 `studyLibrary`의 `scriptFile`과 `audioFile` 경로만 추가해서 문항을 계속 늘릴 수 있습니다.

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
