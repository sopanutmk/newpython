def display_info (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
display_info(name="MIX" , age=13 , city="New York")