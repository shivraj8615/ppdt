import os

# === Settings ===
folder_path = "pics"  # Change this if your folder is named differently
file_extensions = (".jpg", ".jpeg", ".png")

# === Rename Logic ===
def rename_images_in_folder(path):
    files = [f for f in os.listdir(path) if f.lower().endswith(file_extensions)]
    files.sort()  # Optional: Ensures consistent order

    for idx, filename in enumerate(files, start=1):
        extension = os.path.splitext(filename)[1]
        new_name = f"test{idx}{extension.lower()}"
        src = os.path.join(path, filename)
        dst = os.path.join(path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")

    print("\n✅ Renaming complete!")

# === Run Script ===
if __name__ == "__main__":
    rename_images_in_folder(folder_path)
