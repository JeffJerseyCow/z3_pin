# z3_pin
The purpose of the source code is to generate lists of bad Personal Identification Numbers (PINs). It works by constraining possible combinations to certain rules, for example:

- No more than 4 consecutive numbers, e.g. 12345 and 63456 (3456)
- No more than 3 idential numbers in a row, e.g. 11154 and 23444
- No more than one two digit repeating code, e.g. 12266 (2266) and 66554 (6655)
- No more than one consecutive repeating code, e.g. 12128 (1212) and 75656 (5656)

With these constraints set at a specific length, e.g. a 5-digit pin. The Satisfiability Moduloe Theories (SMT) z3 is used to print out all offending PINs to create a blacklist.

The purpose of the blacklist is to verify common PINs during PIN authentication and creation within applications.

## Usage
The largest requirement is installing the z3 theorem prover, but it's fairly simple to compile and build following this link:

https://github.com/Z3Prover/z3?tab=readme-ov-file#building-z3-using-make-and-gccclang

I prefer the traditional make build tool, but there are other and they all install easily.

After installing z3 on your system, simply install requirements with poetry - you must get in the z3_pin project directory. And run the application for a PIN length - in this example 5-digit pins.

```bash
poetry install
poetry run z3_pin -- 5
```
