import subprocess
import shlex
from sys import platform
from agent.tool.core import tool

# 定义最大输出长度，防止返回过大内容
MAX_OUTPUT_LENGTH = 10000


def truncate_output(text: str) -> str:
    """截断过长的输出"""
    if len(text) > MAX_OUTPUT_LENGTH:
        return text[:MAX_OUTPUT_LENGTH] + "\n... (输出被截断)"
    return text


@tool(command="要执行的 bash/shell 命令")
def bash_command(command: str) -> str:
    """
    执行 bash/shell 命令，返回命令输出结果。
    注意：此工具存在安全风险，仅应在受信任环境中使用。
    """
    # 1. 基本输入验证（可选但推荐）
    if not command or not command.strip():
        return "错误：命令不能为空"

    # 2. 确定 shell 可执行文件
    if platform == "win32":
        # Windows 下使用 cmd.exe
        # 注意：shell=True 时，Windows 默认使用 COMSPEC 环境变量指定的 shell (通常是 cmd.exe)
        # 显式指定 executable 时，必须使用 'cmd.exe' 而非 'cmd'
        shell_executable = "cmd.exe"
        # Windows 下 command 可能需要特殊处理，但 subprocess 通常能处理
    else:
        # Unix/Linux/macOS 下使用 /bin/bash
        shell_executable = "/bin/bash"

    try:
        # 3. 执行命令
        result = subprocess.run(
            command,
            shell=True,  # 允许使用 shell 特性（如管道、变量展开）
            executable=shell_executable,
            capture_output=True,
            text=True,
            timeout=30,  # 30秒超时
            # 建议添加以下参数以增强安全性（如果环境支持）：
            # preexec_fn=os.setsid  # Unix: 创建新会话，防止子进程继承信号
        )

        # 4. 处理输出
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # 合并输出，优先显示 stderr 如果有错误
        if result.returncode != 0:
            error_msg = stderr if stderr else stdout
            truncated_error = truncate_output(error_msg)
            return f"[退出码 {result.returncode}]\n{truncated_error}"
        else:
            # 即使返回码为0，也可能有 stderr 输出（警告信息）
            output = stdout if stdout else stderr
            if not output:
                return "(命令执行成功，无输出)"
            return truncate_output(output)

    except subprocess.TimeoutExpired:
        return "[错误] 命令执行超时（超过30秒）"
    except FileNotFoundError:
        return f"[错误] 找不到指定的 shell 解释器: {shell_executable}"
    except Exception as e:
        return f"[错误] 执行命令时发生异常: {str(e)}"
