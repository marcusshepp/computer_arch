load OddCounter.hdl,
output-file OddCounter.out,
compare-to OddCounter.cmp,
output-list time%S1.4.1 reset%D1.3.1 out%B1.16.1;

set reset 0,
tick,output,
tock,output;

tick,output,
tock,output;

tick,output,
tock,output;

tick,output,
tock,output;

set reset 1,
tick,output,
tock,output;

tick,output,
tock,output;

set reset 0,
tick,output,
tock,output;

tick,output,
tock,output;


