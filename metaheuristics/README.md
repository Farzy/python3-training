# Metaheuristics for the N-Queens problem

This folder is a first step into **metaheuristics**: general-purpose strategies that
search for a good (here: valid) solution without exploring the whole search space.
It reuses the N-Queens problem already solved exactly by `../eight-queens.py`, so the
two approaches can be compared on the same ground.

## 1. Exact search vs local search

`eight-queens.py` uses **backtracking**: it places queens row by row and undoes a
choice as soon as it leads to a conflict. It is *complete*: it finds every solution,
and it can prove that none exists (N = 2 or 3). Its cost grows exponentially with N.

A **local search** works on complete boards instead:

1. Start from a complete but wrong board (one queen per row, placed at random).
2. Measure how bad it is (the number of conflicts).
3. Change it a little (move one queen), keeping changes that help.
4. Stop when there are no conflicts left.

It is *incomplete*: it returns one solution, it can fail to find one that exists, and
it can never prove that there is none. The tests check this: for N = 2 or 3 both
solvers give up after `max_steps` instead of claiming a solution.

## 2. Min-conflicts

At each step, pick a random queen that is attacked and move it, within its row, to the
column where it is attacked by the fewest queens (ties broken at random).

- Counters per column and per diagonal make "how many queens attack this square?" an
  O(1) question, so one step costs O(N).
- **Weakness: local minima and plateaus.** The search can reach a board where no single
  move reduces the conflicts and keep wandering there. Measured with
  `max_steps = 100 000`: 7 failures out of 200 seeds for N = 8, 3/200 for N = 20,
  0/50 for N = 50. Small boards stall more often because they have fewer solutions.
  The classic remedy is to restart from a new random board; simulated annealing is
  another one.

## 3. Simulated annealing

The name comes from metallurgy: a metal cooled slowly settles into a low-energy crystal.

- **State**: a permutation, so there is exactly one queen per row *and* per column;
  only diagonal conflicts remain.
- **Energy**: the number of attacking pairs. 0 means solved.
- **Move**: swap the columns of two random rows.
- **Acceptance rule (Metropolis)**: a move that lowers the energy is always accepted.
  A move that raises it by `delta` is accepted with probability `exp(-delta / T)`.
- **Cooling**: the temperature `T` is multiplied by `cooling_rate` at each step.

When `T` is high, bad moves are often accepted, which lets the search leave a local
minimum (exploration). When `T` is low, the search only goes downhill (exploitation).
`initial_temperature` and `cooling_rate` are the knobs to tune; the defaults were
chosen by trying a few values, not by a systematic study.

## 4. Measurements

`python3 n_queens_local_search.py --size N --runs R` runs each method with seeds
0 .. R-1 (Python 3.13, one cloud container, single runs per seed):

| N    | method        | success | median time | median steps |
|------|---------------|---------|-------------|--------------|
| 8    | min-conflicts | 18/20   | 0.0001 s    | 30           |
| 8    | annealing     | 20/20   | 0.0002 s    | 84           |
| 100  | min-conflicts | 20/20   | 0.0027 s    | 120          |
| 100  | annealing     | 20/20   | 0.14 s      | 50 984       |
| 1000 | min-conflicts | 5/5     | 0.19 s      | 705          |
| 1000 | annealing     | 5/5     | 0.56 s      | 151 759      |

For comparison, the backtracking solver needs 0.38 s to find its *first* solution for
N = 20, 6.4 s for N = 28 and 122 s for N = 30.

What to take from this, and what not to:

- Min-conflicts is the better tool for N-Queens: the problem has many solutions spread
  evenly, which is exactly where greedy repair shines. This does not generalise to
  every problem.
- Annealing is slower here but never stalled in these runs. Its strength shows on
  problems with deep local minima.
- Timings vary with the machine; compare the methods with each other, not with the
  absolute numbers.

## 5. Running

```bash
python3 metaheuristics/n_queens_local_search.py --help
python3 metaheuristics/n_queens_local_search.py --size 1000 --runs 5
python3 -m unittest discover -s metaheuristics -v
```

## 6. Ideas to go further

- Add random restarts to min-conflicts and measure the success rate again on N = 8.
- Tune the annealing temperature schedule and plot the energy over time (matplotlib
  is already a dependency).
- Try a genetic algorithm on the same problem and compare the three methods.
