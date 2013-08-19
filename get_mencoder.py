
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

download_file('http://archive.ubuntu.com/ubuntu/pool/universe/m/mplayer/mencoder_1.0~rc4~try1.dsfg1-1ubuntu1_i386.deb','mencoder_1.0~rc4~try1.dsfg1-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/m/mplayer/mplayer_1.0~rc4~try1.dsfg1-1ubuntu1_i386.deb','mplayer_1.0~rc4~try1.dsfg1-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdca/libdca0_0.0.5-3_i386.deb','libdca0_0.0.5-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/d/directfb/libdirectfb-1.2-9_1.2.10.0-4ubuntu2_i386.deb','libdirectfb-1.2-9_1.2.10.0-4ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/t/tslib/libts-0.0-0_1.0-7build1_i386.deb','libts-0.0-0_1.0-7build1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/t/tslib/tsconf_1.0-7build1_all.deb','tsconf_1.0-7build1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdnav/libdvdnav4_4.1.3-7_i386.deb','libdvdnav4_4.1.3-7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdread/libdvdread4_4.1.3-10ubuntu2_i386.deb','libdvdread4_4.1.3-10ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdread/libdvdread4_4.1.3-10ubuntu2_i386.deb','libdvdread4_4.1.3-10ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdnav/libdvdnav4_4.1.3-7_i386.deb','libdvdnav4_4.1.3-7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/e/enca/libenca0_1.13-2_i386.deb','libenca0_1.13-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/giflib/libgif4_4.1.6-9_i386.deb','libgif4_4.1.6-9_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/l/lzo2/liblzo2-2_2.03-2_i386.deb','liblzo2-2_2.03-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/l/lame/libmp3lame0_3.98.4-0ubuntu1_i386.deb','libmp3lame0_3.98.4-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/s/svgalib/libsvga1_1.4.3-29_i386.deb','libsvga1_1.4.3-29_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libv/libvdpau/libvdpau1_0.4-5ubuntu1_i386.deb','libvdpau1_0.4-5ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/x264/libx264-98_0.98.1653+git88b90d9-3_i386.deb','libx264-98_0.98.1653+git88b90d9-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/xvidcore/libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb','libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdca/libdca0_0.0.5-3_i386.deb','libdca0_0.0.5-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdnav/libdvdnav4_4.1.3-7_i386.deb','libdvdnav4_4.1.3-7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdread/libdvdread4_4.1.3-10ubuntu2_i386.deb','libdvdread4_4.1.3-10ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdread/libdvdread4_4.1.3-10ubuntu2_i386.deb','libdvdread4_4.1.3-10ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdnav/libdvdnav4_4.1.3-7_i386.deb','libdvdnav4_4.1.3-7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/e/enca/libenca0_1.13-2_i386.deb','libenca0_1.13-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/giflib/libgif4_4.1.6-9_i386.deb','libgif4_4.1.6-9_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/l/lzo2/liblzo2-2_2.03-2_i386.deb','liblzo2-2_2.03-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/l/lame/libmp3lame0_3.98.4-0ubuntu1_i386.deb','libmp3lame0_3.98.4-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/x264/libx264-98_0.98.1653+git88b90d9-3_i386.deb','libx264-98_0.98.1653+git88b90d9-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/xvidcore/libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb','libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb')
