import base64

s = r"H4sIAAAAAAAAAMWTPWvDMBCG\\/0q42QVZ\\/pB8cwrdOrh0CRkU64IFsuzaSkoI+e+V21BMMLRgQsZ7Jd3p4ZHOMFTK9TQcrB8AN2fYDYPRgKBTzCWmGmOGOkeSEMF16a2m1avVq7I2XUgr1amdscYbCi1g81yW2xDve\\/o4kKtOgDwVPAJLR7KATzmLwJuGBq+aDlAUhchiLgqWh17kPPXjUQbIpnX8U9fKObKfRvv6O2g76pVvwxZDTtuTUw2FS4T5R3Jh\\/LW8RPNkFUe1jCydkmWzZLJ4ANnorFpAlvHR0y+ZmHcW35JlXPwJFy+DYxTIcL9MG59qk\\/PasvgxD3KZNj7RJue1yfE73mhL7qQtYSgF6gKTBFOJbKLtpfVk14d34\\/4pLRETtGIeTWZ3lLa9fAFwsc3+MQUAAA==\""
s = s.replace("\\", "")

print(s)
secret_revealed = base64.b64decode(s) 
print(f"{secret_revealed}")


print(f"Hello World 2")
# print(f"{secret_revealed}")
