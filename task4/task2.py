
user_input = input("Enter data to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
append_data = input("Enter data to append to the file: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
