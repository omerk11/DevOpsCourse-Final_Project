FROM python:3.7-alpine
COPY rest_app.py backend_testing.py clean_environment.py db_connector.py .creds install.txt /
EXPOSE 5000
RUN pip3 install -r  install.txt
RUN chmod 644 rest_app.py
CMD ["python3", "./rest_app.py"]