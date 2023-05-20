""" Component 6 - Statement formatter
Make the code look better with decorative symbols
"""


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


print(formatter('=', 'Welcome!'))
print(formatter('*', 'Correct!'))
print(formatter('.', 'Goodbye!'))
