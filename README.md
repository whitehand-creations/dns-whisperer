# DNS WHISPERER 
A CLI tool made for enumerating DNS records for domains

## Usage 
python3 main.py --domain DOMAIN --record RECORD_TYPE 

## Examples

python3 main.py --domain google.com --record A
python3 main.py --domain google.com --record MX
python3 main.py --domain google.com --record TXT


## Requirements
Python 3.x 
dnspython 

## Installation
git clone https://github.com/whitehand-creations/dns-whisperer.git
cd dns-whisperer
pip install -r requirements.txt

## Disclaimer
This tool is for legal and authorized use only. 
Gain consent before enumerating a domain 

## License
MIT License
