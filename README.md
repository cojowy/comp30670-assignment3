Assignment for COMP30670 - Software Engineering at UCD.

The Science Centre is installing a new display board which is constructed from LED
lights.
The board is a square grid of LEDs which we control by sending commands to the unit
to turn on or off certain rectangular regions.
The L × L lights can be modelled as a 2 dimensional grid with L rows of lights and L
lights in each row and the LED’s at each corner are (0, 0), (0, L − 1), (L − 1, L − 1) and
(L − 1, 0).
The lights are either on or off.
Your job is to test the lights. We test them by sending instructions to turn on, turn
off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through
2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
For example:
• "turn on 0,0 through 999,999" would turn on (or leave on) every light.
• "switch 0,0 through 999,0" would toggle the first line of 1000 lights, turning
off the ones that were on, and turning on the ones that were off.
• "turn off 499,499 through 500,500" would turn off (or leave off) the middle
four lights.
You will read a list of these instructions from a file. Your task is to determine how many
lights are on after all the instructions have been applied.
(a) Before you write any code to solve this problem, think about how you will solve
it. Write a paragraph outlining your initial strategy (you can include pseudocode
if you wish).
©UCD Semester II/ Modular Page 1 of 3
(b) Create a python project in Eclipse following the standard template. You should
have a package directory, a tests directory and a setup.py file.
1 skeleton/
2 NAME/
3 __init__.py
4 docs/
5 setup.py
6 tests/
7 test.py
(c) Create a new Github repository and connect it to your local Eclipse repository as
a remote. Make regular commits as you work through and develop your solution.
(d) The file has the following format:
999
turn on 0,0 through 999,999
switch 0,0 through 999,0
turn off 499,499 through 500,500
where the first line specifies the size of the grid 0 < L < 109 and the next lines
contain the command. The only possible commands are ”turn on”, ”turn off” and
”switch”.
Your setup.py should install a script which reads input from a file (perhaps over
the network), specified as a command line argument:
1 solve_led --input http://claritytrec.ucd.ie/~alawlor/comp30670/←-
input_assign3.txt
(e) Try to follow the Test Driven Development model for this assignment. Think about
the piece you are going to write, develop a test, write the test, execute it (it will
fail!), then write the code to make it pass. Make sure the commit history reflects
the actual development.
Your code should test for various things:
• Existence of the input file
• Check for errors in the file, any commands which are not ”turn on”, ”turn off”
or ”switch” should be ignored.
• If a command affects a region outside the area of the grid, then it will still be
executed, but only on the region of lights inside the boundary of the grid.
(f) Run the code on your Amazon EC2 instance.
(g) Comment on the design and complexity of your solution (a couple of paragraphs is
fine.
(h) Run your code with each of the following inputs:
1. http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt
2. http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt
©UCD Semester II/ Modular Page 2 of 3
3. http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt
4. http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt
5. http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt
