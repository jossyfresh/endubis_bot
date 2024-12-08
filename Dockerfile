FROM python:3.10-slim

WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

EXPOSE 5000

# Set the environment variable to prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "main.py"]
