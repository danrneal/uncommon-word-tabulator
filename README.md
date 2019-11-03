# Uncommon Word Tabulator

This is a command line program to tabulate the appearance and frequency of
uncommon words in a text file. It takes two files as inputs. The first input
is a text file with words that you'd like the program to be considered "common"
(all other words will be considered "uncommon"). The second input is the text
file you want the program to tabulate.

## Usage

```
usage: uncommonwords.py common_words_file text_file
```

###### Note:
When comparing words, possessives are counted as separate words from their 
non-possessive counterparts (i.e. "Alice" is a separate word from "Alice's").
Non-words such as chapter numbers or headings are also counted as words.

## Testing Suite

This repository contains a test suite consisting of functional tests and unit
tests.

#### Functional Tests

These test the program from the outside, from a user's point of view and are
also known as Acceptance Tests or End-to-End Tests. You can run them with the
following command:

```
python3 -m unittest discover functional_tests/
```

#### Unit Tests

These test the program from the inside, from developer's point of view. You
can run them with the following command:

```
python3 -m unittest discover tests/
```

## A comment on TDD

This project was done following Test-Driven Development principles where the
starting point is a failing test. My process was to write a functional test to
describe the desired behavior from the user's point of view and then a unit
test to define how I wanted to the code to behave. That is the point where I
wrote the "actual" code to get the unit tests to pass. Once I had passing
unit tests, I checked to see if the FT passed; if they didn't pass, I wrote
more unit tests and corresponding code. 

While this may seem unnecessary for a program of such a small size and may
seem like showing off or overdoing, TDD principles help to create quality,
maintainable code and as such I believe are good habits to foster even on a
small project such as this.
