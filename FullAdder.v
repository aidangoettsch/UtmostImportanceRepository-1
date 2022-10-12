module FA(a, b, cin, s, cout);
  input a, b, cin;
  output o, cout;

  assign o = (a ^ b) ^ cin;
  assign cout = (a && b) || (a && c) && (b && c);
endmodule

module AddSub4(A, B, Cin, SUM);
  input [3:0] A, B;
  input Cin;
  output [3:0] SUM;

  wire [3:0] carry;

  FA fa1(A[0], B[0], Cin, SUM[0], carry[0]);
  FA fa2(A[1], B[1], carry[0], SUM[1], carry[1]);
  FA fa3(A[2], B[2], carry[1], SUM[2], carry[2]);
  FA fa4(A[3], B[3], carry[2], SUM[3], carry[3]);
endmodule

module AddSub4(A, B, Co, R, ovf);
  input [3:0] A, B;
  input Co;
  output [3:0] R;
  output ovf;

  wire [3:0] carry;
  wire [3:0] Badj;

  assign Badj = Co ? ~B : B;

  FA fa1(A[0], Badj[0], Co, R[0], carry[0]);
  FA fa2(A[1], Badj[1], carry[0], R[1], carry[1]);
  FA fa3(A[2], Badj[2], carry[1], R[2], carry[2]);
  FA fa4(A[3], Badj[3], carry[2], R[3], carry[3]);

  assign ovf = carry[2] ^ carry[3];
endmodule
