import argparse

def main():
    parser = argparse.ArgumentParser(description='Mathematical operations')
    parser.add_argument('-equation', help='Enter your equation')

    args = parser.parse_args()

    if args.equation:
        print(f"Equation provided: {args.equation}")
        # Perform further operations with the equation if needed
    else:
        print("No equation provided.")

if __name__ == "__main__":
    main()
