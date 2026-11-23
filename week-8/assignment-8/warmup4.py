""" Warmup 4: Virtual Environment Setup
Set up a virtual environment for your project, install the requests library, 
and generate a requirements.txt with pip freeze. Then write a short script that
 imports requests and prints its version. Paste the contents of your requirements.txt
 as a comment at the top of the file."""

# certifi==2026.10.23
# charset-normalizer==3.5.2
# idna==3.20
#requests==2.34.2
# urllib3==2.8.0

import requests 
print(f"Requests version: {requests.__version__}")