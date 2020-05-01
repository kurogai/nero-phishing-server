# NERO - The WEB Phishing Tool [Alpha]
![Optional Text](../master/images/alt1.png)

NERO is an Simple but powerfull fishing tool, build in python with python payloads.
The main purpose of NERO, is to simplify the WEB attack vectors during the pentest. Also, it comes with is 
own modules to automate WEB Based Pentest, such as Social Engineering, Scanning, and Footprint.

## Features

* Quick and easy to use
* Performs ARP Poisoning
* Try to match host OS
* SSL Support
* Quick integrated port scanning tool
* Hability to create a full costumized server
* Can bypass full static pages (enable module "Costum page")
* Note: this is the alpha version, errors may appear. If so, please report.

## Basic use

The default use for NERO, is:
```
   set ip [adress]
   set port [adress]
   set url [complete url]
   run
```
You can ative modules for better fingerprint:
```
  set module [id]
  example
  set module 4
```
If you turn on "Costumized", the url option turn unavaliable, and you can run an costumized server, with html/index.html as default file

Displaying help
```
  help
```

Displaying all current modules
```
  list
```

## Notes for Alpha

The alpha version, comes with an complete server to use, but some erros may occour while setting up an costumized server and SSL verification. If you find one of then, please report :) .

## Requirements

* Python 3
* Scapy

## LICENSE

See license file for more
