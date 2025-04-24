from collections import Counter
from typing import List

class StatisticsCalculator:
    def __init__(self, numbers: List[int]):
        self.numbers = sorted(numbers)

    def mean(self) -> float:
        return sum(self.numbers) / len(self.numbers)

    def median(self) -> float:
        n = len(self.numbers)
        mid = n // 2
        if n % 2 == 0:
            return (self.numbers[mid - 1] + self.numbers[mid]) / 2
        else:
            return self.numbers[mid]

    def mode(self) -> List[int]:
        count = Counter(self.numbers)
        max_freq = max(count.values())
        return sorted([num for num, freq in count.items() if freq == max_freq])

if __name__ == "__main__":
    calc = StatisticsCalculator([1, 2, 2, 3, 4])
    print("Mean:", calc.mean())
    print("Median:", calc.median())
    print("Mode:", calc.mode())
