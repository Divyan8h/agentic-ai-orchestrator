from agent.schemas import codeResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from agent.llm import get_llm

code_parser = PydanticOutputParser(pydantic_object=codeResult)

code_generator_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior software engineer. {format_instructions} "
        "Rules: Only return valid structured output, no markdown fences, minimal correct code."
    ),
    ("human", "Language: {language}\nTask: {task}")
]).partial(format_instructions="{format_instructions}")


def generate_code(task: str, language: str = "Python", provider: str = "gemini") -> codeResult:
    """
    Generate code using LLM.
    Returns structured codeResult.
    """
    llm = get_llm()

    structured_llm = llm.with_structured_output(codeResult)

    # ✅ Prompt → LLM → structured output
    chain = code_generator_prompt | structured_llm

    return chain.invoke({"task": task, "language": language})
