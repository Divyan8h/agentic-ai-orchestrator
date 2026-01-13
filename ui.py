# ui.py
import streamlit as st
from agent.orchestrator import agent_handle


def render_ui():
    st.set_page_config(
        page_title="Agentic AI System",
        page_icon="🤖",
        layout="centered"
    )

    # ---------- HEADER ----------
    st.markdown("""
    <h1 style='text-align:center;'>🤖 Agentic AI</h1>
    <p style='text-align:center; color: #9CA3AF;'>
    Deterministic multi-tool AI agent with intelligent routing
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- INPUT ----------
    query = st.text_input("Ask anything")
    run = st.button("🚀 Run Agent")

    # ---------- EXECUTION ----------
    if run:
        if not query.strip():
            st.warning("Please enter a query!")
            return

        with st.spinner("Agent is reasoning..."):
            response = agent_handle(query, thread_id="ui")

        st.markdown("---")

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

        elif isinstance(response, dict) and "error" in response:
            st.error(response["error"])
        else:
            st.error("Unexpected response format")
