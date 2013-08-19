#!/usr/bin/python -i

BATTERIES_NOT_INCLUDED=0
BATTERIES_INCLUDED=1
BATTERIES_AND_ACCESSORIES_INCLUDED=2

#SWITCHES HERE
level=BATTERIES_INCLUDED
repolist="Maverick" #File
repoloc="http://archive.ubuntu.com/ubuntu/" #Repositary: archive.ubuntu.com

#'dpkg-query -W -f="\${Package}\t\${Version}\n"' style
#However having the config files should not qualify in this situation as the package being present
#DesktopManifest_raw is 'dpkg-query -W -f="\${Status}\t\${Package}\t\${Version}\n"'
#From that, only "install ok installed    " lines must be taken and reformatted
#Manifest_phase2.py aims to do that
desktop_manifest="DesktopManifest" #File

#TODO: Handle "Replaces" fields properly
#Replaces are currently autoconverted to provides.  2 issues:
#
# - Provides cannot specify versions
# - Provides are lower priority thatn actualities, replaces higher...

doiing=[]

sizez=[]

class Package(object):
    installed=False
    def __iter2__(self):
        for i in self.depends:
            i.important=1
            yield i
        if level>=1:
            for i in self.recommends:
                i.important=0
                yield i
        if level>=2:
            for i in self.suggests:
                i.important=0
                yield i
    def __iter__(self):
        if self.name in doiing:
            raise StopIteration
        else:
            doiing.append(self.name)
        yield repoloc+majad[self.name].location
        sizez.append(self.size)
        for i in self.depends:
            i.important=1
            if i.installed:continue
            for j in majad[i.name]:
                yield j
        if level>=1:
            for i in self.recommends:
                i.important=0
                if i.installed:continue
                for j in majad[i.name]:
                    yield j
        if level>=2:
            for i in self.suggests:
                i.important=0
                if i.installed:continue
                for j in majad[i.name]:
                    yield j
        doiing.remove(self.name)

class Dependancy(Package):
    pass

#Calculation of majad below

prowviydz={}
replycz={}

def parse_lists(f): #f is a file object
    print "Parsing",f
    li={}
    d={}
    lastkey=None
    while 1:
        l=f.readline()
        if not l.strip():
            if d:
                li[d["Package"]]=d
                if "Provides" in d:
                    providelist=d["Provides"].split(", ")
                    for providee in providelist:
                        if providee not in prowviydz:
                            prowviydz[providee]=[]
                        prowviydz[providee].append(d["Package"])
                if "Replaces" in d:
                    providelist=[nnn.split()[0] for nnn in d["Replaces"].split(", ")]
                    for providee in providelist:
                        if providee not in replycz:
                            replycz[providee]=[]
                        replycz[providee].append(d["Package"])
                d={}
            if not l:break
            continue
        if not l: #NOT elif
            break
        else:
            l=l.strip("\n")
            if l.startswith(" "):
                k=lastkey
                extrav="\n"+l[1:]
                if extrav=="\n.":
                    extrav="\n"
                d[k]=d[k]+extrav
            else:
                #print l
                k,v=l.split(": ",1)
                d[k]=v
                lastkey=k
    prowviydz.update(replycz) #Overwrite provides with replaces
    return dict(  zip(li.keys(), map(parse_dict,li.values()) )  )

def parse_dict(d): #d is a dict for an individual package
    #print "Parsing",d
    p=Package()
    p.location=d["Filename"]
    p.depends=[]
    p.recommends=[]
    p.suggests=[]
    p.name=d["Package"]
    p.version=parse_version(d["Version"])
    if "Depends" in d:
        p.depends=parse_depends(d["Depends"])
    if "Recommends" in d:
        p.recommends=parse_depends(d["Recommends"])
    if "Suggests" in d:
        p.suggests=parse_depends(d["Suggests"])
    p.size=d["Size"]
    return p

def parse_depends(s):
    print "Parsing",s
    s=s.strip().split(", ")
    lis=[]
    for i in range(len(s)):
        p=Dependancy()
        si=tuple(s[i].split(" | "))
        p.name={}
        for j in range(len(si)):
            if " " in si[j]:
                sij,version=si[j].split(" ",1)
                assert version[0]=="(" and version[-1]==")"
                version=parse_version(version[1:-1])
            else:
                sij=si[j]
                version=parse_version(">= 0")
            p.name[sij]=version
        lis.append(p)
    return lis

def parse_version(v):
    if v[:2] in (">=","<=","<<",">>"):
        return v[2:].strip(),v[:2]
    elif v[0]=="=":
        return v[1:].strip(),v[0]
    else:
        return v

