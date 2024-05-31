> terminal 0
```
wget https://www.openssl.org/source/openssl-3.0.0.tar.gz
tar -xf openssl-3.0.0.tar.gz
cd openssl-3.0.0
./Configure enable-fips
make
```

> terminal 0
```
wget https://www.openssl.org/source/openssl-3.2.0.tar.gz
tar -xf openssl-3.2.0.tar.gz
cd openssl-3.2.0
./Configure enable-fips
make
```

```
cp ../openssl-3.0.0/providers/fips.so providers/.
cp ../openssl-3.0.0/providers/fipsmodule.cnf 
./util/wrap.pl -fips apps/openssl list -provider-path providers -provider fips -providers
make tests
cd ../openssl-3.0.0
sudo mkdir /usr/local/ssl/
cp providers/fipsmodule.cnf /usr/local/ssl/
sudo make install_fips
./util/wrap.pl -fips apps/openssl list -provider-path providers -provider fips -providers
```

---

> in ~/.bashrc

```
export PATH=<YOUR_PATH_TO>/openssl-3.2.0/apps:$PATH
export LD_LIBRARY_PATH=<YOUR_PATH_TO>/openssl-3.2.0:$LD_LIBRARY_PATH
export OPENSSL_FIPS=1
```
```
source ~/.bashrc
```

> in /usr/local/ssl/fipsmodule.cnf, prepend:

```
config_diagnostics = 1
openssl_conf = openssl_init

.include /usr/local/ssl/fipsmodule.cnf

[openssl_init]
providers = provider_sect

[provider_sect]
fips = fips_sect
base = base_sect

[base_sect]
activate = 1

[algorithm_sect]
default_properties = fips=yes
```

> Verify installation with:

```
openssl version -v
```
