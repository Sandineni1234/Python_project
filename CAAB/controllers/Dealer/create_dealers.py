from . import Dealer_bp
from CAAB.models import Dealers
from CAAB.models.comments import CommentsIncidents
from CAAB.models.fileuploader import FileUploader
from flask import request, jsonify, json
from sqlalchemy.inspection import inspect
from datetime import datetime
from CAAB.db import db
from CAAB.middlewares import logger
from flask_jwt_extended import jwt_required, get_jwt_identity
from CAAB.utils.file_upload import file_uploads
from CAAB.utils.common import parse_int
from CAAB.service import dealer_service, comments_service
from CAAB.utils.enum import DealerStatus, DealerStage


@Dealer_bp.route('/dealer_creation_stage', methods=['POST'])
@jwt_required()
def dealer_creation_stage():
    DealerID = parse_int(request.args.get("DealerID"))
    try:
            file_keys = ['CreationDeedDoc', 'CreditLineDoc', 'ProxyDeedDoc', 'CorporateIncomeTaxDoc']
            stage_ID = 1
            data = request.form 
            user_id = get_jwt_identity()
            Dealer_data = data.to_dict()
            status = DealerStatus.DRAFT if(Dealer_data.get("isDraft") == "true") else DealerStatus.APPROVED
            ExistingDealer = Dealers.query.filter_by(id = DealerID).first()
            ExistingComments = CommentsIncidents.query.filter_by(DealersID = DealerID).first()
            if(status == DealerStatus.APPROVED):
                stage_ID = DealerStage.CREDIT_ANALYSIS
            elif(status == DealerStatus.DRAFT):
                stage_ID = DealerStage.DEALER_CREATION
            if(ExistingDealer):
                dealer_service.update_dealer(ExistingDealer, Dealer_data, user_id, status, stage_ID)
                comments_service.update_comments(ExistingComments, Dealer_data, user_id, stage_ID)
                upload_files = file_uploads(file_keys, DealerID ,stage_ID, user_id)
                upload_files.update_files()
                # for key, value in Dealer_data.items():
                #     if hasattr(ExistingDealer, key) and value != getattr(ExistingDealer, key):
                #         if isinstance(getattr(ExistingDealer, key, None), int):
                #             setattr(ExistingDealer,key, parse_int(value))
                #         else:
                #             setattr(ExistingDealer,key, value)
                #     elif hasattr(ExistingComments, key) and value != getattr(ExistingComments, key):
                #         setattr(ExistingComments, key, value)
                message = "Dealer Updated Successfully!"
            elif(ExistingDealer is None):
                new_dealer = dealer_service.build_dealer(Dealer_data, user_id, status, stage_ID)
                db.session.add(new_dealer)
                db.session.flush()
                
                new_comments = comments_service.build_comments(new_dealer.id, Dealer_data, user_id, stage_ID)
                db.session.add(new_comments)
                db.session.flush()

                upload_files = file_uploads(file_keys, new_dealer.id ,stage_ID, user_id)
                upload_files.Create_files()
                message = "Dealer Created Successfully!"

            
            db.session.commit()
            return jsonify({"message": message}), 200
    except Exception as e:
            db.session.rollback()
            logger.exception("Dealer creation failed: %s", str(e))
            return jsonify({"error": str(e)}), 500