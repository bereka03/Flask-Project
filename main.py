from website import create_app
from flask import Flask, render_template
import requests


app = create_app()

anime_name = "one_piece"
url = f"https://anime-facts-rest-api.herokuapp.com/api/v1/{anime_name}"
r = requests.get(url)
data = r.json()
facts = data['data']


@app.route('/anime_facts')
def anime_facts():
    return render_template('facts.html', info=facts)

if __name__ == '__main__':
    app.run(debug=True)
