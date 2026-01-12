import ast, operator
from agent.schemas import CalculationResult

OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}

def _evaluate(node, steps):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left, steps)
        right = _evaluate(node.right, steps)
        result = OPS[type(node.op)](left, right)
        steps.append(f"{left} {type(node.op).__name__} {right} = {result}")
        return result
    raise ValueError("Invalid expression")

def execute_calculator(expression: str, show_steps: bool = True) -> CalculationResult:
    tree = ast.parse(expression, mode="eval")
    steps = []
    result = _evaluate(tree.body, steps)
    return CalculationResult(expression=expression, result=float(result), steps=steps if show_steps else None)
