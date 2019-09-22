from flask import Flask
from flask import Markup
import requests
import json
app = Flask(__name__)


@app.route('/pokemon/<query>')
def pokemon_lookup(query):

    url = "https://pokeapi.co/api/v2/pokemon/" + query
    r = requests.get(url)

    try: check = r.json()
    except ValueError: return(Markup("""<font size=\"20\"><b>That pokemon
                                        does not exist!<b></font>"""))

    pokemon_dict = json.loads(r.text)

    if(query.isdigit()):
        response = "The pokemon with id " + query + " is " + pokemon_dict["name"]
        response_format = Markup("<font size=\"20\"><b>" + response + "<b></font>")
        return response_format

    else:
        response = query + " has id " + str(pokemon_dict["id"])
        response_format = Markup("<font size=\"20\"><b>" + response + "<b></font>")
        return response_format
