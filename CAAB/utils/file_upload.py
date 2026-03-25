import os
from werkzeug.utils import secure_filename
from datetime import datetime
from CAAB.models import fileuploader
from CAAB.db import db
from flask import request
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

class file_uploads:

# Update this to your actual upload folder
    def __init__(self, file_keys, dealer_id, stage_id, user_id):
        self.doc_names = file_keys
        self.dealer_id = dealer_id
        self.stage_id = stage_id
        self.user_id = user_id
        self.saved_files = []

    def get_files(self):
        return({k: request.files[k] 
                      for k in self.doc_names 
                      if k in request.files})
    
    def Create_files(self):
        files_dict = self.get_files()
        try:
            for key, file in files_dict.items():
                files = self.store_files(file)
                self.upload_files(key, files)
        except Exception as e:
            for filepath in self.saved_files:
                if os.path.exists(filepath):
                    os.remove(filepath)
            raise RuntimeError("File upload failed and was rolled back")

    def update_files(self):
        files_dict = self.get_files()
        for key, file in files_dict.items():
            key_id = fileuploader.Documents.query.filter_by(Name = key).first()
            get_file = fileuploader.FileUploader.query.filter_by(DealersID = self.dealer_id, DocumentID = key_id.id_doc).first()
            if(get_file is None):
                files = self.store_files(file)
                self.upload_files(key, files)
            elif get_file is not None:
                filepath = get_file.FilePath
                if os.path.exists(filepath):
                    os.remove(filepath)
                    files = self.store_files(file)
                    get_file.FilePath = files["save_path"]
                    get_file.filename = files["newFilename"]
                    get_file.ModifiedBy = self.user_id
                    get_file.Modified_date = datetime.now()


    def store_files(self, file):
        OGfilename = secure_filename(file.filename)
        filenameparts = OGfilename.split(".")
        newFilename = filenameparts[0]+ str(int(datetime.now().strftime("%Y%m%d%H%M%S%f")))+ '.' +filenameparts[1]
        save_path = os.path.join(UPLOAD_FOLDER, newFilename)
        file.save(save_path)
        return {"newFilename" : newFilename, "save_path": save_path}
    
    def upload_files(self, key, file):
        if file:
            try: 
                uploadedDocumentID = fileuploader.Documents.query.filter_by(Name = key).first()
                file_record = fileuploader.FileUploader(
                        DealersID=self.dealer_id,
                        FilePath=file["save_path"],
                        filename=file["newFilename"],
                        stageID=self.stage_id,
                        CreatedBy=self.user_id,
                        isactive=1,
                        Created_date=datetime.now(),
                        DocumentID = uploadedDocumentID.id_doc
                        )
                db.session.add(file_record)
                self.saved_files.append(file["save_path"])
            except Exception as e:
                self.saved_files.append(file["save_path"])
                raise RuntimeError(f"Error uploading file '{key}': {e}")