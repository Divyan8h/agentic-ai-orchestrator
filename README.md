A deterministic multi-tool Agentic AI system with structured routing, guarded tool execution, and final answer synthesis.

This project demonstrates a structured Agentic AI workflow built using LangGraph and LangChain.

Instead of calling tools directly, the system uses:
- explicit prompt templates
- typed inputs
- conditional routing
- tool-based execution
- memory handling

The goal was not speed of implementation, but **understanding how agent decisions, prompt variables, and tool execution actually flow at runtime**.

##Why this approach (THIS is what makes it senior)
While the same functionality could be achieved using direct tool calls or higher-level abstractions,
this project intentionally builds the flow step-by-step to understand:

- how prompt variables are injected
- how chains fail when inputs are misaligned
- how tool routing decisions are made
- how agent state is maintained across turns
- how recoverable vs non-recoverable errors surface

This makes the system more debuggable, extensible, and production-aligned.


## Architecture

User Query
   ↓
ChatPromptTemplate (strict variables)
   ↓
LLM Chain
   ↓
Conditional Router (LangGraph)
   ↓
Tool Execution (if required)
   ↓
Final Response

##Key Learnings
- Prompt templates are contracts, not strings
- Missing variables break chains silently if not handled properly
- Tool execution should be routed, not assumed
- Agent memory needs explicit configuration
- Errors are part of the agent lifecycle, not exceptions to ignore

## Setup

1. Clone the repo
2. Create a `.env` file with your OpenAI/Gemini key
3. Install dependencies:
   pip install -r requirements.txt

4. Run the main script

<img width="1261" height="292" alt="project1 7" src="https://github.com/user-attachments/assets/0652bea5-c3fd-4b7b-84f0-fc09cbbdfe4f" />
