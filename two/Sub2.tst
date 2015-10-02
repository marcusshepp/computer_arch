load Sub2.hdl,
output-file Sub2.out,
compare-to Sub2.cmp,
output-list x%B3.2.3 y%B3.2.3 out%B3.2.3;

set x %B00,
set y %B00,
eval,
output;

set x %B00,
set y %B01,
eval,
output;

set x %B00,
set y %B10,
eval,
output;

set x %B00,
set y %B11,
eval,
output;

set x %B01,
set y %B00,
eval,
output;

set x %B01,
set y %B01,
eval,
output;

set x %B01,
set y %B10,
eval,
output;

set x %B01,
set y %B11,
eval,
output;

set x %B10,
set y %B00,
eval,
output;

set x %B10,
set y %B01,
eval,
output;

set x %B10,
set y %B10,
eval,
output;

set x %B10,
set y %B11,
eval,
output;

set x %B11,
set y %B00,
eval,
output;

set x %B11,
set y %B01,
eval,
output;

set x %B11,
set y %B10,
eval,
output;

set x %B11,
set y %B11,
eval,
output;
