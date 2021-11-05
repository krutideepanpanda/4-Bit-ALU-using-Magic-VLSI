#!/bin/bash

python cmdGenerate.py
echo "CMD files generated, proceeding to execute in irsim"

irsim scmos100.prm mag/ALU.mag -cmd/test/cmd
echo "IRSIM execution finished, proceeding to verification"