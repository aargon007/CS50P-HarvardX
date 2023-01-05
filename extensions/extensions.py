#get the name of a file
extensions=input("File name: ")
extensions=extensions.lower().strip()

#outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:.gif.jpg.jpeg.png.pdf.txt.zip
if ".gif" in extensions:
    print("image/gif")
elif ".jpg" in extensions:
    print("image/jpeg")
elif ".jpeg" in extensions:
    print("image/jpeg")
elif ".png" in extensions:
    print("image/png")

elif ".pdf" in extensions:
    print("application/pdf")
elif ".txt" in extensions:
    print("text/plain")
elif ".zip" in extensions:
    print("application/zip")
#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

else:
    print("application/octet-stream")