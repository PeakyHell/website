# --- Build Sphinx Documentation ---
FROM python:3.13 AS sphinx

# Enter build directory
WORKDIR /sphinx

# Install dependencies
RUN pip install --no-cache-dir sphinx sphinx-book-theme

# Copy the source files
COPY sphinx/ .

# Build the html files
RUN make html

# --- Nginx ---
FROM nginx:latest

COPY certificates/cert.pem /etc/nginx/certificates/
COPY certificates/key.pem /etc/nginx/certificates/

# Copy Sphinx documentation
COPY --from=sphinx /sphinx/build/* /usr/share/nginx/html/docs/

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
