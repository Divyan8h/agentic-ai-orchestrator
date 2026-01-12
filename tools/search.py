from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
from agent.schemas import SearchResult, ErrorResponse

wiki_app = WikipediaAPIWrapper(top_k_results=2)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_app)

def search_web(query: str) -> SearchResult | ErrorResponse:
    try:
        raw = wiki_tool.run(query)

        return SearchResult(
            query=query,
            results=[raw],
            source="Wikipedia"
        )
    except Exception as e:
        return ErrorResponse(error_type="SEARCH_ERROR", message=str(e), recoverable=True)
