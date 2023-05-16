#!/usr/bin/python3

while True:
    try:
        x = int(input("Please enter a number: "))
        break;
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        print("Something doesn't seem right...")
    except KeyboardInterrupt:
        print("\nNo. You are not allowed to do that!")
    except EOFError:
        print("\nEOF is not valid character. Try again...")
