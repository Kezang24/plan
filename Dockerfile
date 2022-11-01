FROM python
WORKDIR /app
COPY ./requirement.txt /app
RUN pip install -r requirement.txt
COPY . /app
CMD ["python3", "main.py", "--host","localhost", "--port", "5000"]


# FROM python

# WORKDIR /app
# ADD requirement.txt /app
# RUN pip3 install python-dateutil
# RUN pip3 install -r requirements.txt
# ADD . /app


ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]
