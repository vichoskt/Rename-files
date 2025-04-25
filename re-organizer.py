import os 
import time
import shutil

path = "D:/Escritorio/Datos de prueba"
dir_list = os.listdir(path)

photo_type = ["jpg", "jpeg", "png", "bmp", "gif", "heic", "webp"]
video_type = ["mp4", "avi", "mov", "mkv", "flv", "wmv", "webm", "mpeg", "3gp"]

months_translate = {
    "Jan": "1. Enero",
    "Feb": "2. Febrero",
    "Mar": "3. Marzo",
    "Apr": "4. Abril",
    "May": "5. Mayo",
    "Jun": "6. Junio",
    "Jul": "7. Julio",
    "Aug": "8. Agosto",
    "Sep": "9. Septiembre",
    "Oct": "10. Octubre",
    "Nov": "11. Noviembre",
    "Dec": "12. Diciembre"
}

for i in dir_list:
    full_path = os.path.join(path, i)

    if os.path.isfile(full_path):
        modified_time = os.path.getmtime(full_path)
        formated_modified_time = time.ctime(modified_time)

        # Get the hierarchy
        year = formated_modified_time[20:24]
        month_short = formated_modified_time[4:7]
        month = months_translate.get(month_short, "Unknown month")
        file_type = os.path.splitext(full_path)[1][1:].lower()

        # Directories
        year_folder = os.path.join(path, year)
        month_folder = os.path.join(path, year, month)
        picture_folder = os.path.join(path, year, month, "FOTOS")
        video_folder = os.path.join(path, year, month, "VIDEOS")

        # Creation hierarchy
        if not os.path.isdir(year_folder):
            os.mkdir(year_folder)
        if not os.path.isdir(month_folder):
            os.mkdir(month_folder)
        if file_type in photo_type:
            if not os.path.isdir(picture_folder):
                os.mkdir(picture_folder)
        if file_type in video_type:
            if not os.path.isdir(video_folder):
                os.mkdir(video_folder)

        # Move files
        if file_type in photo_type:
            shutil.move(full_path, picture_folder)
        if file_type in video_type:
            shutil.move(full_path, video_folder)
                
        