#See deb-version(5)
#DOES NOT WOOOOOOOOOOOOOOORK
#def veriscorrect(a,b):
#    #print "******* VIC< %r %r"%(a,b)
#    o=veriscorrect_actualiteeee(a,b)
#    #print "******* VIC> %r "%o
#    return o
#
#def veriscorrect_actualiteeee(tomatch,actual):
#    if type(actual)==type(()):
#        a,op2=actual
#    else:
#        a=actual
#    b,op=tomatch
#    #a op b  where op is an operator
#    odict={"<<":(-1,),"<=":(-1,0),"=":(0,),">=":(0,1),">>":(1,)}
#    cmpres=cmpverz(a,b)
#    return cmpres in odict[op]
#
#def cmpverz(a,b):
#    #print "******* CV< %r %r"%(a,b)
#    o=cmpverz_actualiteeee(a,b)
#    #print "******* CV> %r "%o
#    return o
#
#def cmpverz_actualiteeee(a,b):
#    #-1 if <, 0 if =, 1 if >
#    
#    acolon=a.find(":")
#    adash=a.find("-")
#    if acolon>=0 and (adash<0 or acolon<adash):
#        aepoch,aversion=a.split(":",1)
#    else:
#        aepoch="0"
#        aversion=a
#    if adash>=0:
#        aupstream,adebian=aversion.split("-",1)
#    else:
#        aupstream=aversion
#        adebian=""
#    bcolon=b.find(":")
#    bdash=b.find("-")
#    if bcolon>=0 and (bdash<0 or bcolon<bdash):
#        bepoch,bversion=b.split(":",1)
#    else:
#        bepoch="0"
#        bversion=b
#    if bdash>=0:
#        bupstream,bdebian=bversion.split("-",1)
#    else:
#        bupstream=bversion
#        bdebian=""
#    if aepoch<bepoch:
#        return -1
#    if aepoch>bepoch:
#        return 1
#    #XXX Optimize
#    if upstreamdebiancmp(aupstream,bupstream)<0: #NOT elif
#        return -1
#    if upstreamdebiancmp(aupstream,bupstream)>0:
#        return 1
#    return upstreamdebiancmp(adebian,bdebian)
#
#def upstreamdebiancmp(a,b):
#    #print "******* UDC< %r %r"%(a,b)
#    o=upstreamdebiancmp_actualiteeee(a,b)
#    #print "******* UDC> %r "%o
#    return o
#
#def upstreamdebiancmp_actualiteeee(a,b):
#    while a or b:
#        a_alpha=""
#        while a and not a[0].isdigit():
#            a_alpha+=a[0]
#            a=a[1:]
#        b_alpha=""
#        while b and not b[0].isdigit():
#            b_alpha+=b[0]
#            b=b[1:]
#        dac=debalphacmp(a_alpha,b_alpha)
#        if abs(dac):
#            return dac
#        a_digit="0"
#        while a and a[0].isdigit():
#            a_digit+=a[0]
#            a=a[1:]
#        b_digit="0"
#        while b and b[0].isdigit():
#            b_digit+=b[0]
#            b=b[1:]
#        a_num=int(a_digit,10)
#        b_num=int(b_digit,10)
#        if a_num<b_num:
#            return -1
#        if a_num>b_num:
#            return 1
#        #print a,b
#    return 0
#
#def debalphacmp(a,b):
#    #print "******* DAC< %r %r"%(a,b)
#    o=debalphacmp_actualiteeee(a,b)
#    #print "******* DAC> %r "%o
#    return o
#
#def debalphacmp_actualiteeee(a,b):
#    #-1 if <, 0 if =, 1 if >
#    if (not a) and (not b):
#        return 0 #Same then
#    elif (not a) and b:
#        if b[0]=="~":
#            return 1 #~ before even the empty string
#        else:
#            return -1
#    elif a and (not b):
#        if a[0]=="~":
#            return -1 #~ before even the empty string
#        else:
#            return 1
#    else:
#        if a[0]=="~" and (not b[0]=="~"):
#            return -1 #~ before even the empty string
#        elif b[0]=="~" and (not a[0]=="~"):
#            return 1 #~ before even the empty string
#        if a[0].isalpha() and (not b[0].isalpha()):
#            return -1 #letters before others
#        elif (not a[0].isalpha()) and b[0].isalpha():
#            return 1 #letters before others
#        if a[0]!=b[0]:
#            return asciicmp(a[0],b[0])
#        else:
#            return debalphacmp(a[1:],b[1:])
#
#def asciicmp(a,b):
#    #print "******* AC< %r %r"%(a,b)
#    o=asciicmp_actualiteeee(a,b)
#    #print "******* AC> %r "%o
#    return o
#
#def asciicmp_actualiteeee(a,b):
#    return standardcmp(ord(a),ord(b))
#
#def standardcmp(a,b):
#    #print "******* CMP< %r %r"%(a,b)
#    o=standardcmp_actualiteeee(a,b)
#    #print "******* CMP> %r "%o
#    return o
#
#def standardcmp_actualiteeee(a,b):
#    return (a > b) - (a < b)

