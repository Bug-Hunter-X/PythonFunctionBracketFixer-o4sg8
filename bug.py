def function_with_unclosed_bracket(x):
    if x > 5:
        return x * 2
    else:
        return x + 3 # Missing closing bracket

result = function_with_unclosed_bracket(7)