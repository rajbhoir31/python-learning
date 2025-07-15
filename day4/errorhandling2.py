def open_file_safely():
    """
    Asks user for a filename until a valid file is found.
    Opens and prints its contents.
    """
    while True:
        filename = input("Enter filename to open: ")
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                print("✅ File opened successfully!")
                print("-" * 30)
                print(contents)
                print("-" * 30)
                break
        except FileNotFoundError:
            print(f"❌ File '{filename}' not found. Please try again.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
