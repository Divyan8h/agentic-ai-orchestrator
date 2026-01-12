# agent/router.py
from pydantic import BaseModel
from typing import Literal, Optional, Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from agent.llm import get_llm

class RouterDecision(BaseModel):
    tool_name: Literal[
        "search",
        "code_generator",
        "code_explainer",
        "read_file",
        "calculator",
        "none"
    ]
    reasoning: str
    tool_input: Optional[Dict[str, Any]] = None


router_prompt = ChatPromptTemplate.from_messages([
    ("system",
     """
You are an intelligent routing agent.

IMPORTANT:
- You MUST ensure tool_input keys exactly match the target tool's function parameters.

Tool contracts:
- code_generator → {{ "task": str }}
- code_explainer → {{ "code": str }}
- search → {{ "query": str }}
- read_file → {{ "path": str }}
- calculator → {{ "expression": str }}
- none → tool_input = null

Return ONLY valid JSON:
{{
  "tool_name": "<tool_name>",
  "reasoning": "<short reason>",
  "tool_input": {{ }}
}}
"""),
    ("human", "{user_input}")
])


def route_user_query(user_input: str) -> RouterDecision:
    llm = get_llm()
    structured_llm = llm.with_structured_output(RouterDecision)
    return (router_prompt | structured_llm).invoke({"user_input": user_input})
