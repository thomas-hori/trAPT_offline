#See comments in trAPT_offline.py

s="install ok installed\t"
ls=len(s) #Optimize "len(s)"

f=open("DesktopManifest_raw","r")
b=f.readlines()
f.close()

f=open("DesktopManifest","w")

for i in b:
	if i[:ls]==s:
		f.write(i[ls:])
