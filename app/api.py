from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemon.db'
db = SQLAlchemy(app)
api = Api(app)

class PokemonModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    edible = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return '<Pokemon: name={}, edible={}, description={}>'.format(self.name,self.edible,self.description)

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, help='Pokemon\'s name', required=True)
user_args.add_argument('edible', type=bool, help='Can you eat this Pokemon?', required=True)
user_args.add_argument('description', type=str, help='', required=False)

pokemonFields = {
    'id': fields.Integer,
    'name': fields.String,
    'edible': fields.Boolean,
    'description': fields.String
}

class Pokemons(Resource):
    @marshal_with(pokemonFields)
    def get(self):
        pokemons = PokemonModel.query.all()
        return pokemons, 200

    @marshal_with(pokemonFields)
    def post(self):
        args = user_args.parse_args()
        pokemon = PokemonModel(name=args['name'], edible=args['edible'], description=args['description'])
        db.session.add(pokemon)
        db.session.commit()
        pokemons = PokemonModel.query.all()
        return pokemons, 201

class Pokemon(Resource):
    @marshal_with(pokemonFields)
    def get(self, id):
        pokemon = PokemonModel.query.filter_by(id=id).first()
        if not pokemon:
            abort(404, "Pokemon not found")
        return pokemon, 200

    @marshal_with(pokemonFields)
    def patch(self, id):
        args = user_args.parse_args()
        pokemon = PokemonModel.query.filter_by(id=id).first()
        if not pokemon:
            abort(404, "Pokemon not found")

        pokemon.name = args['name']
        pokemon.edible = args['edible']
        pokemon.description = args['description']
        db.session.commit()

        return pokemon, 200

    @marshal_with(pokemonFields)
    def delete(self, id):
        pokemon = PokemonModel.query.filter_by(id=id).first()
        if not pokemon:
            abort(404, "Pokemon not found")

        db.session.delete(pokemon)
        db.session.commit()

        return pokemon, 204


api.add_resource(Pokemons, '/api/pokemons/')
api.add_resource(Pokemon, '/api/pokemon/<int:id>')

@app.route('/')
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)