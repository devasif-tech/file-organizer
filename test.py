import os
import shutil


print("Current Working Directory is:")
print(os.getcwd())

target_folder = "MINI PROJECT"

folders = {
    "Images" : [".jpg", ".jpeg", ".png"],
    "Music" : [".mp3", ".wav"],
    "Videos" : ["mp4"],
    "TextFiles" : [".txt", ".docx"],
    "python" : [".py"],
}

for file in os.listdir(target_folder):
    print("Scanning file:", file)
    filename, extension = os.path.splitext(file)
    

    if extension == "":
        continue

    for folder_name,extensions in folders.items():
        if extension.lower() in extensions:
            dest_folder = os.path.join(target_folder, folder_name)
            
            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)

            #move karna
            source_path = os.path.join(target_folder,file)
            destination_path = os.path.join(dest_folder,file)
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' -> '{folder_name}'") 