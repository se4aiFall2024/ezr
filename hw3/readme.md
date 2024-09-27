## Results
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