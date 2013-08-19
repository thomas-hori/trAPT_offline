
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/xorg/xorg-dev_7.5+6ubuntu3_all.deb','xorg-dev_7.5+6ubuntu3_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libd/libdmx/libdmx-dev_1.1.0-2_i386.deb','libdmx-dev_1.1.0-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libd/libdmx/libdmx1_1.1.0-2_i386.deb','libdmx1_1.1.0-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libx11/libx11-dev_1.3.3-3ubuntu1_i386.deb','libx11-dev_1.3.3-3ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxau/libxau-dev_1.0.6-1_i386.deb','libxau-dev_1.0.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-core/x11proto-core-dev_7.0.17-1_all.deb','x11proto-core-dev_7.0.17-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxdmcp/libxdmcp-dev_1.0.3-2_i386.deb','libxdmcp-dev_1.0.3-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-input/x11proto-input-dev_2.0-2_all.deb','x11proto-input-dev_2.0-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-kb/x11proto-kb-dev_1.0.4-1_all.deb','x11proto-kb-dev_1.0.4-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/xtrans/xtrans-dev_1.2.5-1_all.deb','xtrans-dev_1.2.5-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxcb/libxcb1-dev_1.6-1_i386.deb','libxcb1-dev_1.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libp/libpthread-stubs/libpthread-stubs0-dev_0.3-2_i386.deb','libpthread-stubs0-dev_0.3-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libp/libpthread-stubs/libpthread-stubs0_0.3-2_i386.deb','libpthread-stubs0_0.3-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-dmx/x11proto-dmx-dev_2.3-2_all.deb','x11proto-dmx-dev_2.3-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libf/libfontenc/libfontenc-dev_1.0.5-2_i386.deb','libfontenc-dev_1.0.5-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/z/zlib/zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb','zlib1g-dev_1.2.3.4.dfsg-3ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libf/libfs/libfs-dev_1.0.2-1build1_i386.deb','libfs-dev_1.0.2-1build1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-fonts/x11proto-fonts-dev_2.1.0-1_all.deb','x11proto-fonts-dev_2.1.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libi/libice/libice-dev_1.0.6-1_i386.deb','libice-dev_1.0.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libs/libsm/libsm-dev_1.1.1-1_i386.deb','libsm-dev_1.1.1-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxaw/libxaw7-dev_1.0.7-1_i386.deb','libxaw7-dev_1.0.7-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxmu/libxmu-dev_1.0.5-1_i386.deb','libxmu-dev_1.0.5-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxext/libxext-dev_1.1.2-1_i386.deb','libxext-dev_1.1.2-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xext/x11proto-xext-dev_7.1.1-2_all.deb','x11proto-xext-dev_7.1.1-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxt/libxt-dev_1.0.7-1_i386.deb','libxt-dev_1.0.7-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxmu/libxmu-headers_1.0.5-1_all.deb','libxmu-headers_1.0.5-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxpm/libxpm-dev_3.5.8-1_i386.deb','libxpm-dev_3.5.8-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxcomposite/libxcomposite-dev_0.4.2-1_i386.deb','libxcomposite-dev_0.4.2-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxfixes/libxfixes-dev_4.0.5-1_i386.deb','libxfixes-dev_4.0.5-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-fixes/x11proto-fixes-dev_4.1.1-2_all.deb','x11proto-fixes-dev_4.1.1-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-composite/x11proto-composite-dev_0.4.1-1_all.deb','x11proto-composite-dev_0.4.1-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxcursor/libxcursor-dev_1.1.10-2_i386.deb','libxcursor-dev_1.1.10-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxrender/libxrender-dev_0.9.6-1_i386.deb','libxrender-dev_0.9.6-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-render/x11proto-render-dev_0.11-1_all.deb','x11proto-render-dev_0.11-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxdamage/libxdamage-dev_1.1.3-1_i386.deb','libxdamage-dev_1.1.3-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-damage/x11proto-damage-dev_1.2.0-1_all.deb','x11proto-damage-dev_1.2.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxfont/libxfont-dev_1.4.2-1_i386.deb','libxfont-dev_1.4.2-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/freetype/libfreetype6-dev_2.4.2-2_i386.deb','libfreetype6-dev_2.4.2-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/xft/libxft-dev_2.1.14-2ubuntu1_i386.deb','libxft-dev_2.1.14-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/fontconfig/libfontconfig1-dev_2.8.0-2ubuntu1_i386.deb','libfontconfig1-dev_2.8.0-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/e/expat/libexpat1-dev_2.0.1-7ubuntu1_i386.deb','libexpat1-dev_2.0.1-7ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxi/libxi-dev_1.3-4_i386.deb','libxi-dev_1.3-4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxinerama/libxinerama-dev_1.1-3_i386.deb','libxinerama-dev_1.1-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xinerama/x11proto-xinerama-dev_1.2-2_all.deb','x11proto-xinerama-dev_1.2-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxkbfile/libxkbfile-dev_1.0.6-2_i386.deb','libxkbfile-dev_1.0.6-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxmu/libxmuu-dev_1.0.5-1_i386.deb','libxmuu-dev_1.0.5-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxrandr/libxrandr-dev_1.3.0-3_i386.deb','libxrandr-dev_1.3.0-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-randr/x11proto-randr-dev_1.3.1-1_all.deb','x11proto-randr-dev_1.3.1-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxres/libxres-dev_1.0.4-1_i386.deb','libxres-dev_1.0.4-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-resource/x11proto-resource-dev_1.1.0-1_all.deb','x11proto-resource-dev_1.1.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxss/libxss-dev_1.2.0-2_i386.deb','libxss-dev_1.2.0-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-scrnsaver/x11proto-scrnsaver-dev_1.2.0-2_all.deb','x11proto-scrnsaver-dev_1.2.0-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxtst/libxtst-dev_1.1.0-3_i386.deb','libxtst-dev_1.1.0-3_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-record/x11proto-record-dev_1.14-2_all.deb','x11proto-record-dev_1.14-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxv/libxv-dev_1.0.5-1_i386.deb','libxv-dev_1.0.5-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-video/x11proto-video-dev_2.3.0-1_all.deb','x11proto-video-dev_2.3.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxvmc/libxvmc-dev_1.0.5-1ubuntu1_i386.deb','libxvmc-dev_1.0.5-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxxf86dga/libxxf86dga-dev_1.1.1-2_i386.deb','libxxf86dga-dev_1.1.1-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xf86dga/x11proto-xf86dga-dev_2.1-2_all.deb','x11proto-xf86dga-dev_2.1-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libx/libxxf86vm/libxxf86vm-dev_1.1.0-2_i386.deb','libxxf86vm-dev_1.1.0-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xf86vidmode/x11proto-xf86vidmode-dev_2.3-2_all.deb','x11proto-xf86vidmode-dev_2.3-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-bigreqs/x11proto-bigreqs-dev_1.1.0-1_all.deb','x11proto-bigreqs-dev_1.1.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-gl/x11proto-gl-dev_1.4.11-1_all.deb','x11proto-gl-dev_1.4.11-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xcmisc/x11proto-xcmisc-dev_1.2.0-1_all.deb','x11proto-xcmisc-dev_1.2.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xf86bigfont/x11proto-xf86bigfont-dev_1.2.0-2_all.deb','x11proto-xf86bigfont-dev_1.2.0-2_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-xf86dri/x11proto-xf86dri-dev_2.1.0-1_all.deb','x11proto-xf86dri-dev_2.1.0-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/xorg-server/xserver-xorg-dev_1.9.0-0ubuntu7_i386.deb','xserver-xorg-dev_1.9.0-0ubuntu7_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/p/pixman/libpixman-1-dev_0.18.4-1_i386.deb','libpixman-1-dev_0.18.4-1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/x/x11proto-dri2/x11proto-dri2-dev_2.3-1_all.deb','x11proto-dri2-dev_2.3-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libp/libpciaccess/libpciaccess-dev_0.12.0-1_i386.deb','libpciaccess-dev_0.12.0-1_i386.deb')
