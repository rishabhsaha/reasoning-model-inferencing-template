import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ToolSet, CodeInterpreterTool, BingGroundingTool
from azure.identity import DefaultAzureCredential
from agents import deli_lead


def call_api(prompt):
    """
    Calls the API with the given prompt and returns the response.
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = deli_lead(prompt, st.session_state["markdown_content"])

        response = st.write_stream(stream)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})


st.title("Agent Fresh")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
if "markdown_content" not in st.session_state:
    # Load the Markdown file into session state
    with open("../reasoning/output/reasoningmodeloutput.md", "r", encoding="utf-8") as file:
        st.session_state["markdown_content"] = file.read()

# Display the Markdown content
# st.markdown(st.session_state["markdown_content"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4.1"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# st.markdown(deli_lead("Hello, how can I assist you today?"))

if prompt := st.chat_input("What is up?"):
    call_api(prompt)

if st.sidebar.button("Deli Lead"):
    prompt = "As a Deli Lead, how do you manage your team effectively?"
    call_api(prompt)


if st.sidebar.button("Deli Associate"):
    prompt = "As a Deli Associate, I need to know the Fresh Production Plan in tabular format and 2 to 3 bullet points that would help me execute that plan appropriately?"
    call_api(prompt)


if st.sidebar.button("Deli Coach"):
    prompt = "As a Deli Coach, I need to know the Fresh Production Plan and 2 to 3 bullet points that would help me understand how the rotissery chicken pruduction has performed yesterday and what my agenda should be when I do my walkthrough and handover at shift end?"
    call_api(prompt)
