import hashlib
import sys

filename = sys.argv[1]
md5 = open("MD5-"+filename+".txt", "w")
md5.write(hashlib.md5(filename).hexdigest())
md5.close()

sha1 = open("SHA1-"+filename+".txt", "w")
sha1.write(hashlib.sha1(filename).hexdigest())
sha1.close()