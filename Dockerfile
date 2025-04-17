# Use a Python base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy your repository files into the container
COPY . /app

# Install dependencies (if needed)
RUN pip install -r requirements.txt

#Upgrade Python Inside My container
RUN pip install --upgrade pip

#Not Pure Python Package so cannot be installed through requirements & Set Time OUT

RUN pip install --default-timeout=100 spacy && python -m spacy download en_core_web_sm


# Define the command to run your script
CMD ["python", "linkedIn_search_script.py"]
