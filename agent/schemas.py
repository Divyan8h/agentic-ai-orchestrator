from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal

class RouterDecision(BaseModel):
    tool_name: Literal["read_file", "code_generator", "code_explainer", "calculator", "search", "none", "error"]
    reasoning: str
    tool_input: Optional[Dict[str, Any]] = None

class codeResult(BaseModel):
    language: str
    filname: Optional[str] = None
    code: str
    explanation: Optional[str] = None

class CalculationResult(BaseModel):
    expression: str
    result: float
    steps: Optional[List[str]] = None

class SearchResult(BaseModel):
    query: str
    results: List[str]
    source: Optional[str] = None

class FileSummary(BaseModel):
    title: str
    summary: str
    key_points: List[str]

class ErrorResponse(BaseModel):
    error_type: str
    message: str
    recoverable: bool = True
