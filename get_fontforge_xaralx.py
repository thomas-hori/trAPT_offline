
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
download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/x/xaralx/xaralx_0.7r1785-2ubuntu2_i386.deb','xaralx_0.7r1785-2ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/w/wxwidgets2.6/libwxbase2.6-0_2.6.3.2.2-5ubuntu1_i386.deb','libwxbase2.6-0_2.6.3.2.2-5ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/w/wxwidgets2.6/libwxgtk2.6-0_2.6.3.2.2-5ubuntu1_i386.deb','libwxgtk2.6-0_2.6.3.2.2-5ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/x/xaralx/xaralx-svg_0.7r1785-2ubuntu2_i386.deb','xaralx-svg_0.7r1785-2ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/i/imagemagick/imagemagick_6.6.2.6-1ubuntu1_i386.deb','imagemagick_6.6.2.6-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/i/imagemagick/libmagickcore3-extra_6.6.2.6-1ubuntu1_i386.deb','libmagickcore3-extra_6.6.2.6-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/graphviz/libcdt4_2.26.3-4_i386.deb','libcdt4_2.26.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/graphviz/libgraph4_2.26.3-4_i386.deb','libgraph4_2.26.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/graphviz/libgvc5_2.26.3-4_i386.deb','libgvc5_2.26.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/graphviz/libpathplan4_2.26.3-4_i386.deb','libpathplan4_2.26.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/graphviz/libxdot4_2.26.3-4_i386.deb','libxdot4_2.26.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/n/netpbm-free/netpbm_10.0-12.2_i386.deb','netpbm_10.0-12.2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/n/netpbm-free/libnetpbm10_10.0-12.2_i386.deb','libnetpbm10_10.0-12.2_i386.deb')
