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
            accuracy_result = str(request.form.get('accuracy'))
            priority_result = str(request.form.get('priority'))
            attack_value = str(request.form.get('attack_type'))
            if accuracy_result == "HIGH":
                final_accracy_result = 3
            elif accuracy_result == "MEDIUM":
                final_accracy_result = 2
            else:
                final_accracy_result = 1
            if priority_result == "HIGH":
                final_priority_result = 3
            elif priority_result == "MEDIUM":
                final_priority_result = 2
            else:
                final_priority_result = 1
            if request.form.get("rule") == "Header":
                dynamic_value = "headercontent"
            elif request.form.get("rule") == "URL":
                dynamic_value = "uricontent"
            if attack_value == "XSS":
                attack_value = "Cross Site Scripting (XSS)"
            if attack_value == "Abuse of functionality":
                attack_value = "Abuse of Functionality"
            rule_value = dynamic_value + ":" + "\"" + str(request.form.get('val')) + "\"" + "; nocase;"
            waf_data = {"name": str(request.form.get('name')), "apply_to": str(request.form.get('apply_to')),
                        "attack_type": attack_value, "rule": rule_value,
                        "accuracy": str(final_accracy_result), "risk": str(final_priority_result)}
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
    child  = root.find('sig').find('rev')
    grand_child_sig_name = child.find('sig_name')
    grand_child_sig_name.text = waf_data["name"]
    grand_child_rule = child.find("rule")
    grand_child_rule.text =  waf_data["rule"]
    grand_child_apply_to = child.find("apply_to")
    grand_child_apply_to.text = waf_data["apply_to"]
    grand_child_risk = child.find("risk")
    grand_child_risk.text = waf_data["risk"]
    grand_child_accuracy = child.find("accuracy")
    grand_child_accuracy.text = waf_data["accuracy"]
    grand_child_attack = child.find("attack_type")
    grand_child_attack.text = waf_data["attack_type"]

    tree.write("./templates/bigip_waf_conf.xml")


def update_ngx_json(waf_data):
    """Update Nginx basic template with user inputs."""
    with open('./nginx_basic_conf.json', 'r') as file:
        data = json.load(file)
    data["signatures"] = waf_data
    with open("./templates/nginx_basic_conf.json", "w") as output:
        json.dump(data, output)


if __name__ == '__main__':
    sig_gen.run(host='0.0.0.0', port=8000, debug=True)
