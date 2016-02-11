#!/bin/bash

SINCE="2016-01-01"
AUTHOR="Fabian Schuh"

pushd ~/BitShares

for d in python-graphene docs.bitshares.eu graphene-ui bsips Committee/proposals Committee/Instructions
do
 echo "$d:"
 git -C "$d" log --author="$AUTHOR" --since="$SINCE" --oneline | wc -l
 git -C "$d" log --author="$AUTHOR" --since="$SINCE" --pretty=tformat: --numstat | gawk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s removed lines: %s total lines: %s\n", add, subs, loc }' -
done

popd
