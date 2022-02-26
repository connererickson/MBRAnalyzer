#!/usr/bin/env python3
import hashlib
import sys
import json

filename = sys.argv[1]
#open the MBR
file = open(filename, "rb")
content = file.read()

#creates md5 and sha1 checksums for the arg filename
md5file = open("MD5-"+filename+".txt", "w")
md5 = hashlib.md5()
md5.update(content)
md5file.write(md5.hexdigest())
md5file.close()

sha1file = open("SHA1-"+filename+".txt", "w")
sha1 = hashlib.sha1()
sha1.update(content)
sha1file.write(sha1.hexdigest())
sha1file.close()

#read json to dict, data structure is a list of dicts
f = open("PartitionTypes.json",)
partitionTypes = json.load(f)

#stores the start index of each partition's boot sector
partitionIndex = [0, 0, 0, 0]

#bootstrap code contained in first 446 bytes, need to skip
file.seek(446, 0)

#pull partition data from each 16-byte sector in the partition table
for i in range(4):
    content = file.read(16)
    partition = content.hex()
    #find lba value and convert to 10-digit integer
    lba = int.from_bytes(content[8:12], "little")
    lbaStr = str(lba).zfill(10)
    #find size value and convert to 10-digit integer
    size = int.from_bytes(content[12:14], "little")
    sizeStr = str(size).zfill(10)
    #find type, match to item in dictionary
    type = partition[8:10]
    partitionType = next((item for item in partitionTypes if str(item["hex"]) == type), None)
    #if partition is not empty
    if(type != "00"):
        print("(" + type + ") " + partitionType["desc"] + ", " + lbaStr + ", " + sizeStr)
        #add partition data to partition data structure here
        partitionIndex[i] = lba*512

for i in range(len(partitionIndex)):
    if(partitionIndex[i] != 0):
        print("Partition number: " + str(i+1))
        #retrieve last 8 bytes of boot record
        file.seek(partitionIndex[i]+504, 0)
        content = file.read(8)
        string = content.hex()
        print("Last 8 bytes of boot record: " + string[0:2] + " " + string[2:4] + " " + string[4:6] + " " + string[6:8] + " " + string[8:10] + " " + string[10:12] + " " + string[12:14] + " " + string[14:16])

# close the mbr
file.close()
