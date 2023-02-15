from flask import Flask, jsonify, request, render_template
import json
import requests
from requests.structures import CaseInsensitiveDict
from flask import send_file

sig_gen = Flask(__name__)


# Allowed methods to endpoint are GET & POST
@sig_gen.route('/', methods=['GET', 'POST'])
def policy_creator():
    """Policy creator default route."""
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        #data = request.get_json()
        target = request.form.get("target")

        if target == "bigip":
            pass #chaithanya
        elif target == "nap":
            pass #shajiya
        elif target == "xc":
            d = {}

            d["sign_name"] = str(request.form.get('name'))
            d["sign_type"] = str(request.form.get('apply_to'))
            d["attack"] = str(request.form.get('attack_type'))
            d["rule"] = str(request.form.get('rule'))
            d["value"] = str(request.form.get('val'))
            d["accuracy"] = str(request.form.get('accuracy'))
            d["risk"] = str(request.form.get('priority'))
            # send query param to update service policy json file
            update_xc_json(d)
            #return render_template('sp.json')
        else:
            #custom errror message
            print("nothing matched!")
        path = "./templates/sp.json"
        return send_file(path, as_attachment=True)
        #return jsonify(render_template('./my.json'))

def update_xc_json(inputs):
    """Method to update default json accordingly."""
    # gen cust sign
    # update service policy json file
    with open('./templates/sp.json', 'r') as file:
        data = json.load(file)
        data["metadata"]["name"] = inputs["sign_name"]
        if inputs["rule"] == "Header":
           data["spec"]["rule_list"]["rules"][0]["spec"]["headers"][0]["item"]["exact_values"][0] = inputs["value"]
    with open("./templates/sp.json", "w") as output:
        json.dump(data, output)
        return

def update_xml():
    pass


def update_ngx_json():
    pass


if __name__ == '__main__':
    sig_gen.run(host='0.0.0.0', port=80)
                                           