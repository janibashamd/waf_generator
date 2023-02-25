from flask import Flask, request, render_template
import json
from flask import send_file
import xml.etree.ElementTree as ET

sig_gen = Flask(__name__)


# Allowed methods to endpoint are GET & POST
@sig_gen.route('/', methods=['GET', 'POST'])
def policy_creator():
    """Policy creator default route."""
    global json_path
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        target = request.form.get("target")
        if target == "bigip":
            rule_value = str(request.form.get('rule')) + ":" + str(request.form.get('val')) + "; nocase;"
            waf_data = {"name": str(request.form.get('name')), "apply_to": str(request.form.get('apply_to')),
                        "attack_type": str(request.form.get('attack_type')), "rule": rule_value,
                        "accuracy": str(request.form.get('accuracy')), "risk": str(request.form.get('priority'))}
            update_xml(waf_data)
            json_path = "./templates/bigip_waf_conf.xml"

        elif target == "nap":
            rule_value = str(request.form.get('rule')) + ":" + str(request.form.get('val')) + "; nocase;"
            waf_data = [{"name": str(request.form.get('name')), "signatureType": str(request.form.get('apply_to')),
                        "attackType": {"name": str(request.form.get('attack_type'))}, "rule": rule_value,
                         "accuracy": str(request.form.get('accuracy')), "risk": str(request.form.get('priority'))}]
            update_ngx_json(waf_data)
            json_path = "./templates/nginx_basic_conf.json"

        elif target == "xc":
            d = {"sign_name": str(request.form.get('name')), "sign_type": str(request.form.get('apply_to')),
                 "attack": str(request.form.get('attack_type')), "rule": str(request.form.get('rule')),
                 "name": str(request.form.get('key')),
                 "value": str(request.form.get('val')), "accuracy": str(request.form.get('accuracy')),
                 "risk": str(request.form.get('priority'))}
            # send user param to update service policy json file
            update_xc_json(d)
            json_path = "./templates/f5xc_service_policy.json"

        # return send_file(path, as_attachment=True)
        with open(json_path, 'r') as f:
            return render_template('custom_pol.html', target=target, text=f.read())


@sig_gen.route('/download_file/<target>', methods=['GET'])
def download_file(target):
    """Downloading file endpoint."""
    if target == "xc":
        file_path = "./templates/f5xc_service_policy.json"
    elif target == "nap":
        file_path = "./templates/nginx_basic_conf.json"
    else:
        file_path = "./templates/bigip_waf_conf.xml"
    print("Successfully downloaded waf bundle for : " + str(target))
    return send_file(file_path, as_attachment=True)


def update_xc_json(inputs):
    """Method to update default json accordingly."""
    # gen cust sign
    with open('./templates/f5xc_service_policy.json', 'r') as file:
        data = json.load(file)
        data["metadata"]["name"] = inputs["sign_name"]
        if inputs["rule"] == "Header":
            data["spec"]["rule_list"]["rules"][0]["spec"]["headers"][0]["name"] = inputs["name"]
            data["spec"]["rule_list"]["rules"][0]["spec"]["headers"][0]["item"]["exact_values"][0] = inputs["value"]
            #data["spec"]["rule_list"]["rules"][0]["spec"]["headers"][0]["item"]["exact_values"][0] = inputs["value"]
    with open("./templates/f5xc_service_policy.json", "w") as output:
        json.dump(data, output)


def update_xml(waf_data):
    """Update BigIP basic template with user inputs."""
    tree = ET.parse('bigip_waf_conf.xml')
    root = tree.getroot()
    name = root.find('sig').find('rev')
    name.set("sig_name", waf_data["name"])
    name.set("risk", waf_data["risk"])
    name.set("apply_to", waf_data["apply_to"])
    name.set("accuracy", waf_data["accuracy"])
    name.set("rule", waf_data["rule"])

    tree.write("./templates/bigip_waf_conf.xml")


def update_ngx_json(waf_data):
    """Update Nginx basic template with user inputs."""
    with open('./nginx_basic_conf.json', 'r') as file:
        data = json.load(file)
    data["signatures"] = waf_data
    with open("./templates/nginx_basic_conf.json", "w") as output:
        json.dump(data, output)


if __name__ == '__main__':
<<<<<<< HEAD
    sig_gen.run(host='0.0.0.0', port=8000, debug=True)
=======
    sig_gen.run(host='0.0.0.0', port=80, debug=True)
                                           
>>>>>>> 93938a6914e3570aa1a027dc1346aa71c37d5f9d
