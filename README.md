# GenKat
Generating obfuscation code
## Description
The script is used to generate obfuscated python code.
The input data also implies the use of scripts in python.
For obfuscation, the AES-128 cryptographic algorithm with the CFB mode is used to encrypt the initial data and xor for the subsequent encryption of the AES keys and input vector.
## Installation
pip3 install -r requirements.txt
## Usage
python3 gen_obfuscate_code.py <path_to_file> 
