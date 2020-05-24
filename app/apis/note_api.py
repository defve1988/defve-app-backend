from flask import request, jsonify
from flask_restful import Resource, abort
from app.extensions import api,db, KEY
from app.models.note import *

todo_schema = TodoSchema(many = True)
note_schema = NoteSchema(many = True)
flashcard_schema = FlashCardSchema(many = True)
timeline_schema = TimelineSchema(many = True)

table_index = {
    'todo':[Todo, todo_schema],
    'note':[Note, note_schema],
    'flashcard':[FlashCard, flashcard_schema],
    'timeline':[Timeline, timeline_schema],
}

class NoteAPI(Resource):
    def get(self, table):
        Table = table_index[table][0]
        Table_schema = table_index[table][1]

        notes = Table.query.all()
        res = Table_schema.dump(notes)
        return jsonify(res)

    def put(self, table):
        try:
            Table = table_index[table][0]
            Table_schema = table_index[table][1]

            request_id = request.json['id']
            data = Table.query.get(request_id)
            data_query.update(data, request.json)
            db.session.commit()
            res = Table_schema.dump([data])
            return jsonify(res)
        except:
            abort(404, message="Update note error.")

    def post(self, table):
        try:
            Table = table_index[table][0]
            Table_schema = table_index[table][1]

            new_data = Table(request.json)
            db.session.add(new_data)
            db.session.commit()
            res = Table_schema.dump([new_data])
            return jsonify(res)
        except:
            abort(404, message="Post note error.")

    def delete(self, table):
        try:
            Table = table_index[table][0]
            Table_schema = table_index[table][1]

            request_id = request.json['id']
            data = Table.query.filter_by(id=request_id).first()
            db.session.delete(data)
            db.session.commit()
            res = Table_schema.dump([data])
            return jsonify(res)
        except:
            abort(404, message="Delete note error.")

class NoteAPI_Filter(Resource):
    def get(self, table):
        Table = table_index[table][0]
        Table_schema = table_index[table][1]

        data = Table.query.filter_by(**request.json).all()
        res = Table_schema.dump(data)
        return jsonify(res)

class ClearTable(Resource):
    def delete(self, table):
        try:
            Table = table_index[table][0]
            Table_schema = table_index[table][1]
            if request.json['key'] == KEY:
                data = Table.query.all()
                for i in data:
                    db.session.delete(i) 
                db.session.commit()
                return jsonify({"msg":"{} is cleared.".format(table)})
        except:
            abort(404, message="Delete table error.")


api.add_resource(NoteAPI, '/api/note/<table>')
api.add_resource(NoteAPI_Filter, '/api/note_filter/<table>')
api.add_resource(ClearTable, '/api/note_clear/<table>')

