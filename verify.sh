#!/bin/bash

python3 cmdGenerate.py
echo "CMD files generated, proceeding to execute in irsim"

irsim scmos100.prm ALU.sim -cmd/test.cmd
echo "IRSIM execution finished, proceeding to verification"

python3 logVerify.py
echo "Verification complete"
echo "Ending procedure"