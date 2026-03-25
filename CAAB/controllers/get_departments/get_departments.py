from CAAB.models.department import Department
from . import departments_dp
from flask import jsonify

@departments_dp.route('/departments', methods=['GET'])
def get_departments():
    dept = Department.query.all()
    departments_list = [Department.to_dict(depts) for depts in dept]
    return(jsonify(departments_list))