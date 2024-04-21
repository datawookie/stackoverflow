FROM python:3.10.3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code into the container
COPY . .

# Set the command to run the app
CMD ["sh", "-c", "streamlit run Test.py --server.port=8501 --server.address=0.0.0.0 --server.baseUrlPath=/Testweb/"]
