# Multiplexer Design Verification

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 32 2-bit inputs inp0 to inp31, 5 - bit selection lines sel and gives 2-bit output out

The values are assigned to the input port using 
```
dut.inp12.value = 3
dut.sel.value = 12
```

The assert statement is used for comparing the Multiplexers's output to the expected value.

The following error is seen:
```
 assert dut.out.value == I[temp], "selected value is incorrect: {SEL} {INPUT} != {OUT}, expected value = {EXP}".format(SEL=int(dut.sel.value), INPUT=I[temp], OUT=int(dut.out.value), EXP=I[temp])
                     AssertionError: selected value is incorrect: 12 3 != 1, expected value = 3
```
## Test Scenario 
- Test Inputs: inp12=3 sel=12
- Expected Output: out=3
- Observed Output in the DUT dut.out=1

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

``` buggy lines are found and image is inserted```

For the Multiplexer design, the select line 5'b01100 is not given in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as mux.v

```updated design image is included```
