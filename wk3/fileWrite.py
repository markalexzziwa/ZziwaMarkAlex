file_name = "data_science.txt"

with open(file_name, "w") as file:
    file.write("i love python\n")
    file.write("am a data scientist\n")

print(f"File '{file_name}' has been created successfully!")
