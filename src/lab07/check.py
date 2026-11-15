import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search
from src.lab07.search import two_sum_brute, two_sum_fast
def check_sorting(fn, trials=100):
    for i in range(trials):
        n = random.randint(0,50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        nums2 = nums.copy()
        nums_fn = fn(nums)
        assert nums == nums2, f"Исходный список изменился: было {nums2}, стало {nums}"
        assert sorted(nums2) == nums_fn, f"На входе: {nums2}, результат: {nums_fn}"

def check_search():
    for i in range(100):
        n = random.randint(0,50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        
        digit_fn = linear_search(nums, x)
        assert digit_fn == expected, f"Список: {nums}, x: {x}, ожидалось: {expected}, получено: {digit_fn}"

        sorted_nums = sorted(nums)
        result = binary_search(sorted_nums, x)
        if expected == -1:
            assert result == -1, f"Список={sorted_nums}, x={x}, ожидалось=-1, получено={result}"
        else:
            assert 0 <= result < len(sorted_nums), f"Недопустимый индекс: список={sorted_nums}, x={x}, result={result}"
            assert sorted_nums[result] == x, f"Неверное значение: список={sorted_nums}, x={x}, result={result}"
    nums = [1, 3, 5, 7, 9]
    result = binary_search(nums, 1)
    assert result == 0, f"Первый элемент: список={nums}, x=1, получено={result}"

    result = binary_search(nums, 9)
    assert result == 4, f"Последний элемент: список={nums}, x=9, получено={result}"

    result = binary_search(nums, 6)
    assert result == -1, f"Отсутствующее число: список={nums}, x=6, получено={result}"  

def check_two_sum(trials=100):
    for i in range(trials):
        target = random.randint(-200,200)
        n =  random.randint(0,50)
        nums = [random.randint(-100,100) for _ in range(n)]
        brute_result = two_sum_brute(nums, target)
        fast_result = two_sum_fast(nums, target)
        assert (brute_result is None) == (fast_result is None), f"Разные ответы: nums={nums}, target={target}, brute={brute_result}, fast={fast_result}"
        for result in (brute_result, fast_result):
            if result is not None:
                i, j = result
                assert 0 <= i < j < len(nums), f"Неверные индексы: nums={nums}, target={target}, result={result}"
                assert nums[i] + nums[j] == target, f"Неверная сумма: nums={nums}, target={target}, result={result}"


if __name__ == "__main__":
    random.seed(42)
    trials = 100
    checks = 0

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn, trials)
        checks += trials

    check_search()
    checks += 100 + 3

    check_two_sum(trials)
    checks += trials

    print(f"OK: {checks} проверок")