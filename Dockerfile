# Use a Python base image
FROM python:3.9-slim

# Add the Mozilla repository for Firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main" >> /etc/apt/sources.list

# Update package lists and install Firefox
RUN apt-get update && apt-get install -y firefox

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code to the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Set the entry point command to run your Python code
CMD ["sh", "-c", "pytest --html=report/report.html && tail -f /dev/null"]