# Use an official Python runtime as a parent image
FROM python:3.12.0

# Set the working directory in the container to /app
WORKDIR /testtask

# Add the current directory contents into the container at /app
ADD . /testtask

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run tests.py when the container launches
CMD ["python", "tests.py"]
