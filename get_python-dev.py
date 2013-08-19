
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/p/python-defaults/python-dev_2.6.6-2ubuntu1_all.deb','python-dev_2.6.6-2ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/p/python2.6/python2.6-dev_2.6.6-5ubuntu1_i386.deb','python2.6-dev_2.6.6-5ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl-dev_0.9.8o-1ubuntu4_i386.deb','libssl-dev_0.9.8o-1ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl0.9.8_0.9.8o-1ubuntu4_i386.deb','libssl0.9.8_0.9.8o-1ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/z/zlib/zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb','zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb')
