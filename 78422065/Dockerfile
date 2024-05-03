# FROM amazon/aws-cli:2.8.3

# RUN yum update -y \
#     && curl --silent --location https://rpm.nodesource.com/setup_20.x | bash - \
#     && yum install -y nodejs which zip \
#     && yum clean all \
#     && rm -rf /var/cache/yum

FROM public.ecr.aws/lambda/python:3.9

# Optionally set a working directory
WORKDIR /var/task

# Copy the function code and any additional files
# COPY app.py ./
# COPY requirements.txt ./

# Install any dependencies
# RUN python -m pip install -r requirements.txt

# Set the CMD to your handler (could also be done via function configuration in AWS)
# CMD [ "app.handler" ]

# During local development, you might need to emulate Lambda's environment.
# AWS Lambda Runtime Interface Emulator is used for local testing.
# Uncomment the following lines if you need to run your function locally.

# Install AWS Lambda RIE
RUN curl -Lo aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    && chmod +x aws-lambda-rie \
    && mv aws-lambda-rie /usr/local/bin

# When the image is used locally, AWS Lambda RIE is invoked as the entry point
ENTRYPOINT [ "/usr/local/bin/aws-lambda-rie" ]
