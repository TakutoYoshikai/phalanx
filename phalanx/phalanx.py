import hashlib
import argparse

def generate_password(filepath, password):
    f = open(filepath, "rb")
    content = f.read()
    content = bytearray(content)
    if password != None:
        content.extend(password.encode())
    return hashlib.md5(content).hexdigest()

def main():
    parser = argparse.ArgumentParser(description="phalanx is a password generator with any file")
    parser.add_argument("file")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    print(generate_password(args.file, args.password))

if __name__ == "__main__":
    main()
