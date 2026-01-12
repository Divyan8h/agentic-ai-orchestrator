from agent.llm import get_llm

def synthesize_answer(user_input: str, tool_output: dict) -> str:
    llm = get_llm()

    prompt = f"""
You are a confident, expert AI assistant.

Answer the user's question clearly and concisely.
Do NOT mention tools, sources, or internal steps.

User question:
{user_input}

Context:
{tool_output}

Answer like a human expert.
"""

    return llm.invoke(prompt).content.strip()
