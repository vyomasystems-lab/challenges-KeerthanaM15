# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.wr_clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    clock = Clock(dut.rd_clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut.reset.wr_en=1
    await FallingEdge(dut.wr_clk)
    dut.data_i.value=11
    await FallingEdge(dut.wr_clk)
    dut.data_i.value=7
    await FallingEdge(dut.wr_clk)
    dut._log.info(f'input={int(dut.data_i.value):05} output={int(dut.data_o.value):05}')

    dut.reset.rd_en=1
    await FallingEdge(dut.rd_clk)
    dut._log.info(f'input={int(dut.data_i.value):05} output={int(dut.data_o.value):05}')

    