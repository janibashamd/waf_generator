from flask import Flask, jsonify, request, render_template, send_file
import json
import os
import requests
from requests.structures import CaseInsensitiveDict

DOWNLOAD_DIRECTORY = os.getcwd()
sig_gen = Flask(__name__)


# Allowed methods to endpoint are GET
@sig_gen.route('/', methods=['GET'])
def home_page():
    """Policy creator default route."""
    return render_template('home.html')


@sig_gen.route('/update_template/', methods=['POST'])
def update_template():
    """Update templates after taking inputs."""
    try:
        data = request.get_data().for
        qp = str(request.args.get('header'))
        render_template("custom_pol.html", result=data)
        return jsonify({'query_param': qp})
    except Exception as e:
        return str(e)


@sig_gen.route('/download_file/', methods=['POST'])
def download_file():
    """Return the file once user clicks on download."""
    try:
        # if target == "bigip":
        #     return send_file('bigip_waf_conf.xml', attachment_filename='bigip_custom_signature.xml')
        # elif target == "nap":
        #     return send_file('nginx_basic_conf.json', attachment_filename='nap_definition.json')
        # else:
        #     return send_file("distributed_cloud_service_policy.json",
        #                      attachment_filename='distributed_cloud_service_policy.json')
        return send_file('bigip_waf_conf.xml', attachment_filename='bigip_custom_signature.xml')
    except Exception as e:
        return str(e)


def update_json(qp):
    """Method to update default json accordingly."""
    # gen cust sign
    # update service policy json file
    with open('./my.json', 'r') as file:
        data = json.load(file)
        data["metadata"]["disable"] = qp
    with open("./my.json", "w") as output:
        json.dump(data, output)
        return


if __name__ == '__main__':  
    sig_gen.run(host='0.0.0.0', port=80)
