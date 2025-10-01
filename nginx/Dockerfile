# --- Build Sphinx Documentation ---
FROM python:3.13 AS sphinx

# Enter build directory
WORKDIR /sphinx

# Clone the source files
RUN git clone https://github.com/PeakyHell/documentations.git

# Install dependencies
RUN pip install --no-cache-dir sphinx sphinx-book-theme

# Build the html files
RUN cd documentations \
	&& make html

# --- Nginx ---
FROM nginx:latest

# Copy Sphinx documentation
COPY --from=sphinx /sphinx/documentations/build/* /usr/share/nginx/html/docs/

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
