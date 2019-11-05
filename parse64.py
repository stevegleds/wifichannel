import base64
from gzip import GzipFile

secret = "H4sIAAAAAAAEACtJLS4BAAx+f9gEAAAA"  # compressed base64 encoded string from 'test' string 
# s = s.replace("\\", "")

print(secret)
compressed_secret = base64.b64decode(secret)  # compressed bases64 decoded
print(f"{compressed_secret}")
with open("newzip.gz", 'wb') as newzip: # i can uncompress using 7 zip successfully after this runs
    newzip.write(compressed_secret)

def extract_zip(input_zip):
    return GzipFile(input_zip).open() # this fails 

with open("newzip.gz", 'rb') as file64:
    zip = extract_zip(file64)
    print("zip file contains:", zip)
    