#Use common sense: use dpkg!
def veriscorrect(tomatch,actual):
    if tomatch==None:
        print "MARZ CALLING EARTG: RETURNING TRUE"
        return True
    a=actual
    b,op=tomatch
    return not os.system('dpkg --compare-versions "%s" "%s" "%s"'%(a,op,b)) #"Not" because 0 is success

import os
if not os.path.exists("majad.pickle"):
    majad=parse_lists(open(repolist))
    
    ubuntudesktop_manifest=open(desktop_manifest)
    
    ubuntudesktop_manifest_data={}
    n=ubuntudesktop_manifest.readline()
    while n:
        n=n.strip().split("\t",1)
        ubuntudesktop_manifest_data[n[0]]=parse_version(n[1])
        n=ubuntudesktop_manifest.readline()
    
    nullver=parse_version(">= 0")
    #Principle is simpler than the code.
    #If a package or a provider (if depend does not specify version) is installed, dependancy is installed.
    #Else get first availible package.
    #Else get first availible provider (if depend does not specify version).
    #Else check if a provider is installed, even if version specified (trust intercompatibility of repositary)
    #Else grab a provider (trust intercompatibility of repositary)
    for m in majad.values():
        for dep in m.__iter2__():
            done=False
            for name,version in dep.name.items():
                if done:
                    break
                if name in ubuntudesktop_manifest_data and veriscorrect(version,ubuntudesktop_manifest_data[name]):
                    dep.installed=True
                    dep.name=name
                    dep.version=version
                    done=True
                    break
                if version==nullver and name in prowviydz:
                    for name2 in prowviydz[name]:
                        if name2 in ubuntudesktop_manifest_data:
                            dep.installed=True
                            dep.name=name2
                            dep.version=version
                            done=True
                            break
            if not done:
                for name,version in dep.name.items():
                    if name in majad and veriscorrect(version,majad[name].version):
                        dep.__dict__.update(majad[name].__dict__)
                        done=True
                        break
            if not done:
                for name,version in dep.name.items():
                    if done:
                        break
                    if version==nullver and name in prowviydz:
                        for name2 in prowviydz[name]:
                            dep.__dict__.update(majad[name2].__dict__)
                            done=True
                            break
            if not done:
                if dep.important:
                    print "Maybe a fail for",dep.name
                for name,version in dep.name.items():
                    if done:
                        break
                    if name in prowviydz:
                        for name2 in prowviydz[name]:
                            dep.__dict__.update(majad[name2].__dict__)
                            done=True
                            break
            if not done:
                if dep.important:
                    print "FAIL!!!!!!!!!! ",dep.name
                else:
                    #print "Unimportant but",dep.name,"failed"
                    dep.installed=True #"Don't bother with me"
            #if done:
            #    print "Attended dependancy",dep.name
    
    import cPickle
    cPickle.dump(majad,open("majad.pickle","wb"),2)
else:
    import cPickle
    majad=cPickle.load(open("majad.pickle","rb"))
#End calculation of majad

l=[]
look4=raw_input("Generate script for: ")
look4z=""

while look4:
    if len(look4z)<80:
        look4z+="_"+look4
    else:
        if not look4z.endswith("_etc"):
            look4z+="_etc"
    l+=list(majad[look4])
    look4=raw_input("Generate script for also (empty to shut up): ")

f=open("get"+look4z+".py","w")

f.write("""
import urllib2,os

def download_file(from_,to_):
    try:
        f=urllib2.urlopen(from_)
    except IOError:
        #Seamless behaviour on dropping support.
        f=urllib2.urlopen(from_.replace("archive.ubuntu","old-releases.ubuntu"))
    if os.path.exists(to_):
        raw_input("Overwrite %r, use Ctrl+C to abort whole download or RETURN to proceed?"%to_)
    t=open(to_,"wb")
    
    c=f.read(1)
    while c:
        t.write(c)
        c=f.read(65536)
    t.close()
    if hasattr(f,"close"):
        f.close()

""")

done=[]
for afile in l:
    if afile not in done:
        f.write("download_file(%r,%r)\n"%(afile,os.path.basename(afile)))
        done.append(afile)
f.close()

f=open("get"+look4z+".txt","w")
waz=[]
for afile in l:
	if afile in waz:
		continue
	print>>f,afile
	waz.append(afile)
f.close()

