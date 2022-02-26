Name: Conner Erickson 
Email: cserick3@asu.edu 
ASU ID: 1214908565
Date: February 24, 2022

PartitionTypes.JSON Credit: @CJ on Discord

High Level Description: The program takes a forensic Master Boot Record as a command line argument, verifies that it is untampered with by generating MD5 and SHA checksums and comparing them with expected ones, and prints out information about each partition contained in the MBR (hex value, type, start sector address in decimal, partition size in decimal). It finally prints out the last 8 bytes of each non-zero partition's boot record.

Program Execution Instructions: First make the file using the command "make". This will translate MBRInfo.py to the executable mbr_info. Then, execute the command with the filename you are analyzing as the second command line argument.
Ex: ./mbr_info input.raw