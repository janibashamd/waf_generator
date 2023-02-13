FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN useradd -ms /bin/bash siggen

USER siggen

ENV PATH="/home/siggen/.local/bin:${PATH}"

RUN pip install requests

RUN pip3 install flask-restful
 
COPY  --chown=siggen:siggen ./* /home/siggen/demo/

WORKDIR /home/siggen/demo/

RUN ls -a

EXPOSE 80

CMD [ "python3", "test.py" ]


