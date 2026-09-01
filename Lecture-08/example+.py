def example_w_plus_mode():
    with open("example.txt",'w+') as file:
        file.write("This is the first line in the file.\n")
        file.write("This is the second line in the file.\n")
        file.seek(0)  # Move the file pointer to the beginning of the file
        content = file.read()
        print("Content of the file after writing:")
        print(content)
example_w_plus_mode()