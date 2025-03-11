# Use official Python 3.12 image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Run both FastAPI and Streamlit together
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

