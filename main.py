# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

#print(arithmetic_arranger(["3 - 223","23 + 1","23 + 21","23 + 1"], False))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], False))

# Run unit tests automatically
main(module='test_module', exit=False)