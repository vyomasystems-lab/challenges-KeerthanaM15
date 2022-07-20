# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    I0 = 0
    I1 = 1
    I2 = 2
    I3 = 3

    I4 = 0
    I5 = 1
    I6 = 2
    I7 = 3

    I8 = 0
    I9 = 1
    I10 = 2
    I11 = 3

    I12 = 0
    I13 = 1
    I14 = 2
    I15 = 3

    I16 = 3
    I17 = 2
    I18 = 1
    I19 = 0

    I20 = 3
    I21 = 2
    I22 = 1
    I23 = 0

    I24 = 3
    I25 = 2
    I26 = 1
    I27 = 0

    I28 = 3
    I29 = 2
    I30 = 1
    I31 = 0

    SEL=14

    dut.inp0.value = I0
    dut.inp1.value = I1
    dut.inp2.value = I2
    dut.inp3.value = I3

    dut.inp4.value = I4
    dut.inp5.value = I5
    dut.inp6.value = I6
    dut.inp7.value = I7

    dut.inp8.value = I8
    dut.inp9.value = I9
    dut.inp10.value = I10
    dut.inp11.value = I11

    dut.inp12.value = I12
    dut.inp13.value = I13
    dut.inp14.value = I14
    dut.inp15.value = I15

    dut.inp16.value = I16
    dut.inp17.value = I17
    dut.inp18.value = I18
    dut.inp19.value = I19

    dut.inp20.value = I20
    dut.inp21.value = I21
    dut.inp22.value = I22
    dut.inp23.value = I23

    dut.inp24.value = I24
    dut.inp25.value = I25
    dut.inp26.value = I26
    dut.inp27.value = I27

    dut.inp28.value = I28
    dut.inp29.value = I29
    dut.inp30.value = I30
    dut.inp31.value = I31

    dut.sel.value = SEL

    await Timer(2,units='ns')
    dut._log.info(f'SEL={SEL:05} INPUT={I14:05} model={I14:05} DUT={int(dut.out.value):05}')
    assert dut.out.value == I14, "selected value is incorrect: {SEL} {I14} != {out}, expected value = {EXP}".format(SEL=int(dut.sel.value), I14=int(dut.inp14.value), out=int(dut.out.value), EXP=I14)
    
    cocotb.log.info('##### CTB: Develop your test here ########')
