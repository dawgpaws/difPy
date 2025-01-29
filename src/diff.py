import difPy
import argparse

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Find and move duplicate images")
    
    # Add arguments for input and output paths
    parser.add_argument('in_folder', type=str, help='Path to the folder to search for duplicates')
    parser.add_argument('out_folder', type=str, help='Path to move duplicates to')

    # Parse arguments
    args = parser.parse_args()

    # Run the DifPy operations
    dif = difPy.build([args.in_folder], in_folder=True)
    search = difPy.search(dif)
    print(search.result)
    search.move_to(args.out_folder)

if __name__ == "__main__":
    main()