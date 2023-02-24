# Custom WAF Generator
Tool to create a custom WAF bundle
<br><br>

Objective:<br>
F5 has different different products covering WAF needs as per customer requirements. BigIp, Nginx App Protect and F5 Distributed Cloud provide WAF support and as of now
we don't have a tool/script to generate a custom WAF which can be created and used for customer deployments. So the main purpose of this project is to have a unified
tool/UI using which customer can get expected WAF bundles as per their product requirement.
<br><br>
![image](https://user-images.githubusercontent.com/6093830/221205137-978631fa-01fe-4253-be5b-088ad85a98cf.png)

Tools used:<br>
Python, html, Docker and Flask
<br><br>

Prerequisites:
1. User should have atleast some basic understanding on WAF deployment and it's options
2. User must have info related to requests, headers, payloads and URL's
<br><br>

Steps for creating custom WAF bundle:
1. Open browser and navigate to `<lb-domain-name>`
2. Provide all user inputs and then click on `Submit` button 
3. From page copy/download the populated WAF signature data
