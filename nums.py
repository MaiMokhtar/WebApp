from flask_restx import Namespace, Resource, fields
from models import Num
from flask_jwt_extended import jwt_required
from flask import request

num_ns = Namespace("num")

num_model = num_ns.model(
    "Num",
    {"id": fields.Integer(), "no": fields.Integer()},
)


@rnum_ns.route("/nums")
class NumsResource(Resource):
    @num_ns.marshal_list_with(num_model)
    def get(self):
        """Get all nums"""

        nums = Num.query.all()

        return nums


@num_ns.route("/num/<int:id>")
class NumResource(Resource):
    @num_ns.marshal_with(num_model)
    def get(self, id):
        """Get a num by id"""
        num = Num.query.get_or_404(id)

        return num


@num_ns.route("/percentage/<int:id>", methods=["POST"])
def percentage():
    data = request.get_json()
    num1 = Num.query.get(id)
    num2 = data.get("num2")

    result = (num1 / num2) * 100

    return jsonify({"result": result})
