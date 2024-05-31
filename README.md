# gen.quey

## setup

> You should be using WSL, or Linux - on a cheap and shitty machine (see ##protocol to understand why)

> In order to be [FIPS compliant](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282), we are relying on [OpenSSL](https://www.openssl.org/docs/fips.html)

> > You must then follow [this guide](./fips.md) to set up the correct OpenSSL module with FIPS enabled

```
git clone https://github.com/auto-cannibal/gen.quey.git
chmod a+x *.sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./run.sh
```

## protocol

> The rasberry pi (or whatever) which was used to encode the secret file has been dissasembled, destroyed and had its parts hung-drawn-quartered and sent for recycling to seperate companies

> > The ciphertext gas been sent to a host machine - or even backed up on your cloud 

> > This means all trace of keystrokes containing information eluding to the user inputted secrets are lost to natural entropy

> As a consequence, the only vulnerability to this program comes in the form of software - with the libraries used to encode the secret, and errors in the theory backing those libraries

## instructions for trustees

> PLEASE NOTE THAT SHOULD YOU SUCCESSFULLY GAIN ACCESS TO YOUR SECRET, THE SECURITY OF THE DEVICE YOU ARE USING IS THEN PERMANENTLY COMPROMISED, IN THE CONTEXT OF THIS PROGRAM
> > IT IS THEREFORE RECOMMENDED THAT YOU TRANSFER YOUR SECRET TO SOMEWHERE YOU ARE COMFORTABLE KEEPING IT, AND DISSASEMBING THE DEVICE YOU USED TO GAIN ACCESS TO THE SECRET, AND TAKE A LARGE MAGET TO IT, SUBMERGE IT IN WATER AND THEN SPLIT IT INTO MULTIPLE COMPONENTS AND RECYCLE THESE COMPONENTS AS SEEN FIT

0. In windows search, type in `Ubuntu on Windows` and open this program
1. In this program, type in the following and press `enter`
```
cd gen.quey/
```
2. In the same program, type in the following, and press `enter`
```
./run.sh
```
3. Now follow the instructions in the program...and don't screw up!