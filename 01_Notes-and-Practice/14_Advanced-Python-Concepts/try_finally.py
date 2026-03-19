# Try with finally clause:
# The finally block is executed whether there is an exception raised in the try block or not.

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print("Error:",e)
        return
    finally:
        print("No exception")
main()
