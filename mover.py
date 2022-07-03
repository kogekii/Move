import os

downloadsFolder = "E:/Descargas/"
PdfFolder = "E:/Descargas/pdfs/"
OfficeFolder = "E:/Descargas/office/"
ZipFolder = "E:/Descargas/zip/"
VideoFolder = "E:/Descargas/videos/"
InstallFolder = "E:/Descargas/instaladores/"
AudioFolder = "E:/Descargas/audios/"
ImageFolder = "E:/Descargas/image/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, PdfFolder + filename)
        if extension in [".xlsx", ".ppt", ".pptx", ".docx", ".odt"]:
            os.rename(downloadsFolder + filename, OfficeFolder + filename)
        if extension in [".zip", ".rar", ".7z"]:
            os.rename(downloadsFolder + filename, ZipFolder + filename)
        if extension in [".mp4"]:
            os.rename(downloadsFolder + filename, VideoFolder + filename)
        if extension in [".exe"]:
            os.rename(downloadsFolder + filename, InstallFolder + filename)
        if extension in [".aac", ".mp3"]:
            os.rename(downloadsFolder + filename, AudioFolder + filename)
        if extension in [".jpg", ".jpeg", ".png"]:
            os.rename(downloadsFolder + filename, ImageFolder + filename)