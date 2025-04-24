import streamlit as st
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ToolSet, CodeInterpreterTool, BingGroundingTool
from azure.identity import DefaultAzureCredential
from agents import deli_lead, deli_associate, deli_coach

st.title("ChatGPT-like clone")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
if "markdown_content" not in st.session_state:
    # Load the Markdown file into session state
    with open("../MarkDown_5260.md", "r", encoding="utf-8") as file:
        st.session_state["markdown_content"] = file.read()

# Display the Markdown content
# st.markdown(st.session_state["markdown_content"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # stream = client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # )
        # response = st.write_stream(stream)
        response = deli_lead(prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

if st.sidebar.button("Deli Lead"):
    prompt = "As a Deli Lead, how do you manage your team effectively?"
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # stream = client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # )
        # response = st.write_stream(stream)
        response = deli_lead(prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

if st.sidebar.button("Deli Associate"):
    prompt = "As a Deli Associate, I need to know the Fresh Production Plan and 2 to 3 bullet points that would help me execute that plan appropriately?"
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # stream = client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # )
        # response = st.write_stream(stream)
        response = deli_lead(prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

if st.sidebar.button("Deli Coach"):
    prompt = "As a Deli Coach, I need to know the Fresh Production Plan and 2 to 3 bullet points that would help me understand how the rotissery chicken pruduction has performed yesterday and what my agenda should be when I do my walkthrough and handover at shift end?"
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # stream = client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # )
        # response = st.write_stream(stream)
        response = deli_lead(prompt)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
