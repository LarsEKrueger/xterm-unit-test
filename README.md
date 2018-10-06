# Introduction

Despite being used by many people and applications, XTerm does not provide a
test suite to ensure that its implementation matches its specification.

This project provides such a test suit. Additionally, this test suite is
implemented in such a fashion that other terminal emulators can be tested to
adhere to the specification or at least to XTerm's implementation.

## Basic Idea

The basic design of each test is the following template:

1. Create a character matrix.
2. Process the character sequence under test.
3. Compare the resulting character matrix with manually-defined ground truth.

In order to fully test the whole set of sequences, a number of additional
requirements have to be fulfilled:

- Tests MUST be portable to at least C (to check XTerm) and Rust (to check
  [BiTe](https://github.com/LarsEKrueger/bite)).
- Tests MUST check behaviour (i.e. the state of the character matrix), not
  implementation (e.g. internal states of the terminal emulator).
- Ground Truth MUST support multiple checks per test.
- Tests MUST be built and executed without changes to the `XTerm` repository.
  This is a requirement from the `XTerm` maintainer.
- Tests SHOULD be easy to define.
- Tests SHOULD work on character matrices of different sizes.
- Tests SHOULD be runnable in parallel.
- Failing tests SHOULD catch as many errors per run as possible.
- Test coverage SHOULD be displayed.
- Tests SHALL be built as an integral part of the `BiTe` build system.
- Tests SHALL be declared with little boiler plate code.

Based on these requirements, the implementation of the steps is done as follows:

1. Fill the character matrix using a function based on the initial size. This
   function will have no side-effects, thus the same character matrix is
   generated for a given size. A test will be supplied to check that the
   generator implements the specified function.
2. Process the character sequence. This sequence may contain arbitrary bytes,
   e.g. unicode bytes.
3. Provide a plethora of test functions. Do not limit the number of checks per
   test. Provide EXPECT and ASSERT functionality like google test.

For a portable implementation of those tests, a code generator is used. Thus,
the tests are defined in a domain specific language (DSL) and converted to
source code at compile time. This could be done in Rust with the use of the
macro system, much like the control sequence parser is tested. This would not
be very portable.

Two options are most convenient to define the DSL: `python` and `M4`. `python`
has the advantage that more people are familiar with it, `M4` has the
advantage that XTerm already uses it (`automake`/`autoconf` are based on
`M4`).

`M4` is a macro processor, like the `C` preprocessor, but more powerful.
Unfortunately, it does not support multi-byte characters very well.

The current implementation will use `python` as it is deemed the more general solution.

## Example Test

The following example code will give an impression what such a test looks
like. For that, we choose a simple command sequence: print an `A`, move one
line up, print a `ü`. The sequence is:

    A ESC [ A ü

### `python` Example

    test("a_up_b", 80, 25, 40, 13, "A\x1b[Aü")
         .claim().size(80,25)
         .expect().
         .cpos(42,12)
         .char(40,13,'A')
         .attr(40,13,'')
         .uc(41,12,0xfc)
         .bg_def(41,12)
         .fg_def(41,12)

A test is declared with `test`. The user provides a name, the initial size of
the character matrix, the initial cursor position, and the sequence under test.
Size and positions are always (X,Y) starting at (0,0) at the top-left of the
matrix.

The method `claim` make the following tests abort the test, while `expect`
only produces a warning unless the test cannot be performed. In most testing
frameworks, `claim` is called `assert`, but that is a reserved word in `python`.

`cpos` checks the final cursor position, `char` checks if a certain ASCII
character is at the given position. `uc` does the same for unicode code
points.

`attr` checks that a certain set of
attributes is set. Here, it checks that no attributes are set.

The checks `bg_*` and `fg_*` check for a given foreground / background
color. Here, they check that the default colors are used.

The tests are declared via the [*builder*
pattern](https://en.wikipedia.org/wiki/Builder_pattern). As `python3` supports
UTF-8 as the default encoding of source files, the character sequence can be
provided directly.

# Implementation Notes

## Attributes

As the test pattern generator generates the attributes as a 13 bit number
instead of e.g. drawing the individual bits from separate random numbers, the
mapping of the bits to XTerm's attribute needs to be fixed. The following table
lists this mapping.

| Bit n| Attribute    |Code| Description                      |
|-----:|:-------------|:--:| :------------------------------- |
|    0 | inverse      |  i | Swap foreground/background colors|
|    1 | underline    |  u | <u>Underline font</u>            |
|    2 | bold         |  b | **Bold font**                    |
|    3 | blink        |  l | Blinking character               |
|    4 | background   |  c | Background color has been set    |
|    5 | foreground   |  f | Foreground color has been set    |
|    6 | protected    |  p | Character cannot be overwritten  |
|    7 | drawn        |  d | Cell will be copied when selected|
|    8 | faint        |  a | Faint font                       |
|    9 | italic       |  t | *Italic font*                    |
|    10| strikeout    |  s | Draw line through character      |
|    11| double under |  w | Double underline                 |
|    12| invisible    |  v | Character is there, but not drawn|

*Bit n* is to interpreted as `1 << n` in C notation. *Code* refers to the
character that has to be passed to `.attr` to check for that attribute.
