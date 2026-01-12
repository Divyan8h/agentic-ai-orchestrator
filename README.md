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

<img width="1918" height="907" alt="Project1 1" src="https://github.com/user-attachments/assets/96604ee5-9ab2-4bf7-9c51-71ae2e5c22bc" />
<img width="1918" height="727" alt="project1 2" src="https://github.com/user-attachments/assets/24bd5e43-5fbf-427b-933b-32058dc2fc3c" />
<img width="1918" height="861" alt="project1 3" src="https://github.com/user-attachments/assets/7794641b-1cc2-437f-9a73-fb87a5e395a5" />
<img width="1918" height="752" alt="project1 4" src="https://github.com/user-attachments/assets/3a5640d1-eee2-4ccf-b972-47895f633d69" />
<img width="1918" height="541" alt="project1 5" src="https://github.com/user-attachments/assets/50aeffa9-85f6-415a-9577-88701fcc7383" />




