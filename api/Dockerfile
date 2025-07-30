#Importing python base image
FROM python:3.10

# Creating Environment
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development

# Assigning Working directory in the container
WORKDIR /app

# Copying the requirements.txt file to the /app/requirements.txt
COPY requirements.txt requirements.txt

# Running the bash commands to update the server and insall the requirements
RUN pip install -r requirements.txt

# Copying the whole codes from local to /app 
COPY . .

# Running commands to start the app on the server. "--host=0.0.0.0", "--port=5000" is telling docker :
# Run the waitress WSGI server, expose it on all interfaces, on port 5000, and load the app from wsgi.py.
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "wsgi:app"]