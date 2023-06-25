# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code to the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Set the entry point command to run your Python code
CMD [ "pytest" ]