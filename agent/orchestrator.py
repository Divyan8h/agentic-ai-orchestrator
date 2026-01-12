from .dispatcher import dispatch_tools
from .router import route_user_query
from .schemas import RouterDecision, ErrorResponse
from .synthesizer import synthesize_answer
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("agent")

def agent_handle(user_input, thread_id=None):
    try:
        # Step 1: Get routing decision
        decision: RouterDecision = route_user_query(user_input)

        # Step 2: Execute tool
        result = dispatch_tools(decision)

        final_answer = synthesize_answer(
            user_input=user_input,
            tool_output=result
        )

        return {
            "answer": final_answer,
            "tool_used": decision.tool_name
        }

    except Exception as e:
        logger.critical({"event": "system_failure", "error": str(e)})
        # ⚠️ Return structured JSON, NOT plain string
        return {"error_type": "system_failure", "message": str(e), "recoverable": True}
