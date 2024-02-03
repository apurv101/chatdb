# [ChatDB](http://chatdb.tech/) - RDS Database Chat App

[ChatDB](http://chatdb.tech/) - an RDS Database Chat App is a Streamlit-based application that allows you to connect and communicate with any database. You can run this app using Docker for easy deployment. With this app, you can start a conversation with your database and retrieve information as needed. This app performs way better than langchain's SQL agent and cost way less.

## Disclaimer

It is recommended that you create a user without write permissions to connect with this agent, since this agent might perform DML statements on your database. Use with care!!


## Environment Configuration

1. Clone the repo to your local machine and navigate to the app directory by running the following commands:

   ```shell
   git clone https://github.com/chatdbtech/chatdb.git
   cd chatdb

   ```

2. Create a `.env` file in the root directory of the app if it doesn't already exist.

3. Open the `.env` file and add the following line with your OpenAI API key:

   ```shell
   OPENAI_API_KEY=your-openai-key
   ```

## Docker Setup

To run the app in a Docker container, follow these instructions:

1. Make sure you have Docker installed on your system.


2. Build the Docker image by running the following command in the same directory as your Dockerfile:

```shell

docker build -t chatdb .

```

3. Once the image is built, you can run the container using the following command:

```shell

docker run -d -p 8501:8501 chatdb

```

This will start the app inside a Docker container and expose it on port 8501.



## Alternative Installation without Docker

1. Install Miniconda depending on your OS from (https://docs.conda.io/projects/miniconda/en/latest/index.html)

2. Create a conda environment named `chatdb-venv` using the command `conda create --name chatdb-venv python=3.8`

3. Activate the environment using `conda activate chatdb-venv`

4. Within the root directory run `pip install -r requirements.txt`

5. Run the application using `streamlit run app.py`



## Using ChatDB

ChatDB is designed to connect to your database and allow you to communicate with it. Here are the steps to get started:

### Instructions

1. Enter the URI of your RDS Database in the text box provided. The format is generally this `postgres://username:password@host:port/database` for a postgres database.

2. Click the **Start Chat** button to initiate the chat with your database.

3. Enter your message in the text box below and press **Enter** to send the message to the API.

### Chat with the API

- Enter your message in the chat input box, and the app will display the response from your database. You can have a conversation with the database by entering messages and receiving replies.

### Contact Us

If you have any questions, comments, or suggestions about this app, please feel free to [contact us](info@chatdb.tech).

Enjoy using the ChatDB to interact with your database through a user-friendly interface!
