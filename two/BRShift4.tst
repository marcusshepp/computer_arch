load BRShift4.hdl,
output-file BRShift4.out,
compare-to BRShift4.cmp,
output-list time%S1.4.1 in%D1.6.1 load%B2.1.2 shift%D2.1.2 out%D1.6.1;

set in 0,
set load 0,
tick,
output;
tock,
output;

set load 1,
set in 5,
tick,
output;
tock,
output;

set load 0,
set shift 1,
tick,
output;
tock,
output;

tick,
output;
tock,
output;

tick,
output;
tock,
output;

set load 1,
set shift 0,
set in 7,
tick,
output;
tock,
output;

set load 0,
set shift 1,
tick,
output;
tock,
output;

tick,
output;
tock,
output;

tick,
output;
tock,
output;

tick,
output;
tock,
output;

tick,
output;
tock,
output;


