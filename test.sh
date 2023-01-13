#!/usr/bin/env sh

mkdir -p rsc
echo "some-input" > rsc/plain.txt

_key="some-key"

python3 ./python/deCryptor.py rsc/plain.txt rsc/enc.txt "$_key"
node ./javascript/deCryptor.js rsc/enc.txt rsc/dec.txt "$_key"

if diff rsc/plain.txt rsc/dec.txt; then
  echo "passed"
fi
