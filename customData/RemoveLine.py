import os

folder_path = "./labels"  # <-- Change this to your folder path

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r") as f:
            lines = f.readlines()

        filtered_lines = [line for line in lines if line.strip() and line.strip().split()[0] != "0"]

        # Overwrite the original file
        with open(file_path, "w") as f:
            f.writelines(filtered_lines)

print("All files processed. Lines starting with 0 removed.")
