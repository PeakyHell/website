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

RUN cd sdk-sm/ \
    && npm install \
    && npm run schemas

RUN cd sdk-sm/languages/python/ \
    && maturin build --manylinux off\
    && pip install /app/sdk-sm/target/wheels/bitwarden_sdk-1.0.0-cp313-abi3-linux_aarch64.whl

# Copy rest of the files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the app
CMD ["python", "app.py"]
