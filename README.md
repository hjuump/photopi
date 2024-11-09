# 📸 Photo Pi

**Photo Pi**는 라즈베리 파이를 활용한 스마트 포토 부스 시스템입니다.  
사용자의 입장을 감지하고, 부스 내부의 환경을 최적화하며, 간단한 인터페이스로 사진을 촬영할 수 있도록 설계되었습니다.

## 📝 소개

Photo Pi는 초음파 센서를 이용해 사용자의 입장을 자동으로 감지하고, 조도 및 온습도 센서를 통해 부스 환경을 쾌적하게 유지합니다. 사용자는 버튼을 이용해 촬영할 사진 매수를 선택하고, 카메라로 촬영한 사진을 웹 브라우저에서 확인할 수 있습니다.

### 주요 기능
- 🕵️‍♂️ 초음파 센서를 통해 사용자 입장 자동 감지
- 💡 LED와 센서를 활용한 부스 내부 환경 조절
- 🎛 스위치 입력으로 사진 촬영 매수 및 재촬영 여부 선택
- ⏳ 카운트다운 후 자동 촬영 및 결과 확인
- 🌐 웹 브라우저를 통한 직관적인 UI 제공

## 🎬 화면 구성

- 초기 화면
  - 사용자가 부스 앞에 다가가면 입장을 감지합니다.

- 촬영 매수 선택 화면
  - 스위치를 사용해 촬영할 사진 매수를 선택합니다.

- 사진 촬영 화면
  - 카운트다운 후 카메라가 자동으로 사진을 촬영합니다.

- 결과 화면
  - 촬영된 사진을 확인하고 재촬영 여부를 선택합니다.

## ⚙ 기술 스택

### Hardware
- **라즈베리 파이**: 프로젝트 메인 컨트롤러
- **카메라 모듈**: 사진 촬영
- **초음파 센서**: 사용자 입장 감지
- **LED**: 부스 내부 조도 조절
- **HTU21D** 센서: 부스 내부 온습도 측정
- **조도 센서**: 주변 밝기를 측정하여 부스 환경을 조정
- **스위치**: 사진 매수 선택 및 재촬영 여부 입력

### Back-end
- Python
- Flask

### Front-end
- HTML
- CSS

### Tools
- GitHub
- Notion

## 👩‍💻 제작
- 한성대학교 컴퓨터공학부 22학번 조현주