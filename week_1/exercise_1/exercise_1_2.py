# Example 2
def print_is_odd_or_even(number : int = 0) -> None:
    """Print if a number is odd or even. This function is used by list_odd_or_even_check."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def list_odd_or_even_check(numbers : list[int] = []) -> None:
    """Check if numbers in a list are odd or even using print_is_odd_or_even."""
    for number in numbers:
        print_is_odd_or_even(number)

numbers1 = [10, 15, 22, 29, 30]
numbers2 = [1, 4, 7, 9, 12]
numbers3 = [100, 150, 200]
print(f"First list check ({numbers1}):")
list_odd_or_even_check(numbers1)
print(f"Second list check ({numbers2}):")
list_odd_or_even_check(numbers2)
print(f"Third list check ({numbers3}):")
list_odd_or_even_check(numbers3)