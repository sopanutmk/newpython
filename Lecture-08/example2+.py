def example_a_plus_mode():
    with open("example_a+.txt",'a+') as file:
        file.seek(0)  # Move the file pointer to the beginning of the file
        content = file.read()
        print("Content of the file before appending:")
        print(content)

        file.write("Appending a new line to the end.\n")

        file.seek(0)  # Move the file pointer to the beginning of the file again
        update_content = file.read()
        print("\nUpdated content of the file:")
        print(update_content)

example_a_plus_mode()