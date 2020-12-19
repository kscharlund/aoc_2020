# Advent of Code 2020 solutions #

These are my solutions to the problems from
[Advent of Code 2020](https://adventofcode.com/2020/).

Some problems or solutions I found noteworthy for whatever reason:

## 2020-12-08 ##

Took me a while to get that I should just test all modified programs. Don't
think that the backtracking solution I implemented is necessary, probably
just evaluating would have worked as well.

## 2020-12-10 ##

Cool problem. I got to the straightforward solution based on 1- or 3-diffs by
calculating the number of combinations for different runs by hand. The dynamic
programming and recursive solutions are nice, but made inspired by other code.

## 2020-12-13 ##

A Chinese Remainder Theorem application. Since I could recall the term, I just
found a solver in SymPy instead of actually trying to solve the problem myself.
Later, I implemented a handwritten solution inspired by some code from reddit.
I think I could have gotten there myself if I hadn't remembered the CRT...

## 2020-12-14 ##

Got stumped by part 2 after trying to run the small example input from part 1
on a brute force solution. Had to go to reddit to get unstuck, the brute force
solution works for all input in the big input set.

## 2020-12-15 ##

Brute force, used the exact same solution for parts 1 and 2. Wonder if there is
a nicer way?

## 2020-12-17 ##

A variation on the problem from 2020-12-11 (Game of Life-like simulation),
but the solution I found for this problem was much nicer.
Also extremely easy to adapt from part 1 to part 2.

## 2020-12-18 ##

A simple expression parsing problem, I solved part 1 using a hand-written
recursive parser. For part two, where operator precedence was introduced,
I found Dijkstras
[shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
that I hadn't heard about before and found very pleasing. More reading on the
expression parsing topic here: http://www.oilshell.org/blog/2017/03/31.html.

Some pretty interesting Python trickery to be able to use `eval` on
https://www.reddit.com/r/adventofcode/comments/kfh5gn/2020_day_18_part2_swapping_to_parse_using_the/.

## 2020-12-19 ##

This one was tough for me. I managed to solve part 1 with an ugly, inefficient
recursive solution. For part 2, I nicked code from
[reddit user thomasahle](https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggcohaa)
instead. Just not inspired enough to do it properly...

Another nice solution, similar to what I was going for but done competently:
https://gist.github.com/andreypopp/6036fe8dcb891534f15c0d741f68f2f6
