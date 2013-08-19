
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

download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/vlc_1.1.4-1ubuntu1_i386.deb','vlc_1.1.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/vlc-nox_1.1.4-1ubuntu1_i386.deb','vlc-nox_1.1.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/a/a52dec/liba52-0.7.4_0.7.4-14ubuntu1_i386.deb','liba52-0.7.4_0.7.4-14ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/liba/libass/libass4_0.9.9-1fakesync1_i386.deb','libass4_0.9.9-1fakesync1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/e/enca/libenca0_1.13-2_i386.deb','libenca0_1.13-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libc/libcddb/libcddb2_1.3.2-2fakesync1_i386.deb','libcddb2_1.3.2-2fakesync1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdca/libdca0_0.0.5-3_i386.deb','libdca0_0.0.5-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvbpsi/libdvbpsi6_0.1.7-1_i386.deb','libdvbpsi6_0.1.7-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdnav/libdvdnav4_4.1.3-7_i386.deb','libdvdnav4_4.1.3-7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libd/libdvdread/libdvdread4_4.1.3-10ubuntu2_i386.deb','libdvdread4_4.1.3-10ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libe/libebml/libebml2_1.0.0+dfsg-0ubuntu1_i386.deb','libebml2_1.0.0+dfsg-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libk/libkate/libkate1_0.3.7-3_i386.deb','libkate1_0.3.7-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libm/libmatroska/libmatroska2_1.0.0+repack-0ubuntu1_i386.deb','libmatroska2_1.0.0+repack-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libm/libmodplug/libmodplug1_0.8.8.1-1ubuntu1_i386.deb','libmodplug1_0.8.8.1-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libm/libmpc/libmpcdec6_0.1~r459-1_i386.deb','libmpcdec6_0.1~r459-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/m/mpeg2dec/libmpeg2-4_0.4.1-3_i386.deb','libmpeg2-4_0.4.1-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/t/twolame/libtwolame0_0.3.12-1_i386.deb','libtwolame0_0.3.12-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libu/libupnp/libupnp3_1.6.6-5_i386.deb','libupnp3_1.6.6-5_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vcdimager/libvcdinfo0_0.7.23-4ubuntu2_i386.deb','libvcdinfo0_0.7.23-4ubuntu2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libc/libcdio/libiso9660-7_0.81-4_i386.deb','libiso9660-7_0.81-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/libvlc5_1.1.4-1ubuntu1_i386.deb','libvlc5_1.1.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/libvlccore4_1.1.4-1ubuntu1_i386.deb','libvlccore4_1.1.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/vlc-data_1.1.4-1ubuntu1_all.deb','vlc-data_1.1.4-1ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/s/sdl-image1.2/libsdl-image1.2_1.2.10-2_i386.deb','libsdl-image1.2_1.2.10-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/libt/libtar/libtar_1.2.11-6_i386.deb','libtar_1.2.11-6_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libv/libva/libva-x11-1_1.0.1-3_i386.deb','libva-x11-1_1.0.1-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/xcb-util/libxcb-keysyms1_0.3.6-1build1_i386.deb','libxcb-keysyms1_0.3.6-1build1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxcb/libxcb-randr0_1.6-1_i386.deb','libxcb-randr0_1.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxcb/libxcb-xv0_1.6-1_i386.deb','libxcb-xv0_1.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/vlc-plugin-notify_1.1.4-1ubuntu1_i386.deb','vlc-plugin-notify_1.1.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/vlc/vlc-plugin-pulse_1.1.4-1ubuntu1_i386.deb','vlc-plugin-pulse_1.1.4-1ubuntu1_i386.deb')
