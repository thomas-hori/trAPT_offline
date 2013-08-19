
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/fontforge/fontforge_0.0.20090923-2ubuntu1_i386.deb','fontforge_0.0.20090923-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/fontforge/libfontforge1_0.0.20090923-2ubuntu1_i386.deb','libfontforge1_0.0.20090923-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/giflib/libgif4_4.1.6-9_i386.deb','libgif4_4.1.6-9_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libs/libspiro/libspiro0_20071029-2build1_i386.deb','libspiro0_20071029-2build1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libu/libuninameslist/libuninameslist0_0.0.20091231-1_i386.deb','libuninameslist0_0.0.20091231-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/fontforge/libgdraw4_0.0.20090923-2ubuntu1_i386.deb','libgdraw4_0.0.20090923-2ubuntu1_i386.deb')
