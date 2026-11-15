import random
import timeit
import signal
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search
from src.lab07.search import two_sum_brute, two_sum_fast
from src.lab04.io_txt_csv import write_csv

def timeout_handler(signum, frame):
    raise TimeoutError


def measure_sort(fn, nums):
    previous_handler = signal.signal(signal.SIGALRM, timeout_handler)
    try:
        signal.setitimer(signal.ITIMER_REAL, 60)
        return timeit.timeit(lambda: fn(nums), number=1)
    except TimeoutError:
        return "> 60 с"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


def bench_sorts(n):
    nums = [random.randint(-100, 100) for _ in range(n)]
    rows = []

    seconds = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("sort", n, "sorted", seconds))

    for fn in (bubble_sort, insertion_sort, selection_sort):
        seconds = measure_sort(fn, nums)
        rows.append(("sort", n, fn.__name__, seconds))

    return rows



def bench_search():
    nums = [random.randint(-100_000, 100_000) for _ in range(100_000)]
    queries = [random.randint(-100_000, 100_000) for _ in range(10_000)]
    rows = []
    seconds = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("search", len(nums), "sorting", seconds))
    sorted_nums = sorted(nums)

    seconds = timeit.timeit(lambda: [linear_search(nums, x) for x in queries], number=1)
    rows.append(("search", len(nums), "linear_search", seconds))

    seconds = timeit.timeit(lambda: [binary_search(sorted_nums, x) for x in queries], number=1)
    rows.append(("search", len(nums), "binary_search", seconds))

    return rows


def bench_two_sum(n):
    nums = [random.randint(-100_000, 100_000) for _ in range(n)]
    target = nums[-2] + nums[-1]
    rows = []
    for fn in (two_sum_brute, two_sum_fast):
        seconds = timeit.timeit(lambda: fn(nums, target), number=1)
        rows.append(("two_sum", n, fn.__name__, seconds))

    return rows 

if __name__ == "__main__":
    random.seed(42)
    rows = []

    for n in (1000, 10000, 100_000):
        rows.extend(bench_sorts(n))

    rows.extend(bench_search())

    for n in (1000, 10000):
        rows.extend(bench_two_sum(n))

    write_csv(rows, "data/lab07/bench.csv", header=("task", "n", "impl", "seconds"))
    print(f"{'task':<12} {'n':>8} {'impl':<20} {'seconds':>12}")
    for task, n, impl, seconds in rows:
        seconds_text = f"{seconds:.6f}" if isinstance(seconds, (int, float)) else seconds
        print(f"{task:<12} {n:>8} {impl:<20} {seconds_text:>12}")