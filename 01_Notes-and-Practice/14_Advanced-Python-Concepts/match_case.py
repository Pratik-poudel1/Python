# Match Case:
# Python 3.10 introduced the match-case statement, which is a more compact 
# and readable alternative to the if-elif-else statement.
# It allows you to write more concise and readable code for complex conditional statements.

# Example 1:
x = 5
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case _:
        print("x is not 1, 2, or 3")

# Example 2:
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown"
# Usage:
print(http_status(200)) # Output: "OK"
print(http_status(404)) # Output: "Not Found"
print(http_status(500)) # Output: "Internal Server Error"
print(http_status(600)) # Output: "Unknown"

