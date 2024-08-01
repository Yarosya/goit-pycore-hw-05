import re
from typing import Callable, Generator
def generator_numbers(text: str) -> Generator[float, None, None]:
    matches = re.findall(r'\b\d+\.\d+\b', text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return round(sum(func(text)),2)

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 20020.21231 як основний дохід, доповнений додатковими надходженнями 127.45124121 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
