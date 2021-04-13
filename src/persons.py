from flask.views import MethodView
from flask import abort, request


class PersonAPI(MethodView):

    def get(self, id):
        """
        Returns a person by ID
        ---
        tags:
          - persons
        parameters:
          - in: path
            name: id
        definitions:
          - schema:
              id: Person
              required:
                - id
                - firstName
                - lastName
                - age
              properties:
                id:
                  type: integer
                  description: the id of the person
                  example: 123
                firstName:
                  type: string
                  description: the first name of the person
                  example: Elon
                lastName:
                  type: string
                  description: the last name of the person
                  example: Musk
                age:
                  type: integer
                  description: the age of the person
                  example: 49
        responses:
          200:
            description: A person object
            schema:
              $ref: '#/definitions/Person'
          404:
            description: Not found error. Person with specified ID not found.
            """
        if id != 123:
            abort(404)

        return {
            "id": id,
            "firstName": "Elon",
            "lastName": "Musk",
            "age": 49
        }

    def post(self):
        """
        Create a new person
        ---
        tags:
          - persons
        parameters:
          - in: body
            name: body
            schema:
              $ref: '#/definitions/Person'
        responses:
          200:
            description: Whether person was created
            schema:
              properties:
                created:
                  type: boolean
                  description: Whether person was created
                  example: true
        """
        return {
            "created": True
        }
