# mcp_server.py - FastMCP 기반 구현
import datetime
from fastmcp import FastMCP
from typing import List
# FastMCP 서버 인스턴스 생성
mcp = FastMCP("Joke MCP Server")


# 시간 제공 도구 등록
@mcp.tool()
def getTime() -> List[str]:
    """현재 시간을 반환합니다"""    
    current_time = datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")        
    return [current_time]

# 메인 함수
def main():    
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()