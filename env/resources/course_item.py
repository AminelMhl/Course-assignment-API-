import uuid
from flask_smorest import Blueprint, Api
from flask import abort, request
from flask.views import MethodView
from db import course_items
blp=Blueprint("Course Item", __name__, description="operations")
class course_item(MethodView):
    def get(self, course_item_id):
        try:
            del course_items[course_item_id]
            return {"message": "Course_item deleted."}
        except KeyError:
            abort(404, description ="Course_item not found.")
    def delete(self, course_item_id):
        try:
            del course_items[course_item_id]
            return {"message": "Course_item deleted."}
        except KeyError:
            abort(404, description ="Course_item not found.")    
    def put(self, course_item_id):
        course_item_data = request.get_json()
        if "type" not in course_item_data or "name" not in course_item_data:
            abort(400,description ="Bad request. Ensure 'type', and 'name' are included in the JSON payload.",)
        try:
            course_item = course_items[course_item_id]
            course_item |= course_item_data
            return course_item
        except KeyError:
            abort(404, description ="Course_item not found.")

class course_itemList(MethodView):
    def get(self):
        return {"course_items": list(course_items.values())}
    def post(self):
        course_item_data = request.get_json()
        if (
        "type" not in course_item_data
        or "specialization_id" not in course_item_data
        or "name" not in course_item_data
        ):
            abort(400,description ="Bad request. Ensure 'type', 'specialization_id', and 'name' are included in the JSON payload.",)

        for course_item in course_items.values():
            if (
            course_item_data["name"] == course_item["name"]
            and course_item_data["specialization_id"] == course_item["specialization_id"]
            ):
                abort(400, description ="Course_item already exists.")
        course_item_id = uuid.uuid4().hex
        course_item = {**course_item_data, "id": course_item_id}
        course_items[course_item_id] = course_item
        return course_item, 201
    