import base64
import gzip
""" Takes compressed base64-encoded string and converts to uncompressed decoded string (the original text)
Step 1 : use base64 to change compressed encoded string to compressed decoded string
Step 2 : Create local zipped file (gz) containing compressed decoded string. 
This can be unzipped to read contents
Step 3 : Open zipped file to extract contents in memory to be used as needed

Returns:
    [file] -- [zipped file containing decoded text]
    [string] -- [contains clear text]
"""
zipfile = "zipfile.gz"

def extract_zip(input_zip):
    with gzip.open(input_zip) as f:
        data = f.read()
    return data


secret_test = "H4sIAAAAAAAEACtJLS4BAAx+f9gEAAAA"  # compressed base64 encoded string from 'test' string 
secret_raw = "H4sIAAAAAAAAAE2OPQ+CMBCG\\/8vNmJSKNd5owuZgwuDQMJxwhCalYFswxPjfrR+D4\\/Pe+16eB4SGnOcw2xgA9QOuIZgWEEhgt8Umx0IidSglZPA7+aUfB07c0ERXY000nMagL+W51mVV1fp4KutU6DzfZnbNCiiLXGZgeWELuFEqg2gGDpGGCTCXQhVif5BSqV36yy6yf48FoPjn\\/Ms9Ocf2btrYf4JxYk9xTBXDrrWro+SHkAwWdkngh8\\/6+QL2SvRC8QAAAA=="
secret_clean = secret_raw.replace("\\", "")
print(f"{secret_clean}")

# s = s.replace("\\", "")
compressed_secret = base64.b64decode(secret_clean)  # compressed bases64 decoded
with open(zipfile, 'wb') as newzip: # i can uncompress using 7 zip successfully after this runs
    newzip.write(compressed_secret)

extracted_data = extract_zip(zipfile)
print(extracted_data)

