import uuid
from flask_smorest import Blueprint, Api
from flask import abort, request
from flask.views import MethodView
from db import specializations
blp=Blueprint("specialization", __name__, description="operations")
class Specialization(MethodView):
    def get(self, specialization_id):
        try:
            return specializations[specialization_id]
        except KeyError:
            abort(404, description ="Specialization not found.")
    def delete(self, specialization_id):
        try:
            del specializations[specialization_id]
            return {"message": "Specialization deleted."}
        except KeyError:
            abort(404, description ="Specialization not found.")

class SpecializationList(MethodView):
    def get(self):
        return {"specializations": list(specializations.values())}
    def post(self):
        specialization_data = request.get_json()
        if "name" not in specialization_data:
            abort(400,description ="Bad request. Ensure 'name' is included in the JSON payload.",)
        for specialization in specializations.values():
            if specialization_data["name"] == specialization["name"]:
                abort(400, description="Specialization already exists.")
        specialization_id = uuid.uuid4().hex
        specialization = {**specialization_data, "id": specialization_id}
        specializations[specialization_id] = specialization
        return specialization