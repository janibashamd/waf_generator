---
Title: 'Custom WAF Generator'
Date: 2023-02-28
Excerpt: 'Unified UI using which customer can generate custom WAF bundle.'
Tags: ['Hackfest', 'F5', 'F5XC', 'waf', 'python']
Team: ['Shubham Mishra', 'Mohammed Janibasha', 'Shajiya Shaik', 'Chaithanya Dileep']
Sponsor: []
Mentor: ['Valentin Tobi']
---
## Project Description

Main purpose of this project is to have a unified tool/UI using which customer can create custom WAF bundles as per their WAF product requirement.

## Key Hypothesis
F5 has diversified products like BIG-IP, Nginx App Protect (NAP) and F5 Distributed Cloud (F5 XC) covering needs as per customer requirements. Currently we don't have a way for customers to generate custom WAF signatures. Waf custom signature Generator (WafGen) aims to make this workflow smooth and ridiculously easy by allowing them to create custom WAF bundles as per user inputs and per WAF engine. </br>
</br>
WafGen offers a unified GUI that allows customers to generate custom WAF bundle for all 3 flavors of WAF.

![hackfest](https://user-images.githubusercontent.com/6093830/221343325-1a25e8cb-ff30-4a05-af87-74fe2d00d6a7.JPG)


## How It Works

Application is written in flask, deployed as k8s service and finally published on F5 XC load balancer over internet so users can access the application.
</br></br>

#### API use case steps
API collection is readily available in repo so users can use them and below are some details about API implementation.</br>
  
| Valid API Endpoints      |   Allowed HTTP Methods   |      param options          |
| ----------| ----------------------------------------|---------------------------- |
| /                        |        GET & POST        |
| /download_file/[target]  |          GET             |   target = bigip/nap/xc     |
</br>

Below is the sample form data payload for sending POST request to API Endpoint `/` 
```
"formdata": [
	{
	"key": "name",
	"value": "custom-waf-sig",
	"type": "default"
	},
	{
	"key": "target",
	"value": "xc",
	"type": "default"
	},	
	{
	"key": "apply_to",
	"value": "Request",
	"type": "default"
	},
	{
	"key": "attack_type",
	"value": "Abuse of functionality",
	"type": "default"
	},
	{
	"key": "rule",
	"value": "Header",
	"type": "default"
	},
	{
	"key": "key",
	"value": "custom-hdr",
	"type": "default"
	},
	{
	"key": "val",
	"value": "<script>",
	"type": "default"
	},
	{
	"key": "accuracy",
	"value": "HIGH",
	"type": "default"
	},
	{
	"key": "priority",
	"value": "HIGH",
	"type": "default"	
	}
]
  ```

#### UI use case steps
Below are the steps for creating custom WAF bundle through UI:
1. Open browser and navigate to `https://wafgen.f5-hyd-demo.com`.
2. Provide all user inputs and then click on `Submit` button.
3. From page, users can either `copy` or `download` the populated WAF signature data.
4. Next as a optional step, customers can import this bundle in any of the WAF engines and add it to their WAF configuration (Note: this is not covered as part of the project).


## Deployment Steps
If users don't want to use publicly available DNS, they can deploy this application locally in below ways:
1. Build docker image using Dockerfile and create container from it. Refer docker build and run docs for more info.
2. In docker enginer user's can run `docker run --name wafgen -d -p 80:8000 registry.gitlab.com/sbmmsra/waf-signature-generator` to run it as container and expose it on 80 port.
3. We can also run this code as k8s service by simply running `kubectl apply -f custom_waf_flask.yml` which will bring up k8s deployment and service (`NOTE:` you should have access to k8s cluser using kubeconfig and svc is available on port 8000).

## Business Value

This project provides a unified UI to create custom WAF bundle as per customer WAF requirements.

## Technologies Used

Python, Flask, Jinja2 and html

## Presentations

#### VIDEO:



#### POWERPOINT:
https://f5.sharepoint.com/:p:/s/F5HackfestFeb23/EYNQ4aGOEHVJgb_PwcQzjHMBpmpunBJyLC3RaS9ccvFvIA?e=mERA7t


## Interested? Come join us!

Reach out to the principal researchers if you are interested in supporting this project.

| Role   | Skills                                                               |
| ------ | ------------------------------------------------------------------------- |
| UI Developer  | html, css, Node, JS |
| API Developer  | API, Flask, JS, Node |
