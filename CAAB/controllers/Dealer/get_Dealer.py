from flask import request, jsonify
from . import Dealer_bp
from CAAB.models.Dealer import Dealers
from CAAB.models.comments import CommentsIncidents
from CAAB.models.fileuploader import FileUploader
from flask_jwt_extended import jwt_required


@Dealer_bp.route('/get_dealer', methods=['GET'])
@jwt_required()
def get_Dealer():
        dealer_id = request.args.get('DealerID')
        try :
            dealer = Dealers.get_dealer_details(Dealers.query.filter_by(id = dealer_id).first())
            comments = CommentsIncidents.to_dict(CommentsIncidents.query.filter_by(DealersID = dealer_id, stageID = dealer['StageId']).first())
            file_records = FileUploader.query.filter_by(DealersID=dealer_id, stageID=dealer['StageId']).all()
            files = {file.Documents.Name: file.to_dict() for file in file_records}  # Convert each record to a dict
            dealer.update(comments)
            dealer.update(files)
            return jsonify(dealer)
        except Exception as e:
            return("Error", e)