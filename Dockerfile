FROM python:3.6
 
<<<<<<< HEAD
RUN mkdir -p /hackfest/waf_sig_gen
=======
COPY  --chown=siggen:siggen . /home/siggen/custom_waf_generator/
>>>>>>> 93938a6914e3570aa1a027dc1346aa71c37d5f9d

WORKDIR /hackfest/waf_sig_gen

RUN pip install requests

RUN pip install flask-restful

COPY . /hackfest/waf_sig_gen

EXPOSE 8000

CMD ["python", "waf_sig.py"]
