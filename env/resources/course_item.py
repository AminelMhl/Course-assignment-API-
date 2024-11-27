import uuid
#from flask import abort, request
from flask import abort
from flask_smorest import Blueprint
from flask.views import MethodView
from db import course_items
##add
from schemas import CourseitemSchema, CourseitemUpdateSchema
#blp = Blueprint("course_items", __name__, description="Operations on course_items")
blp = Blueprint("Course_items", "course_items", description="Operations on course_items")
@blp.route("/course_item/<string:course_item_id>")
class Course_item(MethodView):
    def get(self, course_item_id):
        try:
            return course_items[course_item_id]
        except KeyError:
            abort(404, message="Course_item not found.")
    def delete(self, course_item_id):
        try:
           del course_items[course_item_id]
           return {"message": "Course_item deleted."}
        except KeyError:
            abort(404, message="Course_item not found.")
    #add 
    @blp.arguments(CourseitemUpdateSchema)
    #def put(self, course_item_id):
    def put(self, course_item_data, course_item_id):
    #delete the following json instruction
        #course_item_data = request.get_json()
    #comment
        # if "type" not in course_item_data or "name" not in course_item_data:
        #     abort(
        #         400,
        #         message="Bad request. Ensure 'type', and 'name' are included in the JSON payload.",
        #     )
        try:
            course_item = course_items[course_item_id]
            course_item |= course_item_data
            return course_item
        except KeyError:
            abort(404, message="Course_item not found.")
@blp.route("/course_item")
class Course_itemList(MethodView):
    def get(self):
        return {"course_items": list(course_items.values())}
    #add 
    @blp.arguments(CourseitemSchema)
    #def post(self):
    def post(self, course_item_data):
    #delete the following json instruction
        #course_item_data = request.get_json()
    #comment    
        # if (
        #     "type" not in course_item_data
        #     or "specialization_id" not in course_item_data
        #     or "name" not in course_item_data
        # ):
        #     abort(
        #         400,
        #         message="Bad request. Ensure 'type', 'specialization_id', and 'name' are included in the JSON payload.",
        #     )
        # for course_item in course_items.values():
        #     if (
        #         course_item_data["name"] == course_item["name"]
        #         and course_item_data["specialization_id"] == course_item["specialization_id"]
        #     ):
        #         abort(400, message="Course_item already exists.")
        course_item_id = uuid.uuid4().hex
        course_item = {**course_item_data, "id": course_item_id}
        course_items[course_item_id] = course_item
        return course_item