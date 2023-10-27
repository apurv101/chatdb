import streamlit as st
import requests
from querying import save_db_details, complete_process
import os

# Define the folder names
folders_to_create = ['csvs', 'vectors']

# Check and create folders if they don't exist
for folder_name in folders_to_create:
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")


# Function to call the API with the provided URI
def call_api(uri):
    unique_id = save_db_details(uri)
    st.session_state.unique_id = unique_id
    st.session_state.db_uri = uri
    return {"message": "Connection established to Database!"}



    

# Function to call the API with the provided URI and user message
def call_api_with_message(message):
    unique_id = st.session_state.unique_id
    db_uri = st.session_state.db_uri
    print(message, unique_id, db_uri)
    result = complete_process(message, unique_id, db_uri)
    return {"message": str(result)}


# Streamlit app
st.title("ChatDB - RDS Database Chat App")

## Contact us button at top right
st.sidebar.subheader("Contact Us")
st.sidebar.markdown(
    """
    [ChatDB](https://github.com/chatdbtech/chatdb) is an open-source app to chat with any Relational Database System. 
    If you have any questions, comments, or suggestions, please reach out to us at info@chatdb.tech. 

    If your database is not accessible publicly, for example, if it is running on localhost or within a virtual private network, you can still use ChatDB by following the instructions in the [GitHub repository](https://github.com/chatdbtech/chatdb).
    """
)

# Initialize the chat history list
chat_history = []





# ## Instructions
st.subheader("Instructions")
st.markdown(
    """
    1. Enter the URI of your RDS Database in the text box below.
    2. Click the **Start Chat** button to start the chat.
    3. Enter your message in the text box below and press **Enter** to send the message to the API.
    """
)


# Input for the database URI
uri = st.text_input("Enter the RDS Database URI")

if st.button("Start Chat"):
    if not uri:
        st.warning("Please enter a valid database URI.")
    else:
        st.info("Connecting to the API and starting the chat...")
        chat_response = call_api(uri)
        if "error" in chat_response:
            st.error("Error: Failed to start the chat. Please check the URI and try again.")
        else:
            st.success("Chat started successfully!")

# Chat with the API (a mock example)
st.subheader("Chat with the API")


# Text Input for User Messages
# user_message = st.text_input("Your Message")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # response = f"Echo: {prompt}"
    response = call_api_with_message(prompt)["message"]
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})






# Run the Streamlit app
if __name__ == "__main__":
    st.write("This is a simple Streamlit app for starting a chat with an RDS Database.")
