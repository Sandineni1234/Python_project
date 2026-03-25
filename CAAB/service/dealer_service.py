from CAAB.utils.common import parse_int
from datetime import datetime
from CAAB.models.Dealer import Dealers
from CAAB.models.comments import CommentsIncidents
from CAAB.models.fileuploader import FileUploader
from CAAB.models import Dealers, dropdowns, user_roles, User
from sqlalchemy import func

def update_dealer(instance, data, user_id, status, stage_ID):
    instance.Address = data.get('Address')
    instance.AskForPolicy = parse_int(data.get('AskForPolicy'))
    instance.CategoryID = parse_int(data.get('CategoryID'))
    instance.CEAReceived = parse_int(data.get('CEAReceived'))
    instance.Comercial = data.get('Comercial')
    instance.CompanyID = data.get('CompanyID')
    instance.EconGroup = data.get('EconGroup')
    instance.email = data.get('email')
    instance.LegalName = data.get('LegalName')
    instance.MandateID = parse_int(data.get('MandateID'))
    instance.Municipality = data.get('Municipality')
    instance.PartnerNameSurname1 = data.get('PartnerNameSurname1')
    instance.PartnerNameSurname2 = data.get('PartnerNameSurname2')
    instance.PartnerNameSurname3 = data.get('PartnerNameSurname3')
    instance.PostalCode = data.get('PostalCode')
    instance.Province = data.get('Province')
    instance.ShareholderNameSurname1 = data.get('ShareholderNameSurname1')
    instance.ShareholderNameSurname2 = data.get('ShareholderNameSurname2')
    instance.ShareholderNameSurname3 = data.get('ShareholderNameSurname3')
    instance.ShareholderPercentage1 = data.get('ShareholderPercentage1')
    instance.ShareholderPercentage2 = data.get('ShareholderPercentage2')
    instance.ShareholderPercentage3 = data.get('ShareholderPercentage3')
    instance.PartnerPercentage1 = data.get('PartnerPercentage1')
    instance.PartnerPercentage2 = data.get('PartnerPercentage2')
    instance.PartnerPercentage3 = data.get('PartnerPercentage3')
    instance.StageId = stage_ID
    instance.statusID = status
    instance.typeID = parse_int(data.get('typeID'))
    instance.Zone = data.get('Zone')
    instance.modified_date = datetime.now()
    instance.ModifiedBy = parse_int(user_id)


def build_dealer(data, user_id, status, stage_ID):
    return Dealers(
        Address=data.get('Address'),
        AskForPolicy=parse_int(data.get('AskForPolicy')),
        CategoryID=parse_int(data.get('CategoryID')),
        CEAReceived=parse_int(data.get('CEAReceived')),
        Comercial=data.get('Comercial'),
        CompanyID=data.get('CompanyID'),
        CreatedBy=parse_int(user_id),
        Creation_date=datetime.now(),
        EconGroup=data.get('EconGroup'),
        email=data.get('email'),
        Isactive=1,
        LegalName=data.get('LegalName'),
        MandateID=parse_int(data.get('MandateID')),
        Municipality=data.get('Municipality'),
        PartnerNameSurname1=data.get('PartnerNameSurname1'),
        PartnerNameSurname2=data.get('PartnerNameSurname2'),
        PartnerNameSurname3=data.get('PartnerNameSurname3'),
        PostalCode=data.get('PostalCode'),
        Province=data.get('Province'),
        ShareholderNameSurname1=data.get('ShareholderNameSurname1'),
        ShareholderNameSurname2=data.get('ShareholderNameSurname2'),
        ShareholderNameSurname3=data.get('ShareholderNameSurname3'),
        ShareholderPercentage1=data.get('ShareholderPercentage1'),
        ShareholderPercentage2=data.get('ShareholderPercentage2'),
        ShareholderPercentage3=data.get('ShareholderPercentage3'),
        PartnerPercentage1=data.get('PartnerPercentage1'),
        PartnerPercentage2=data.get('PartnerPercentage2'),
        PartnerPercentage3=data.get('PartnerPercentage3'),
        StageId=stage_ID,
        statusID=status,
        typeID=parse_int(data.get('typeID')),
        Zone=data.get('Zone'),
)            

def get_dealer_full_details(dealer_id):
    dealer_obj = Dealers.query.filter_by(id=dealer_id).first()
    if not dealer_obj:
        return None

    dealer = Dealers.get_dealer_details(dealer_obj)

    comments_obj = CommentsIncidents.query.filter_by(
        DealersID=dealer_id,
        stageID=dealer.get('StageId')
    ).first()
    comments = CommentsIncidents.to_dict(comments_obj) if comments_obj else {}

    file_records = FileUploader.query.filter_by(
        DealersID=dealer_id,
        stageID=dealer.get('StageId')
    ).all()
    files = {file.Documents.Name: file.to_dict() for file in file_records}

    dealer.update(comments)
    dealer.update(files)

    return dealer

def get_dealer_list_for_user(user_id, page, per_page):
    user_obj = User.query.filter_by(id=user_id).first()
    if not user_obj:
        return None, None

    user_dict = user_obj.to_dict()
    role_menu = user_roles.UserRoleMenus.query.filter_by(id=user_dict['userMenuID']).first()
    if not role_menu:
        return None, None

    menu_ids = role_menu.menu_ids.split(",") if role_menu.menu_ids else []
    stage_ids = [
        menu.StageID for menu in user_roles.Menus.query.filter(user_roles.Menus.id.in_(menu_ids)).all()
        if menu.StageID
    ]

    if not stage_ids:
        return [], {}

    paginate_dealers = Dealers.query.filter(Dealers.StageId.in_(stage_ids)).paginate(page=page, per_page=per_page, error_out=False)

    # return [dealer_to_dict(d) for d in dealers], get_total_dealers()
    dealer_list = [dealer_to_dict(d) for d in paginate_dealers]
    dealer_status_count = get_total_dealers()
    response = {
        'items': dealer_list,
        'current_page': paginate_dealers.page,
        'per_page': paginate_dealers.per_page,
        'total_pages': paginate_dealers.pages,
        'total_items': paginate_dealers.total,
        'has_prev': paginate_dealers.has_prev,
        'has_next': paginate_dealers.has_next,
        'prev_num': paginate_dealers.prev_num,
        'next_num': paginate_dealers.next_num,
        "dealer_status_count" : dealer_status_count
    }
    return response


def dealer_to_dict(dealer):
    return {
        "id": dealer.id,
        "Creation_date": dealer.Creation_date,
        "CreatedBy_firstname": dealer.created_by_user.to_dict().get('first_name') if dealer.created_by_user else None,
        "CreatedBy_last_name": dealer.created_by_user.to_dict().get('last_name') if dealer.created_by_user else None,
        "StageName": dealer.stage.to_dict().get('Stage_name') if dealer.stage else None,
        "StageId": dealer.StageId,
        "StatusID": dealer.statusID,
        "legal_name": dealer.LegalName
    }


def get_total_dealers():
    counts_query = (
        Dealers.query
        .with_entities(Dealers.statusID, func.count(Dealers.id))
        .group_by(Dealers.statusID)
        .all()
    )
    counts_dict = {status_id: count for status_id, count in counts_query}

    status_list = dropdowns.Status.query.all()
    result = {}
    for sta in status_list:
        status_name = sta.to_dict().get('Status_values')
        status_id = sta.to_dict().get('id')
        result[f"{status_name}_Count"] = counts_dict.get(status_id, 0)

    return result
    