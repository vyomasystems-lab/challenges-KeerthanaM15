module FIFO(wr_clk,rd_clk,reset,data_i,data_o,fifo_full,fifo_empty,wr_en,rd_en);
  parameter fifo_depth=8;
  output reg [fifo_depth-1:0]data_o;
  output reg fifo_full,fifo_empty;
  input [fifo_depth-1:0]data_i;
  input wr_clk,rd_clk,reset,wr_en,rd_en;
  reg [fifo_depth-1:0]mem[fifo_depth-1:0];
  reg [3:0]wr_ptr=4'b0;
  reg [3:0]rd_ptr=4'b0;
   always@(posedge wr_clk)
    begin
      if(reset)
        begin
          data_o=0;
        end
      else
            begin
              if(wr_en)
                begin
        		mem[wr_ptr]=data_i;
          		wr_ptr=wr_ptr+1;
              	if(wr_ptr==4'b1000)
                  begin
             		wr_ptr=0;
                    if(data_i!=0)
                      begin
                    	fifo_full=1;
                    	$display("fifo queue is full, impossible to load new values");
                      end
                    else
                      fifo_full=0;
                  end
              else
              fifo_full=0;
                end
        end
    end
  always@(negedge rd_clk)
    begin
      if(reset)
        data_o=0;
      else
        begin
          if(rd_en)
            begin
      data_o=mem[rd_ptr];
      rd_ptr=rd_ptr+1;
          if(rd_ptr==4'b1000)
        begin
          rd_ptr=0;
          if(data_o!=0)
            begin
          		fifo_empty=1;
          		$display("everything is read, no new values to read");
            end
          else
            fifo_empty=0;
        end
          else
            fifo_empty=0;
        end
        end
    end
endmodule

