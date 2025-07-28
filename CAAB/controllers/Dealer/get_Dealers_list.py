from flask import request, jsonify
from . import Dealer_bp
from CAAB.db import db
from CAAB.models import Dealers, User, dropdowns
from flask_jwt_extended import jwt_required, get_jwt_identity

@Dealer_bp.route('/Dealer_list', methods=['GET'])
@jwt_required()
def get_Dealers():
    get_user = User.to_dict(User.query.filter_by(id = get_jwt_identity()).first())
    if(get_user.get('userMenuID') == 7):
        columns = Dealers.query.all()
        response_object = {
             'Success' : True,
             'Status' : 200,
            'data' : [total(dealer) for dealer in (Dealers.query.all())],"Total": total_dealers()
        }
        return jsonify(response_object)
    else:
        return jsonify({"message": "Unauthorized"})
    
def total(self):
        return{
            "id": self.id,
            "Creation_date": self.Creation_date,
            "CreatedBy_firstname": self.created_by_user.to_dict().get('first_name') if self.created_by_user else None,
            "CreatedBy_last_name": self.created_by_user.to_dict().get('last_name') if self.created_by_user else None,
            "StageName": self.stage.to_dict().get('Stage_name') if self.stage else None,
            "StageId": self.StageId,
            "StatusID" : self.statusID,
            'legal_name' : self.LegalName
        }

def all_status():
     status = dropdowns.Status.query.all()
     return status

def total_dealers():
     status = all_status()
    #  for sta in status:
    #     sta +"_Count" = {Dealers.query.filter_by(status = sta).count()}
     all_counts = {sta.to_dict().get('Status_values') +"_Count": Dealers.query.filter_by(statusID = sta.to_dict().get('id')).count() for sta in status}
     return all_counts