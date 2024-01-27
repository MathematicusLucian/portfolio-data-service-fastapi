FROM public.ecr.aws/lambda/python:3.12

COPY app.py requirements.txt ./

RUN python3.12 -m pip install --no-cache-dir --upgrade -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.handler"]

# NOTES #
# You can then locally test your function using the docker build and docker run commands.

# To build you image:
# docker build -t <image name> .

# To run your image locally:
# docker run -p 9000:8080 <image name>

# In a separate terminal, you can then locally invoke the function using cURL:
# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'