# public.ecr.aws/lambda/python:3.12-x86_64
FROM public.ecr.aws/lambda/python:3.12

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]

# NOTES #
# You can then locally test your function using the docker build and docker run commands.

# To build you image:
# docker build -t <image name> .

# To run your image locally:
# docker run -p 9000:8080 <image name>

# In a separate terminal, you can then locally invoke the function using cURL:
# curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}'