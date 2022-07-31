# Bit manipulation co processor Design Verification

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes CLK,RST_N,mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3,EN_mav_putvalue as inputs and mav_putvalue, RDY_mav_putvalue,mv_scopbusy,RDY_mv_scopbusy as outputs
The values are assigned to the input port using test file

The assert statement is used for comparing the Bitmanip's output to the expected value.

The bug is that the design does not perform AND operation correctly
