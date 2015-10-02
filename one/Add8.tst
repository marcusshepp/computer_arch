// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/02/Add16.tst

load Add8.hdl,
output-file Add8.out,
compare-to Add8.cmp,
output-list a%B1.8.1 b%B1.8.1 out%B1.8.1;

set a %B00000000,
set b %B00000000,
eval,
output;

set a %B00000000,
set b %B11111111,
eval,
output;

set a %B11111111,
set b %B11111111,
eval,
output;

set a %B10101010,
set b %B01010101,
eval,
output;

set a %B11000011,
set b %B11110000,
eval,
output;

set a %B00110100,
set b %B01110110,
eval,
output;
