from .schemas import RouterDecision
from tools.calculator import execute_calculator
from tools.code_generator import generate_code
from tools.code_explainer import explain_code
from tools.file_reader import read_file
from tools.search import search_web
import time
import signal

TOOL_REGISTRY = {
    "calculator": execute_calculator,
    "code_generator": generate_code,
    "code_explainer": explain_code,
    "read_file": read_file,
    "search": search_web,
}

class ToolExecutionError(Exception):
    pass

def execute_with_guard(func, retries=1, timeout=5, **kwargs):
    start_time = time.time()
    last_error = None
    for _ in range(retries+1):
        try:
            if time.time() - start_time > timeout:
                raise TimeoutError("Tool execution timed out")
            return func(**kwargs)
        except Exception as e:
            last_error = e
    raise ToolExecutionError(str(last_error))

def dispatch_tools(decision: RouterDecision):
    if decision.tool_name in ("none", "error"):
        return {"message": decision.reasoning}
    executor = TOOL_REGISTRY.get(decision.tool_name)
    if not executor:
        return {"error": f"Tool '{decision.tool_name}' not registered"}
    return execute_with_guard(executor, **(decision.tool_input or {}))
