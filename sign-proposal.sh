#!/bin/bash
proposal="2016-02.md"

gpg --output ${proposal}.sig -a --detach-sig ${proposal}
