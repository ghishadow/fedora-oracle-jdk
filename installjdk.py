#!/usr/bin/python3
import os
os.system('echo -e "\033[0;32m Downloading Oracle JDK at  ..\033[0m"')
#os.system('wget -c --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" "http://download.oracle.com/otn-pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm"')
print("Downloading Done. Starting Installation process....")
os.system('rpm -ivh jdk-8u102-linux-x64.rpm')
print('Installation done')