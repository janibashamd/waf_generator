FROM python:3.6
 
RUN mkdir -p /hackfest/waf_sig_gen

WORKDIR /hackfest/waf_sig_gen

RUN pip install requests

RUN pip install flask-restful

COPY . /hackfest/waf_sig_gen

RUN chmod -R 777 /hackfest/waf_sig_gen

EXPOSE 8000

CMD ["python", "waf_sig.py"]
