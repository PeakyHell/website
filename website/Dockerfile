# --- Build Bitwarden SDK ---
FROM python:3.13 AS builder


# Enter build directory
WORKDIR /build


# Install dependencies
RUN apt-get update \
    && apt-get install -y \
        git \
        rust-all \
        npm \
    && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
RUN pip install --no-cache-dir maturin patchelf


# Build Bitwarden SDK from source
RUN git clone https://github.com/bitwarden/sdk-sm.git


RUN cd sdk-sm/ \
    && npm install \
    && npm run schemas


RUN cd sdk-sm/languages/python/ \
    && maturin build --manylinux off \
    && mv /build/sdk-sm/target/wheels/*.whl /build/


# --- Build Website ---
FROM python:3.13


# Enter app directory
WORKDIR /app


# Install dependencies
RUN apt-get update \
    && apt-get install -y \
        ffmpeg \
    && rm -rf /var/lib/apt/lists/*


# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy and install Bitwarden SDK wheel
COPY --from=builder /build/*.whl .
RUN pip install --no-cache-dir *.whl \
    && rm -f *.whl


# Copy rest of the files
COPY . .


# Expose port 8000
EXPOSE 8000


# Start the app
CMD ["python", "app.py"]
