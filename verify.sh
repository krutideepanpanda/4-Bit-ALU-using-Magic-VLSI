#!/bin/bash

python3 cmdGenerate.py
echo "CMD files generated"

irsim scmos100.prm ALU.sim -cmd/test.cmd
echo "IRSIM execution finished"

python3 logVerify.py
echo "Verification complete"
echo "Ending procedure"