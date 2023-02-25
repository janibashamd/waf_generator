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
F5 has diversified products like BIG-IP, Nginx App Protect (NAP) and F5 Distributed Cloud (F5 XC) covering needs as per customer requirements. Currently we don't have a way for customers to generate custom WAF signatures. WAF Generator (WafGen) aims to make this workflow smooth and ridiculously easy by allowing them to create custom WAF bundles as per user inputs and per WAF engine. </br>
</br>
WafGen offers a unified GUI that allows customers to generate custom WAF bundle for all 3 flavors of WAF.

![hackfest](https://user-images.githubusercontent.com/6093830/221343325-1a25e8cb-ff30-4a05-af87-74fe2d00d6a7.JPG)


## How It Works

Application is written in flask, deployed as k8s service and finally published on F5 XC load balancer over internet so users can access the application.

Below are the steps for creating custom WAF bundle:
1. Open browser and navigate to `http://wafgen.f5-hyd-demo.com`
2. Provide all user inputs and then click on `Submit` button 
3. From page, users can either `copy` or `download` the populated WAF signature data
4. Next as a optional step, customers can import this bundle in any of the WAF engines and add it to their WAF configuration (Note: this is not covered as part of the project)


## Business Value

This project provides a unified UI to create custom WAF bundle as per customer WAF requirements.

## Technologies Used

Python, Flask, Jinja2 and html

## Presentations

#### VIDEO:



#### POWERPOINT:
https://f5-my.sharepoint.com/:p:/p/m_janibasha/EYvrQKEPvqhIgTlk4SsxagYBq_nsI7dr33ZJGaEjWBfNQA?e=Bpev1J


## Interested? Come join us!

Reach out to the principal researchers if you are interested in supporting this project.

| Role   | Skills                                                               |
| ------ | ------------------------------------------------------------------------- |
| UI Developer  | html, css, Node, JS |
| API Developer  | API, Flask, JS, Node |
