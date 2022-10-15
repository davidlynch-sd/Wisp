#!/bin/sh

set -x
 
python3 src/main.py src/test.wisp bin/main
strace ./bin/main
objdump -d bin/main
