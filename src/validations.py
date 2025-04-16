from marshmallow import Schema,fields

class FamilySchema(Schema):
    age=fields.Int(validate=lambda n:n>15)
    lucky_numbers=fields.List(fields.Int(),required=True)
    name=fields.Str(required=True)


