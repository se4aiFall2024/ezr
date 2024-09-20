# experiment.py

import sys
import random
import time
from math import exp
from ezr import DATA, csv, the
import stats

def count_independent_vars(file):
    """Counts the number of independent variables in the dataset."""
    data = DATA().adds(csv(file))
    return len(data.cols.x)

def classify_datasets(files):
    """Classify datasets into low and high dimensional based on independent variables."""
    low_dim = []
    high_dim = []
    for file in files:
        num_vars = count_independent_vars(file)
        if num_vars < 6:
            low_dim.append((file, num_vars))
        else:
            high_dim.append((file, num_vars))
    return low_dim, high_dim

def guess(N, d):
    """Selects N random rows and returns them sorted on Chebyshev distance."""
    some = random.choices(d.rows, k=N)
    cloned_data = d.clone().adds(some).chebyshevs()
    sorted_rows = cloned_data.rows
    return sorted_rows

def test_chebyshev_sorting(data):
    """Test if chebyshevs().rows[0] returns the top item."""
    data.chebyshevs()
    top_row = data.rows[0]
    distances = [data.chebyshev(row) for row in data.rows]
    min_distance = min(distances)
    assert data.chebyshev(top_row) == min_distance, "Error: chebyshevs().rows[0] does not return the top item."
    print("Test passed: chebyshevs().rows[0] returns the top item.")

def test_shuffle(data):
    """Test if shuffle() changes the order of the data."""
    original_order = data.rows.copy()
    data.shuffle()
    shuffled_order = data.rows
    assert original_order != shuffled_order, "Error: shuffle() did not change the order of the data."
    print("Test passed: shuffle() changes the order of the data.")

def test_list_lengths(lst, expected_length, method_name):
    """Test if the list has the expected length."""
    if len(lst) != expected_length:
        raise AssertionError(f"{method_name} list length {len(lst)} does not match expected {expected_length}.")

def test_repeats(run_count, expected_repeats, method_name):
    """Test if the code runs the experimental treatment the expected number of times."""
    assert run_count == expected_repeats, f"{method_name} ran {run_count} times, expected {expected_repeats} times."
    print(f"Test passed: {method_name} ran {run_count} times as expected.")

def run_experiment(file):
    repeats = 20  # Number of repetitions for statistical validity
    data = DATA().adds(csv(file))
    num_vars = len(data.cols.x)
    label = "Low-Dimensional" if num_vars < 6 else "High-Dimensional"
    print(f"\nProcessing {label} dataset: {file}")
    print(f"Number of independent variables: {num_vars}")
    somes = []

    # Commissioning tests
    print("Running commissioning tests...")
    try:
        test_chebyshev_sorting(data)
    except AssertionError as e:
        print(e)
    try:
        test_shuffle(data)
    except AssertionError as e:
        print(e)

    # Baseline calculation
    b4 = [data.chebyshev(row) for row in data.rows]
    somes.append(stats.SOME(b4, f"asIs,{len(data.rows)}"))

    # Define scoring policies
    scoring_policies = [
        ('exploit', lambda B, R: B - R),
        ('explore', lambda B, R: (exp(B) + exp(R)) / (1E-30 + abs(exp(B) - exp(R))))
    ]

    for N in [20, 30, 40, 50]:
        the.Last = N
        print(f"\nRunning experiments for N = {N}")

        # Initialize variables to collect length check failures
        length_check_failures = {'smart': 0, 'dumb': 0}
        total_checks = {'smart': 0, 'dumb': 0}

        # Smart Method
        for what, how in scoring_policies:
            for the.branch in [False, True]:
                result = []
                run_count = 0
                for _ in range(repeats):
                    data.shuffle()
                    tmp = data.activeLearning(score=how)
                    try:
                        test_list_lengths(tmp, N, f"{what}/b={the.branch}")
                    except AssertionError as e:
                        length_check_failures['smart'] += 1
                    total_checks['smart'] += 1
                    run_count += 1
                    result.append(data.chebyshev(tmp[0]))
                # Test if the number of runs is as expected
                test_repeats(run_count, repeats, f"{what}/b={the.branch}")
                tag = f"{what}/b={the.branch},{N}"
                somes.append(stats.SOME(result, tag))

        # Dumb Method
        dumb_results = []
        run_count = 0
        for _ in range(repeats):
            lst = guess(N, data)
            try:
                test_list_lengths(lst, N, "Dumb method")
            except AssertionError as e:
                length_check_failures['dumb'] += 1
            total_checks['dumb'] += 1
            run_count += 1
            dumb_results.append(data.chebyshev(lst[0]))
        # Test if the number of runs is as expected
        test_repeats(run_count, repeats, "Dumb method")
        somes.append(stats.SOME(dumb_results, f"dumb,{N}"))

        # After running experiments for N, output whether smart and dumb lists were the right length
        print(f"\nLength checks for N={N}:")
        for method in ['smart', 'dumb']:
            failures = length_check_failures[method]
            total = total_checks[method]
            if failures == 0:
                print(f"  All {total} {method} lists have the correct length {N}.")
            else:
                print(f"  {failures}/{total} {method} lists did not have the correct length {N}.")
                print("  Possible reasons: implementation issues or incorrect handling of 'the.Last'.")

    # Generate report
    print(f"\nResults for dataset: {file}")
    stats.report(somes, 0.01)

if __name__ == "__main__":
    # Collect dataset files from command-line arguments
    dataset_files = [arg for arg in sys.argv[1:] if arg.endswith('.csv')]

    if len(dataset_files) == 0:
        print("No datasets provided.")
        sys.exit(1)

    for file in dataset_files:
        run_experiment(file)
