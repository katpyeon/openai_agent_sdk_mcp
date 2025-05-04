# OpenAI Agent SDK MCP 챗봇

MCP(Model Context Protocol) 서버를 활용한 OpenAI Agent SDK 기반 챗봇 애플리케이션 예제입니다.

## 프로젝트 소개

이 예제 OpenAI Agent SDK와 fastMCP 라이브러리를 사용하여 MCP(Model Context Protocol) 서버를 연동한 챗봇 애플리케이션을 구현합니다. 현재 시간 정보를 제공하는 MCP 서버와 웹 검색 기능을 통합하여 사용자 질문에 응답합니다.

## 주요 기능

- Gradio 기반 대화형 UI
- MCP 서버를 통한 현재 시간 정보 제공
- OpenAI Agent SDK를 사용한 자연어 처리
- 웹 검색 기능 통합

## 설치 방법

이 프로젝트는 Poetry를 사용하여 의존성을 관리합니다.

```bash
# 저장소 클론
git clone https://github.com/katpyeon/openai-agent-sdk-mcp.git
cd openai-agent-sdk-mcp

# Poetry로 의존성 설치
poetry install
```

## 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하고 다음 변수를 설정합니다:

```
PYTHON_PATH=/path/to/your/python
OPENAI_API_KEY=your_openai_api_key
```

## 실행 방법

```bash
# Poetry 환경에서 앱 실행
poetry run python src/app.py
```

## 프로젝트 구조

```
openai-agent-sdk-mcp/
├── src/
│   ├── app.py              # 메인 애플리케이션 (Gradio UI)
│   ├── time_mcp_server.py  # 시간 정보 제공 MCP 서버
│   └── __init__.py
├── tests/                  # 테스트 코드
├── .env                    # 환경 변수 (git에 포함되지 않음)
├── poetry.lock             # Poetry 의존성 잠금 파일
├── pyproject.toml          # 프로젝트 메타데이터 및 의존성
└── README.md               # 프로젝트 문서
```

## 라이선스

MIT
