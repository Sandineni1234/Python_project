import os
from werkzeug.utils import secure_filename
from datetime import datetime
from CAAB.models import fileuploader
from CAAB.db import db

# Update this to your actual upload folder
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

def save_uploaded_files(files_dict, dealer_id, stage_id, created_by):
    """
    Save uploaded files to disk and create DB entries.
    
    :param files_dict: dict of key to file objects from request.files
    :param dealer_id: int - dealer's ID
    :param stage_id: int - stage ID to associate file with
    :param created_by: int - user ID
    :return: list of saved filenames
    """
    saved_files = []

    for key, file in files_dict.items():
        if file:
            OGfilename = secure_filename(file.filename)
            filenameparts = OGfilename.split(".")
            newFilename = filenameparts[0]+ str(int(datetime.now().strftime("%Y%m%d%H%M%S%f")))+ '.' +filenameparts[1]
            save_path = os.path.join(UPLOAD_FOLDER, newFilename)
            file.save(save_path)
            # uploadedDocumentID = fileuploader.Documents.query.filter_by(Name = deealer_)


            file_record = fileuploader.FileUploader(
                DealersID=dealer_id,
                FilePath=save_path,
                filename=newFilename,
                stageID=stage_id,
                CreatedBy=created_by,
                isactive=1,
                Created_date=datetime.now(),
                DocmentID = 1
            )
            db.session.add(file_record)
            saved_files.append(newFilename)

    return saved_files

# def get_files()