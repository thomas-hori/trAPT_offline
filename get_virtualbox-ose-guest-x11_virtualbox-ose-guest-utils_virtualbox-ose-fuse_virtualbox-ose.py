
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

download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-guest-x11_3.2.8-dfsg-2ubuntu1_i386.deb','virtualbox-ose-guest-x11_3.2.8-dfsg-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-guest-utils_3.2.8-dfsg-2ubuntu1_i386.deb','virtualbox-ose-guest-utils_3.2.8-dfsg-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-guest-dkms_3.2.8-dfsg-2ubuntu1_all.deb','virtualbox-ose-guest-dkms_3.2.8-dfsg-2ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/d/dkms/dkms_2.1.1.2-3ubuntu1_all.deb','dkms_2.1.1.2-3ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/p/patch/patch_2.6-2ubuntu1_i386.deb','patch_2.6-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/f/fakeroot/fakeroot_1.14.4-1ubuntu1_i386.deb','fakeroot_1.14.4-1ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-fuse_3.2.8-dfsg-2ubuntu1_i386.deb','virtualbox-ose-fuse_3.2.8-dfsg-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose_3.2.8-dfsg-2ubuntu1_i386.deb','virtualbox-ose_3.2.8-dfsg-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl0.9.8_0.9.8o-1ubuntu4_i386.deb','libssl0.9.8_0.9.8o-1ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/libv/libvncserver/libvncserver0_0.9.7-2_i386.deb','libvncserver0_0.9.7-2_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-dkms_3.2.8-dfsg-2ubuntu1_all.deb','virtualbox-ose-dkms_3.2.8-dfsg-2ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/universe/v/virtualbox-ose/virtualbox-ose-qt_3.2.8-dfsg-2ubuntu1_i386.deb','virtualbox-ose-qt_3.2.8-dfsg-2ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqt4-network_4.7.0-0ubuntu4_i386.deb','libqt4-network_4.7.0-0ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqt4-dbus_4.7.0-0ubuntu4_i386.deb','libqt4-dbus_4.7.0-0ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqt4-xml_4.7.0-0ubuntu4_i386.deb','libqt4-xml_4.7.0-0ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqtcore4_4.7.0-0ubuntu4_i386.deb','libqtcore4_4.7.0-0ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqt4-opengl_4.7.0-0ubuntu4_i386.deb','libqt4-opengl_4.7.0-0ubuntu4_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/q/qt4-x11/libqtgui4_4.7.0-0ubuntu4_i386.deb','libqtgui4_4.7.0-0ubuntu4_i386.deb')
