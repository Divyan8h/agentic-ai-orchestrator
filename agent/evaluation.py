from .router import route_user_query
from .schemas import RouterDecision

# Example evaluation cases
EVAL_CASES = [
    {
        "input": "Write a Python function to check palindrome",
        "expected_tool": "code_generator"
    },
    {
        "input": "Explain this code: def add(a,b): return a+b",
        "expected_tool": "code_explainer"
    },
    {
        "input": "What is 15 * (4 + 6)?",
        "expected_tool": "calculator"
    },
    {
        "input": "Hello, how are you?",
        "expected_tool": "none"
    }
]

def evaluate_router(provider="groq"):
    """
    Evaluates router accuracy based on EVAL_CASES
    """
    correct = 0
    for case in EVAL_CASES:
        decision: RouterDecision = route_user_query(case["input"], provider)
        if decision.tool_name == case["expected_tool"]:
            correct += 1
    accuracy = correct / len(EVAL_CASES)
    return {
        "router_accuracy": accuracy,
        "total_cases": len(EVAL_CASES)
    }

if __name__ == "__main__":
    result = evaluate_router()
    print(f"Router Accuracy: {result['router_accuracy']*100}% ({result['total_cases']} cases)")
