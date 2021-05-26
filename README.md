# phalanx
phalanx is a password generator that doesn't have to trust any servers. It calculates hash value of master password and image file, and you can use the hash value as a generated password.

### Usage
**install**
```bash
pip3 install git+https://github.com/TakutoYoshikai/phalanx.git
```

**generate password**
```bash
phalanx <ANY FILE> -p <MASTER PASSWORD> -l <PASSWORD LENGTH>
```

### License
MIT License
