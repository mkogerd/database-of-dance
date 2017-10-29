from flask import Flask, render_template
app = Flask(__name__)
import pandas as pd

#df = pd.read_csv('test.csv')
df = pd.read_csv('moveList.csv')
genres = df.Genre.unique()

@app.route("/")
def template_test():
    return render_template('index.html', df=df, genres=genres)

@app.route('/<genre>')
def some_place_page(genre):
	return render_template('index.html', df=(df[df['Genre'] == genre]), genres=genres)
    

if __name__ == '__main__':
    app.run(debug=True)