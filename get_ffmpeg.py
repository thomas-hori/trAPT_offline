
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/ffmpeg/ffmpeg_0.6-2ubuntu6_i386.deb','ffmpeg_0.6-2ubuntu6_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/f/ffmpeg-extra/libavfilter-extra-1_0.6-2ubuntu3_i386.deb','libavfilter-extra-1_0.6-2ubuntu3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/f/ffmpeg-extra/libavcodec-extra-52_0.6-2ubuntu3_i386.deb','libavcodec-extra-52_0.6-2ubuntu3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/f/ffmpeg-extra/libavutil-extra-50_0.6-2ubuntu3_i386.deb','libavutil-extra-50_0.6-2ubuntu3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/d/dirac/libdirac-encoder0_1.0.2-3_i386.deb','libdirac-encoder0_1.0.2-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/l/lame/libmp3lame0_3.98.4-0ubuntu1_i386.deb','libmp3lame0_3.98.4-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/o/openjpeg/libopenjpeg2_1.3+dfsg-4_i386.deb','libopenjpeg2_1.3+dfsg-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/x264/libx264-98_0.98.1653+git88b90d9-3_i386.deb','libx264-98_0.98.1653+git88b90d9-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/x/xvidcore/libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb','libxvidcore4_1.2.2+debian-1ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/multiverse/f/ffmpeg-extra/libswscale-extra-0_0.6-2ubuntu3_i386.deb','libswscale-extra-0_0.6-2ubuntu3_i386.deb')
