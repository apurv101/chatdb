# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install system packages for building Python packages
RUN apt-get update && apt-get install -y build-essential

# Create a virtual environment
RUN python -m venv /venv

# Set the virtual environment as the active Python environment
ENV PATH="/venv/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt within the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]
