
import urllib2

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

download_file('http://archive.ubuntu.com/ubuntu/pool/universe/l/lesstif2/lesstif-bin_0.95.2-1_i386.deb','lesstif-bin_0.95.2-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/l/lesstif2/lesstif2_0.95.2-1_i386.deb','lesstif2_0.95.2-1_i386.deb')
