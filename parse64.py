import base64
import gzip
import io


""" Takes compressed base64-encoded string and converts to uncompressed decoded string (the original text)
Step 1 : remove escapes from original compressed 64coded string
Step 2 : decode using b64decode
Step 3 : pass decoded (still compressed string) to gunzip function that uses IO functions and gzip to decompress)
Note: the gunzip_bytes_obj() is copied from Garrett-R: https://gist.github.com/Garrett-R/dc6f08fc1eab63f94d2cbb89cb61c33d
Returns:
    [string] -- [contains clear text]
"""

def gunzip_bytes_obj(bytes_obj): # function to unzip a decoded byte string
    in_ = io.BytesIO()
    in_.write(bytes_obj)
    in_.seek(0)
    with gzip.GzipFile(fileobj=in_, mode='rb') as fo:
        gunzipped_bytes_obj = fo.read()
    return gunzipped_bytes_obj.decode()

def clean_coded_zip(coded_string):
    return coded_string.replace("\\", "")

def get_full_string(raw_coded_zip):
    cleaned_coded_zip = clean_coded_zip(raw_coded_zip)
    decoded_zip = base64.b64decode(cleaned_coded_zip)  # compressed bases64 decoded
    full_string = gunzip_bytes_obj(decoded_zip)
    return full_string

# raw_coded_zip = "H4sIAAAAAAAAAE2OPQ+CMBCG\\/8vNmJSKNd5owuZgwuDQMJxwhCalYFswxPjfrR+D4\\/Pe+16eB4SGnOcw2xgA9QOuIZgWEEhgt8Umx0IidSglZPA7+aUfB07c0ERXY000nMagL+W51mVV1fp4KutU6DzfZnbNCiiLXGZgeWELuFEqg2gGDpGGCTCXQhVif5BSqV36yy6yf48FoPjn\\/Ms9Ocf2btrYf4JxYk9xTBXDrrWro+SHkAwWdkngh8\\/6+QL2SvRC8QAAAA=="
# print(get_full_string(raw_coded_zip))

