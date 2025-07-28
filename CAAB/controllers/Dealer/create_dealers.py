from . import Dealer_bp
from CAAB.models import Dealers
from CAAB.models.comments import CommentsIncidents
from CAAB.models.fileuploader import FileUploader
from flask import request, jsonify, json
from datetime import datetime
from CAAB.db import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from CAAB.utils.file_upload import save_uploaded_files


@Dealer_bp.route('/dealer_creation_stage', methods=['POST'])
@jwt_required()
def dealer_creation_stage():
    data = request.form
    Dealer_data = data.to_dict()
    if(Dealer_data.get("isDraft") == "true"):
       Dealer_data["isDraft"] =  3
    elif(Dealer_data.get("isDraft") == "false"):
        Dealer_data["isDraft"] = 1
    try:
        new_dealer = Dealers(
            Address=Dealer_data.get('Address'),
            AskForPolicy=int(Dealer_data.get('AskForPolicy')),
            CategoryID=Dealer_data.get('CategoryID'),
            CEAReceived=int(Dealer_data.get('CEAReceived')),
            Comercial=Dealer_data.get('Comercial'),
            CompanyID=Dealer_data.get('CompanyID'),
            CreatedBy=int(get_jwt_identity()),
            Creation_date=datetime.now(),
            EconGroup=Dealer_data.get('EconGroup'),
            email=Dealer_data.get('email'),
            Isactive=1,
            LegalName=Dealer_data.get('LegalName'),
            MandateID=Dealer_data.get('MandateID'),
            ModifiedBy=Dealer_data.get('ModifiedBy'),
            Municipality=Dealer_data.get('Municipality'),
            PartnerNameSurname1=Dealer_data.get('PartnerNameSurname1'),
            PartnerNameSurname2=Dealer_data.get('PartnerNameSurname2'),
            PartnerNameSurname3=Dealer_data.get('PartnerNameSurname3'),
            PostalCode=Dealer_data.get('PostalCode'),
            Province=Dealer_data.get('Province'),
            ShareholderNameSurname1=Dealer_data.get('ShareholderNameSurname1'),
            ShareholderNameSurname2=Dealer_data.get('ShareholderNameSurname2'),
            ShareholderNameSurname3=Dealer_data.get('ShareholderNameSurname3'),
            ShareholderPercentage1=Dealer_data.get('ShareholderPercentage1'),
            ShareholderPercentage2=Dealer_data.get('ShareholderPercentage2'),
            ShareholderPercentage3=Dealer_data.get('ShareholderPercentage3'),
            PartnerPercentage1=Dealer_data.get('PartnerPercentage1'),
            PartnerPercentage2=Dealer_data.get('PartnerPercentage2'),
            PartnerPercentage3=Dealer_data.get('PartnerPercentage3'),
            StageId= 1, #Dealer_data.get("StageId") 1 is Dealer creation,
            statusID=Dealer_data.get('isDraft'),
            typeID=Dealer_data.get('typeID'),
            Zone=Dealer_data.get('Zone'),
            modified_date=Dealer_data.get('modified_date')  # optional
        )
        db.session.add(new_dealer)
        db.session.flush()

        new_comments = CommentsIncidents(
            DealersID   = new_dealer.id,
            Comments    = Dealer_data.get("Comments"),
            Incidents   = Dealer_data.get("Incidents"),
            stageID     = 1, #Dealer_data.get("StageId") 1 is Dealer creation,
            CreatedBy   = int(get_jwt_identity()),
            isactive    = 1
        )
        db.session.add(new_comments)
        db.session.flush()

        file_keys = ['CreationDeed', 'CreditLineDoc', 'ProxyDeedDoc', 'CorporateTaxDoc']
        files_dict = {k: request.files[k] for k in file_keys if k in request.files}
        save_uploaded_files(
            files_dict=files_dict,
            dealer_id=new_dealer.id,
            stage_id=1, #Dealer_data.get("stageID"),
            created_by=int(get_jwt_identity())
    )
        
        db.session.commit()
        return jsonify({"message": "Dealer created successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return jsonify({"error": str(e)}), 500
    
