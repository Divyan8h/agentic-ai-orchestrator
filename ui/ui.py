import streamlit as st
from agent.orchestrator import agent_handle
import time

st.set_page_config(
    page_title="Agentic AI System",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic AI")
st.caption("Deterministic multi-tool AI agent with structured reasoning")

#if "history" not in st.session_state:
    #st.session_state.history = []

#user_input = st.text_input("Ask something")

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align:center;'>🤖 Agentic AI</h1>
<p style='text-align:center; color: #9CA3AF;'>
Deterministic multi-tool AI agent with intelligent routing
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- INPUT ----------
query = st.text_input(
    "Ask anything"
)

run = st.button("🚀 Run Agent")

# ---------- EXECUTION ----------
if run and query:
    with st.spinner("Agent is reasoning..."):
        response = agent_handle(query, thread_id="ui")

    st.markdown("---")

    # ✅ CASE 1: Normal answer
    if isinstance(response, dict) and "answer" in response:
        st.markdown("""
        <div style="
            background-color:#161B22;
            padding:22px;
            border-radius:14px;
            border:1px solid #30363D;
        ">
        <h3 style="margin-bottom:10px;">✅ Answer</h3>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"<p style='font-size:17px; line-height:1.6;'>{response['answer']}</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<span style='color:#9CA3AF;'>🛠 Tool used:</span> "
            f"<code>{response.get('tool_used','')}</code>",
            unsafe_allow_html=True
        )

    # ❌ CASE 2: Error
    elif isinstance(response, dict) and "error" in response:
        st.error(response["error"])

    else:
        st.error("Unexpected response format")


#for q, a in reversed(st.session_state.history):
    #st.markdown(f"**You:** {q}")
    #if isinstance(a, dict):
        #st.json(a)
    #else:
        #st.markdown(f"**Agent:** {a}")

#if isinstance(response, dict) and "results" in response:
    #for r in response["results"]:
        #st.write(r)

