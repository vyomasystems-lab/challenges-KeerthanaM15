# Pattern_detector Design Verification

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in one bit input inp_bit, and clock, reset and one bit output seq_seen

The values are assigned to the input port using 
```
"dut.inp_bit.value" takes the sequence of 101011011
```

The assert statement is used for comparing the pattern_detector's output to the expected value.

The error occured as the actual design must be a overlapped sequence detector but the bug is that design given is designed for Non-overlapped sequence detector


## Design Fix
Updating the design and re-running the test makes the test pass.


The updated design is checked in as seq_detect_1011.v


following output is found

25000.00ns INFO     input=00001 output=00000
 35000.00ns INFO     input=00000 output=00000
 45000.00ns INFO     input=00001 output=00000
 55000.00ns INFO     input=00000 output=00000
 65000.00ns INFO     input=00001 output=00000
 75000.00ns INFO     input=00001 output=00001
 85000.00ns INFO     input=00000 output=00000
 95000.00ns INFO     input=00001 output=00000
105000.00ns INFO     input=00001 output=00001
105000.00ns INFO     test_seq_bug1 passed
