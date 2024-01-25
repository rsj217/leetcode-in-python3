import unittest
from collections import defaultdict
from typing import Generator, List, Callable, Tuple


def map_func(text: str) -> Generator:
    for word in text.strip().split():
        yield word, 1


def reduce_func(word: str, counts: List[int]) -> Generator:
    yield word, sum(counts)


def map_reduce(
    data: List[str],
    map_fn: Callable[[str], Generator],
    reduce_fn: Callable[[str, List[int]], Generator]) -> List[Tuple[str, int]]:
    tmp = []
    # map
    for line in data:
        tmp.extend(map_fn(line))
    
    # shuffle
    groups = defaultdict(list)
    for k, v in tmp:
        groups[k].append(v)
    
    # reduce
    reduced = []
    for k, v in groups.items():
        reduced.extend(reduce_fn(k, v))
    return reduced


class TestMapReduce(unittest.TestCase):
    
    def test_map_reduce(self):
        data = [
            "hello world",
            "hello mapreduce",
            "mapreduce example",
            "hello mapreduce example"
        ]
        ans = map_reduce(data, map_func, reduce_func)
        hello = ans[0][1]
        word = ans[1][1]
        mapreduce = ans[2][1]
        example = ans[3][1]
        self.assertEqual(hello, 3)
        self.assertEqual(word, 1)
        self.assertEqual(mapreduce, 3)
        self.assertEqual(example, 2)


if __name__ == '__main__':
    unittest.main()
