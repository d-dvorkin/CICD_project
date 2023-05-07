# Stage 1: Linting
FROM python:3.8-slim-buster as linting
WORKDIR /app
RUN pip install pylint
COPY *.py ./
RUN pylint --output-format=parseable --fail-under=9.0 *.py > pylint-output.txt || exit 0


# RUN ls -lan /opt/sonar-scanner/conf/
COPY --from=linting /app /app
RUN sonar-scanner 
 
# Stage 3: Production
FROM python:3.8-alpine as production
WORKDIR /app
COPY .aws/ /root/.aws/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
CMD ["python3", "main.py"]
