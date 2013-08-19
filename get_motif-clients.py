
import urllib2,os

def download_file(from_,to_):
	f=urllib2.urlopen(from_)
	if os.path.exists(to_):
		raw_input("Overwrite %r, use Ctrl+C to abort whole download or RETURN to proceed?"%to_)
	t=open(to_,"wb")
	
	c=f.read(1)
	while c:
		t.write(c)
		c=f.read(1)
	t.close()
	if hasattr(f,"close"):
		f.close()

download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/o/openmotif/motif-clients_2.2.3-4_i386.deb','motif-clients_2.2.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/o/openmotif/libmotif3_2.2.3-4_i386.deb','libmotif3_2.2.3-4_i386.deb')
