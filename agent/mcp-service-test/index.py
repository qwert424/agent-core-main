from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Weather Service",
    json_response=True,
)


@mcp.tool()
async def get_weather(city: str = "成都") -> dict[str, str]:
    """Get weather data for a city"""
    return {
        "city": city,
        "temperature": "22",
        "condition": "多云",
        "humidity": "65%",
    }


# mcp库底层使用 starlette + uvicorn 启动 http 服务
mcp.run(transport="streamable-http")
