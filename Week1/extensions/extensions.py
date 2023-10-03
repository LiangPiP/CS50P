text = input("File name: ").lower().strip()
type={
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}


print(type.get(text.split(sep='.')[-1],"application/octet-stream"))