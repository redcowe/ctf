#!/bin/zsh
echo Banner Grabbing...
for i in {1..65535} ; do
    RESULT="$(nc -w 1 "tethys.picoctf.net" ${i})"
    if [ ! -z "${RESULT}" ] ; then
        echo "Found on port ${i}"
        echo -e "${RESULT}\n" >> output.txt
    fi
done