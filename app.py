import streamlit as st
from agent.orchestrator import agent_handle

st.set_page_config(page_title="Agentic AI", layout="wide")

st.title("Agentic AI - Multi-Tool LLM Agent")
st.markdown("Enter your query below, and the agent will pick the right tool automatically!")

thread_id = "default_thread"  # simple single-thread for now
user_input = st.text_area("Your Query", "")

if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter a query!")
    else:
        with st.spinner("Processing..."):
            output = agent_handle(user_input, thread_id)
            st.subheader("Output")
            st.json(output)
