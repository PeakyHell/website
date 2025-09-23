# PeakyHell's Website

## Usage without Docker

1. Clone the repository.
```
git clone https://github.com/PeakyHell/website.git

cd website/
```

2. Create the secrets files and write the secrets inside
```
mkdir secrets/
nano secrets/bw_api_url.txt
nano secrets/bw_identity_url.txt
nano secrets/bw_access_token.txt
nano secrets/db_password.txt
```

3. Generate the SSL certificate and key.
```
mkdir nginx/certificates/
openssl req -newkey rsa:2048 -keyout nginx/certificates/key.pem -x509 -days 365 -out nginx/certificates/cert.pem -nodes
```

4. Create a virtual environment and install the dependencies for the web app.
```
cd website/

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

5. Start the web server with Gunicorn.
```
gunicorn -c gunicorn.py app:app
```

6. Navigate to your website at `https://localhost:8000`

## Usage with Docker

1. Clone the repository.
```
git clone https://github.com/PeakyHell/website.git

cd website/
```

2. Create the secrets files and write the secrets inside
```
mkdir secrets/
nano secrets/bw_api_url.txt
nano secrets/bw_identity_url.txt
nano secrets/bw_access_token.txt
nano secrets/db_password.txt
```

3. Generate the SSL certificate and key.
```
mkdir nginx/certificates/
openssl req -newkey rsa:2048 -keyout nginx/certificates/key.pem -x509 -days 365 -out nginx/certificates/cert.pem -nodes
```

4. Build the Docker images.
```
docker compose build
```

5. Start the docker containers.
```
docker compose up -d
```

6. Navigate to your website at `https://localhost`
