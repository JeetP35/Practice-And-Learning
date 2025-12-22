file_counts = {"jpg": 10, "png": 23, "gif": 4, "tiff": 2}
print("File counts dictionary:", file_counts)

print("Number of png files:", file_counts["png"])

print("jpg in file_counts?:", "jpg" in file_counts)

file_counts["gif"] = 8
del file_counts["tiff"]
print("Updated file counts dictionary:", file_counts)

folder = {".py": 5, ".txt": 12, ".csv": 4, ".jpg": 9}
for ext, count in folder.items():
    print("There are {} files with the {} extension".format(count, ext))
for ext in folder.keys():
    print("File extension:", ext)
for count in folder.values():
    print("File count:", count)