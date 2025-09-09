FROM python:3.13

# Install dependencies
RUN apt-get update && apt-get install -y ffmpeg rust-all npm

# Enter app directory
WORKDIR /app

# Copy pip requirements file
COPY requirements.txt .

# Install pip modules
RUN pip install --no-cache-dir -r requirements.txt

# Build Bitwarden SDK from source
RUN git clone https://github.com/bitwarden/sdk-sm.git
RUN cd sdk-sm/
RUN npm install
RUN npm run schemas
RUN cd languages/python/
RUN maturin develop
RUN cd ../../../

# Copy rest of the files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the app
CMD ["python", "app.py"]
