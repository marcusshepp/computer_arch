load RAM32.hdl,
output-file RAM32.out,
compare-to RAM32.cmp,
output-list time%S1.4.1 in%D1.6.1 load%B2.1.2 address%D2.3.2 out%D1.6.1;

set in 0,
set load 0,
set address 0,
tick,
output;
tock,
output;

set load 1,
tick,
output;
tock,
output;

set in 1313,
set load 0,
tick,
output;
tock,
output;

set load 1,
set address 13,
tick,
output;
tock,
output;

set load 0,
set address 0,
tick,
output;
tock,
output;

set load 1,
tick,
output;
tock,
output;

set load 0,
tick,
output;
tock,
output;

set address 13,
eval,
output;

set in 6363,
tick,
output;
tock,
output;

set load 0,
tick,
output;
tock,
output;

set load 1,
set in %B0101010101010101,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
tick,
output,
tock,
output;
set address %B10101,
tick,
output,
tock,
output;
set address %B10101,
tick,
output,
tock,
output;
set address %B10110,
tick,
output,
tock,
output;
set address %B10110,
tick,
output,
tock,
output;
set address %B10111,
tick,
output,
tock,
output;
set address %B10111,
tick,
output,
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10100,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10100,
set in %B0101010101010101,
tick,
output,
tock,
output;
set address %B10100,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10100,
set in %B0101010101010101,
tick,
output,
tock,
output;
set address %B10101,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10101,
set in %B0101010101010101,
tick,
output,
tock,
output;
set address %B10101,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10101,
set in %B0101010101010101,
tick,
output,
tock,
output;
set address %B10110,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;
set address %B10111,
eval,
output;

set load 1,
set address %B10110,
set in %B0101010101010101,
tick,
output,
tock,
output;
set address %B10110,
set in %B1010101010101010,
tick,
output;
tock,
output;

set load 0,
set address %B10100,
tick,
output;
tock,
output;
set address %B10100,
eval,
output;
set address %B10101,
eval,
output;
set address %B10101,
eval,
output;
set address %B10110,
eval,
output;
set address %B10110,
eval,
output;
set address %B10111,
eval,
output;

