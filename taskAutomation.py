import os
import shutil

def automate_files():
    # Define source and destination
    source_dir = "./my_photos"
    dest_dir = "./images_folder"
    # Ensure source exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

    # Create destination if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Loop through files in source
    moved_count = 0
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            shutil.move(os.path.join(source_dir, filename), dest_dir)
            print(f"Moved: {filename}")
            moved_count += 1

    if moved_count == 0:
        print("No .jpg files found to move.")
    else:
        print(f"Moved {moved_count} file(s) from {source_dir} to {dest_dir}.")

    return moved_count

# Note: Ensure the 'my_photos' folder exists before running


if __name__ == "__main__":
    try:
        automate_files()
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")

