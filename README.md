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

<img width="1916" height="890" alt="image" src="https://github.com/user-attachments/assets/2e8ecc97-cc43-4a2e-8e89-01d975a521e8" />

<img width="1919" height="536" alt="image" src="https://github.com/user-attachments/assets/8d21718d-f3d1-407e-958c-d7e95302e6ad" />

<img width="1584" height="859" alt="image" src="https://github.com/user-attachments/assets/982fb788-6aa5-45a1-bccf-de9c1bcd0093" />

<img width="1545" height="891" alt="image" src="https://github.com/user-attachments/assets/102bb9d2-3a23-4181-8efc-8caa60439fa0" />

<img width="1517" height="860" alt="image" src="https://github.com/user-attachments/assets/46ff6c2f-f7e3-495c-a4cb-52b7331dec39" />

<img width="1546" height="897" alt="image" src="https://github.com/user-attachments/assets/e8705d8f-f716-4284-9e38-4654ec78e5bd" />






