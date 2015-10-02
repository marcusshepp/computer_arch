load FullSubtractor.hdl,
output-file FullSubtractor.out,
compare-to FullSubtractor.cmp,
output-list a%B3.1.3 b%B3.1.3 c%B3.1.3 diff%B3.1.3 borrow%B3.1.3;

set a 0,
set b 0,
set c 0,
eval,
output;

set a 0,
set b 0,
set c 1,
eval,
output;

set a 0,
set b 1,
set c 0,
eval,
output;

set a 0,
set b 1,
set c 1,
eval,
output;

set a 1,
set b 0,
set c 0,
eval,
output;

set a 1,
set b 0,
set c 1,
eval,
output;

set a 1,
set b 1,
set c 0,
eval,
output;

set a 1,
set b 1,
set c 1,
eval,
output;
