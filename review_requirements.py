import os
import sys

def main():
    # Check if 'requirements.txt' exists in the current directory
    if os.path.isfile('requirements.txt'):
        print("requirements.txt file found.")
        sys.exit(0)  # Exit with a success code (0)
    else:
        print("requirements.txt file not found.")
        sys.exit(1)  # Exit with a non-success code (non-zero)

if __name__ == "__main__":
    main()
