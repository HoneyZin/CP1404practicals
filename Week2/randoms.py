
"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

The smallest number could have 5 and the largest was 20.


What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

The smallest number could have 3 and the largest was 9.
Line 2 could not produce a 4 as the step was 2 from 3 and all the results were odd numbers.


What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

The smallest number could have 2.5 and the largest was 5.4.
"""

import random


def main():
    print(random.randint(1, 100))


if __name__ == "__main__":
    main()
