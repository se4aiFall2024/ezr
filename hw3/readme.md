## Results
### Installation.
No extra installation needed. You can find answer for experiment1 in experiment.py. We modified the branch.sh to fit our specific use case or scenario, renaming it as run_experiments.sh.Besides, rq.sh is in /hw3/tmp/branch/rq.sh. Our output files of experiment 2 are under /hw3/tmp/branch.
### test cases
To illustrate the test cases, I will use the results of running /data/optimize/config/SS-B.csv as an example, which can be executed using the command:
python experiment.py /workspaces/ezr/data/optimize/config/SS-B.csv.

Below is a portion of the output showcasing the corresponding test cases:
```
Processing Low-Dimensional dataset: /workspaces/ezr/data/optimize/config/SS-B.csv
Number of independent variables: 3
Running commissioning tests...
Test passed: chebyshevs().rows[0] returns the top item.
Test passed: shuffle() changes the order of the data.

Running experiments for N = 20
Test passed: exploit/b=False ran 20 times as expected.
Test passed: exploit/b=True ran 20 times as expected.
Test passed: explore/b=False ran 20 times as expected.
Test passed: explore/b=True ran 20 times as expected.
Test passed: Dumb method ran 20 times as expected.

Length checks for N=20:
  All 80 smart lists have the correct length of 20.
  All 20 dumb lists have the correct length of 20.

Running experiments for N = 30
Test passed: exploit/b=False ran 20 times as expected.
Test passed: exploit/b=True ran 20 times as expected.
Test passed: explore/b=False ran 20 times as expected.
Test passed: explore/b=True ran 20 times as expected.
Test passed: Dumb method ran 20 times as expected.

Length checks for N=30:
  All 80 smart lists have the correct length of 30.
  All 20 dumb lists have the correct length of 30.

Running experiments for N = 40
Test passed: exploit/b=False ran 20 times as expected.
Test passed: exploit/b=True ran 20 times as expected.
Test passed: explore/b=False ran 20 times as expected.
Test passed: explore/b=True ran 20 times as expected.
Test passed: Dumb method ran 20 times as expected.

Length checks for N=40:
  All 80 smart lists have the correct length of 40.
  All 20 dumb lists have the correct length of 40.

Running experiments for N = 50
Test passed: exploit/b=False ran 20 times as expected.
Test passed: exploit/b=True ran 20 times as expected.
Test passed: explore/b=False ran 20 times as expected.
Test passed: explore/b=True ran 20 times as expected.
Test passed: Dumb method ran 20 times as expected.

Length checks for N=50:
  All 80 smart lists have the correct length of 50.
  All 20 dumb lists have the correct length of 50.
```
As demonstrated, the test cases address the four required checks:

    1. chebyshevs().rows[0]: Verifies that the function returns the top sorted item.

    2. smart and dumb list lengths: Ensures that both lists have the correct length, depending on the value of N.

    3. Experiment runs 20 times: Confirms that the experiment is executed 20 times for statistical significance.

    4. d.shuffle(): Verifies that the shuffle() function properly randomizes the order of the data.
### Key Methods:
- **exploit**: Optimizes by exploiting known best results.
- **explore**: Tries new configurations to explore other possible improvements.
- **dumb**: Random guessing method to compare against smarter strategies.
- **asIs**: Baseline method without any optimizations.

### RQ.sh Results:
| Rank | Method          | Performance | Evaluation | Delta | Summary |
|------|-----------------|-------------|------------|-------|---------|
| 0    | exploit/b=False | High        | Consistent | Low   | Good performance, low variance |
| 1    | explore/b=False | High        | Consistent | Low   | Balanced exploration and exploitation |
| 2    | dumb            | Moderate    | Varies     | High  | Random guessing leads to inconsistent results |
| 3    | asIs            | Low         | Poor       | Very High | Unoptimized, performs poorly |

### Detailed Insights
- **Exploit and Explore** methods consistently outperform **dumb** and **asIs** methods, especially in terms of rank and delta, indicating more stable and effective optimization.
- **Dumb** method shows higher variance in performance, as expected from a non-optimized random strategy.
- **AsIs** method consistently performs the worst, validating the necessity of optimization strategies.


## Table Results Walkthrough

The results are presented in three main sections: RANK, EVALS, and DELTAS.

1. RANK:
- Shows the percentage of times each method achieved a particular rank across all datasets.
- exploi/b=True performed best, achieving rank 0 in 94% of cases.
- Random guessing (dumb) achieved rank 0 in 63% of cases, lower than most active learning methods.

2. EVALS:
- Displays the average number of evaluations (with standard deviation) for each method at each rank.
- Most methods (except asIs) used 25-29 evaluations on average.
- Random guessing (dumb) used a similar number of evaluations as active learning methods.

3. DELTAS:
- Shows the percentage improvement over the baseline (asIs) for each method.
- All methods showed improvement over the baseline.
- exploi/b=True and explore/b=True showed the largest improvements at rank 0.

These results indicate that active learning methods, particularly exploi/b=True, consistently outperformed random guessing across various problem dimensions. However, random guessing still performed reasonably well, achieving rank 0 in a significant portion of cases.

## Conclusion

Since we observed that active learning methods, especially exploi/b=True, consistently outperformed random guessing across various problem dimensions, we doubt the JJR1 hypothesis and partially confirm the JJR2 hypothesis as follows:

1. JJR1 (Nothing works better than 50 random guesses for low dimensional problems) is not supported by our results. Active learning methods performed better than random guessing even in low-dimensional problems.

2. JJR2 (Random guessing is rubbish for higher dimensional data) is partially supported. While random guessing did perform worse than active learning methods overall, its performance was not entirely "rubbish" as it still achieved rank 0 in 63% of cases.

We propose refining these hypotheses as follows:

1. Refined JJR1: Active learning methods, particularly those employing exploitation strategies, tend to outperform random guessing even in low-dimensional problems.

2. Refined JJR2: While random guessing becomes less effective as problem dimensionality increases, it can still provide reasonable results in some cases. However, active learning methods generally offer superior performance across all dimensionalities.

Further research is needed to investigate the specific performance differences between these methods on problems of varying dimensionality to gain a more comprehensive understanding of their effectiveness in different scenarios.
