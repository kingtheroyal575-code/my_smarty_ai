import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType

# 1. Page Setup
st.set_page_config(page_title="Krishna AI")
st.title("🤖 Krishna's AI Agent")

# 2. Sidebar for API Key (Suraksha ke liye)
api_key = st.sidebar.text_input(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 type="trk67ytk")

if api_key:
    os.environ["GROQ_API_KEY"] = api_key
    try:
        # AI aur Search Tool setup
        llm = ChatGroq(model_name="llama3-8b-8192")
        tools = [DuckDuckGoSearchRun()]
        agent = initialize_agent(
            tools, 
            llm, 
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
            verbose=True, 
            handle_parsing_errors=True
        )

        # 3. Chat Interface
        query = st.text_input("Apna sawal likhein:")
        if st.button("Puchiye"):
            if query:
                with st.spinner("Internet se dhoond raha hoon..."):
                    answer = agent.run(query)
                    st.success(answer)
            else:
                st.warning("Pehle kuch sawal toh likhiye!")
    except Exception as e:
        st.error(f"Dikat aayi: {e}")
else:
    st.info("AI use karne ke liye pehle Left side (Sidebar) mein apni API Key daalein.")
