# ChatDB - RDS Database Chat App

ChatDB - an RDS Database Chat App is a Streamlit-based application that allows you to connect and communicate with any database. You can run this app using Docker for easy deployment. With this app, you can start a conversation with your database and retrieve information as needed.

## Docker Setup

To run the app in a Docker container, follow these instructions:

1. Make sure you have Docker installed on your system.

2. Clone the repo to your local machine and navigate to the app directory by running the following commands:

   ```shell
   git clone https://github.com/chatdbtech/chatdb.git
   cd rds-database-chat-app

   ```

3. Build the Docker image by running the following command in the same directory as your Dockerfile:

```shell

docker build -t rds-chat-app .

```

4. Once the image is built, you can run the container using the following command:

```shell

docker run -p 8501:8501 rds-chat-app

```

This will start the app inside a Docker container and expose it on port 8501.

## Environment Configuration

1. Create a `.env` file in the root directory of the app if it doesn't already exist.

2. Open the `.env` file and add the following line with your OpenAI API key:

   ```shell
   OPENAI_API_KEY=your-openai-key
   ```

## Using ChatDB

ChatDB is designed to connect to your database and allow you to communicate with it. Here are the steps to get started:

### Instructions

1. Enter the URI of your RDS Database in the text box provided.

2. Click the **Start Chat** button to initiate the chat with your database.

3. Enter your message in the text box below and press **Enter** to send the message to the API.

### Chat with the API

- Enter your message in the chat input box, and the app will display the response from your database. You can have a conversation with the database by entering messages and receiving replies.

### Contact Us

If you have any questions, comments, or suggestions about this app or Streamlit in general, please feel free to [contact Us](https://www.streamlit.io/contact-us).

Enjoy using the ChatDB to interact with your database through a user-friendly interface!
