from agent.schemas import codeResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from agent.llm import get_llm


code_parser = PydanticOutputParser(pydantic_object=codeResult)

code_explainer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior software engineer. Explain the code in clear concise steps. {format_instructions}"
    ),
    ("human", "{code}")
]).partial(format_instructions=code_parser.get_format_instructions())

def explain_code(code: str, provider: str = "groq") -> codeResult:
    llm = get_llm()
    chain = code_explainer_prompt | llm | code_parser
    return chain.invoke({"code": code})
