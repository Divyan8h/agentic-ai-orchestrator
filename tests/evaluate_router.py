from agent.evaluation import evaluate_router

def test_router():
    result = evaluate_router()
    accuracy = result["router_accuracy"]
    total = result["total_cases"]
    assert accuracy >= 0.75, f"Router accuracy too low: {accuracy*100}%"
    print(f"Router passed with {accuracy*100}% accuracy over {total} cases")

if __name__ == "__main__":
    test_router()
