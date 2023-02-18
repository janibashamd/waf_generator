from flask import Flask, jsonify, request, render_template
import json
from flask import send_file

sig_gen = Flask(__name__)


# Allowed methods to endpoint are GET & POST
@sig_gen.route('/', methods=['GET', 'POST'])
def policy_creator():
    """Policy creator default route."""
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        target = request.form.get("target")
        if target == "bigip":
            pass #chaithanya
            waf_data = ""
        elif target == "nap":
            pass #shajiya
            waf_data = ""
        elif target=="xc":
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
        else:
            # custom error message
            print("nothing matched!")
        json_path = "./templates/sp.json"
        # return send_file(path, as_attachment=True)
        with open(json_path, 'r') as f:
            return render_template('custom_pol.html', text=f.read())


@sig_gen.route('/download_file/', methods=['GET'])
def download_file():
    """Downloading file endpoint."""
    json_path = "./templates/sp.json"
    print("Successfully downloaded waf bundle.")
    return send_file(json_path, as_attachment=True)


def update_xc_json(inputs):
    """Method to update default json accordingly."""
    # gen cust sign
    with open('./templates/sp.json', 'r') as file:
        data = json.load(file)
        data["metadata"]["name"] = inputs["sign_name"]
        if inputs["rule"] == "Header":
            data["spec"]["rule_list"]["rules"][0]["spec"]["headers"][0]["item"]["exact_values"][0] = inputs["value"]
        #waf_data=json.dump(data)
    with open("./templates/sp.json", "w") as output:
        json.dump(data, output)
    #return waf_data


def update_xml():
    pass


def update_ngx_json():
    pass


if __name__ == '__main__':
    sig_gen.run(host='0.0.0.0', port=80, debug=True)
                                           