import asyncio
import sys
from agents import Agent, Runner, WebSearchTool
from agents.mcp.server import MCPServerStdio
import gradio as gr
from typing import List, Dict, Any, Tuple
import os
from dotenv import load_dotenv

load_dotenv()
PYTHON_PATH = os.getenv("PYTHON_PATH")

# 환경변수가 없으면 기본값 사용
if not PYTHON_PATH:
    PYTHON_PATH = "/Users/yeonghyeonchoi/Library/Caches/pypoetry/virtualenvs/openai-agent-sdk-mcp-7IHQsKXF-py3.12/bin/python"
    print(f"환경변수 없음, 기본값 사용: {PYTHON_PATH}", file=sys.stderr)

async def chat_with_agent(message: str, history: List[List[str]]) -> List[List[str]]:
    async with MCPServerStdio(
        params={
            "command": PYTHON_PATH,
            "args": ["src/time_mcp_server.py"],
        },
        cache_tools_list=True
    ) as mcp_server:
        # 도구 확인
        tools = await mcp_server.list_tools()
        print(f"🔧 MCP 도구: {[tool.name for tool in tools]}", file=sys.stderr)

        # Agent 정의
        agent = Agent(
            model="gpt-4o-mini",
            name="OpenAI Agent",
            instructions="간결하게 답변하세요. 웹서치 도구를 사용하세요. 시간을 물어보면 MCP 도구를 사용하세요.",
            tools=[WebSearchTool()],
            mcp_servers=[mcp_server],
        )

        # 대화 기록 준비
        agent_history = []
        for h in history:
            agent_history.append({"role": "user", "content": h[0]})
            agent_history.append({"role": "assistant", "content": h[1]})
        
        # 현재 메시지 추가
        agent_history.append({"role": "user", "content": message})
        
        # 자연어 입력 → 도구 호출
        result = await Runner.run(agent, agent_history)
        print(f"🧠 최종 응답: {result.final_output}", file=sys.stderr)
        
        # 응답 반환
        return history + [[message, result.final_output]]

async def main():
    # Gradio UI 생성
    with gr.Blocks() as demo:
        gr.Markdown("# MCP 챗봇")
        
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="메시지를 입력하세요...", label="입력")
        clear = gr.Button("대화 초기화")
        
        # 이벤트 연결
        msg.submit(chat_with_agent, [msg, chatbot], [chatbot], queue=True).then(
            lambda: "", None, [msg]
        )
        clear.click(lambda: [], None, [chatbot])
    
    # 서버 실행
    demo.queue()
    await demo.launch(share=False)

if __name__ == "__main__":
    asyncio.run(main())