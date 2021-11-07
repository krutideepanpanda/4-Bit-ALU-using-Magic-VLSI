# EC302-project

This is a simple ALU designed using the pharosc standard library. The ALU supports the following operations :

- Addition
- Bitwise AND
- Bitwise OR

The ALU was extracted and converted to a **.sim** file using **Magic VLSI**. The generated **.sim** file was then simulated using the switch level simulator **IRSIM**.

The python script in **cmdGenerate.py** generates a **.cmd** file to be used with **IRSIM** to verify our ALU. This can initiated using the **verify.sh** bash file, which automatically runs the required commands in the terminal.

To start simulation type the following in the CLI -

```
bash verify.sh
```

