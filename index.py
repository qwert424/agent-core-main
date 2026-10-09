# from agent.agent import Agent
# from agent.printer import ModelPrinterListener

# listener = ModelPrinterListener()
# agent = Agent(model_listener=listener)

# agent.invoke("最近天气如何？注意")
# agent.session.print_friendly()
# import asyncio

# from mcp import StdioServerParameters
# from mcp.client.stdio import stdio_client
# from mcp import ClientSession

# server_params = StdioServerParameters(command="uvx", args=["mcp-server-time"])


# async def main():
#     async with stdio_client(server_params) as (read, write):
#         async with ClientSession(read, write) as session:
#             # 初始化
#             await session.initialize()

#             # tools/call
#             tools = await session.call_tool(
#                 name="get_current_time", arguments={"timezone": "Asia/shanghai"}
#             )
#             print(tools.model_dump_json(indent=2, ensure_ascii=False))


# asyncio.run(main())
# from mcp.client.streamable_http import streamable_http_client
# from mcp import ClientSession


# async def main():

#     async with streamable_http_client("https://learn.microsoft.com/api/mcp") as (
#         read_stream,
#         write_stream,
#         _,
#     ):
#         async with ClientSession(read_stream, write_stream) as session:
#             # initialize
#             await session.initialize()  # http请求1

#             # tools/list
#             tools = await session.list_tools()  # http请求2
#             print(tools.model_dump_json(indent=2, ensure_ascii=False))


# asyncio.run(main())
from agent.agent import Agent
from agent.printer import ModelPrinterListener

listener = ModelPrinterListener()
agent = Agent(model_listener=listener)
agent.invoke(
    "开启两个子线程 分别进行 1子线程回答预测一下明天天气怎么样（注意skill提示用agent-test\agent\.agents\skills\no-permission拒绝了这个回答 ） 2子线程 去调用获取当前时间的工具（用mcp） 然后告诉我现在几点 "
)
agent.session.print_friendly()
agent.session.save()
