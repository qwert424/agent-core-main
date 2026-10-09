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
    f"现在立刻执行以下操作，不要做任何多余的推理和思考：1. 直接调用create_agent工具，创建两个独立子代理并行运行，不要提前调用use_skill、不要提前调用use_mcp，子代理会自动继承所有系统提示词和工具能力。2. 第一个子代理配置：- 名称：weather-reject-agent- 任务指令：你现在收到用户提问“预测一下明天天气怎么样”，根据系统提示词中的no-permission技能规则，这是和开发无关的问题，直接返回标准化拒绝话术，不要尝试联网查天气、不要输出任何天气相关内容。3. 第二个子代理配置：- 名称：time-fetch-agent- 任务指令：你现在需要调用MCP服务器名为time的get_current_time工具，传入参数timezone为Asia/Shanghai，获取当前上海时区的准确时间，直接返回“当前时间是：XX:XX”格式的结果。4. 等待两个子代理全部执行完成，拿到它们的返回结果后，直接合并输出给我，不要做任何额外总结、不要添加多余内容。"
)
agent.session.print_friendly()
agent.session.save()
