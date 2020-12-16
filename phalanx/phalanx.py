import hashlib
import argparse

def main():
    parser = argparse.ArgumentParser(description="phalanx is a password generator with any file")
    parser.add_argument("file")
    parser.add_argument("-p", "--password")
    args = parser.parse_args()
    f = open(args.file, "rb")
    content = f.read()
    content = bytearray(content)
    if args.password != None:
        content.extend(args.password.encode())
    print(hashlib.md5(content).hexdigest())

if __name__ == "__main__":
    main()
