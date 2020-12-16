import hashlib
import argparse
import base64

def generate_password(filepath, password, length):
    f = open(filepath, "rb")
    content = f.read()
    content = bytearray(content)
    if password != None:
        content.extend(password.encode())
    result = base64.b64encode(hashlib.md5(content).hexdigest().encode()).decode()
    result = result[:length]
    return result

def main():
    parser = argparse.ArgumentParser(description="phalanx is a password generator with any file")
    parser.add_argument("file")
    parser.add_argument("-p", "--password")
    parser.add_argument("-l", "--length", default=32)
    args = parser.parse_args()
    print(generate_password(args.file, args.password, int(args.length)))

if __name__ == "__main__":
    main()
