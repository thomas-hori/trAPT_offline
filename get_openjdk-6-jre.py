
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

download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/openjdk-6-jre_6b20-1.9-0ubuntu1_i386.deb','openjdk-6-jre_6b20-1.9-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/openjdk-6-jre-headless_6b20-1.9-0ubuntu1_i386.deb','openjdk-6-jre-headless_6b20-1.9-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/openjdk-6-jre-lib_6b20-1.9-0ubuntu1_all.deb','openjdk-6-jre-lib_6b20-1.9-0ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/c/ca-certificates-java/ca-certificates-java_20100412_all.deb','ca-certificates-java_20100412_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/t/tzdata/tzdata-java_2010l-1_all.deb','tzdata-java_2010l-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-common/java-common_0.38_all.deb','java-common_0.38_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/icedtea-6-jre-cacao_6b20-1.9-0ubuntu1_i386.deb','icedtea-6-jre-cacao_6b20-1.9-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/g/giflib/libgif4_4.1.6-9_i386.deb','libgif4_4.1.6-9_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-access-bridge/libaccess-bridge-java-jni_1.26.2-5_i386.deb','libaccess-bridge-java-jni_1.26.2-5_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-access-bridge/libaccess-bridge-java_1.26.2-5_all.deb','libaccess-bridge-java_1.26.2-5_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-common/default-jre_1.6-38_i386.deb','default-jre_1.6-38_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-common/default-jre-headless_1.6-38_i386.deb','default-jre-headless_1.6-38_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/openjdk-6-jre-headless_6b20-1.9-0ubuntu1_i386.deb','openjdk-6-jre-headless_6b20-1.9-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/openjdk-6-jre-lib_6b20-1.9-0ubuntu1_all.deb','openjdk-6-jre-lib_6b20-1.9-0ubuntu1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/c/ca-certificates-java/ca-certificates-java_20100412_all.deb','ca-certificates-java_20100412_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/t/tzdata/tzdata-java_2010l-1_all.deb','tzdata-java_2010l-1_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-common/java-common_0.38_all.deb','java-common_0.38_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/o/openjdk-6/icedtea-6-jre-cacao_6b20-1.9-0ubuntu1_i386.deb','icedtea-6-jre-cacao_6b20-1.9-0ubuntu1_i386.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/j/java-common/java-common_0.38_all.deb','java-common_0.38_all.deb')
download_file('http://archive.ubuntu.com/ubuntu/pool/main/t/ttf-dejavu/ttf-dejavu-extra_2.31-1_all.deb','ttf-dejavu-extra_2.31-1_all.deb')
