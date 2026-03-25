from CAAB.models.comments import CommentsIncidents
from CAAB.utils.common import parse_int
from datetime import datetime

def build_comments(dealer_id, data, user_id, stage_ID):
    return CommentsIncidents(
        DealersID=parse_int(dealer_id),
        Comments=data.get("Comments"),
        Incidents=data.get("Incidents"),
        stageID=stage_ID,
        CreatedBy=parse_int(user_id),
        isactive=1
    )

def update_comments(instance, data, user_id, stage_ID):
    instance.Comments = data.get("Comments")
    instance.Incidents = data.get("Incidents")
    instance.stageID = stage_ID
    instance.ModifiedBy = parse_int(user_id)
    instance.Modified_date = datetime.now()