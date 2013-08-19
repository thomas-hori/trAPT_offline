
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/glib2.0/libglib2.0-dev_2.26.0-0ubuntu1_i386.deb','libglib2.0-dev_2.26.0-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/glib2.0/libglib2.0-bin_2.26.0-0ubuntu1_i386.deb','libglib2.0-bin_2.26.0-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/z/zlib/zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb','zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libd/libdrm/libdrm-dev_2.4.21-1ubuntu2_i386.deb','libdrm-dev_2.4.21-1ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libd/libdrm/libkms1_2.4.21-1ubuntu2_i386.deb','libkms1_2.4.21-1ubuntu2_i386.deb')
