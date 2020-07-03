from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Alvaro',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'title': 'Blog Post 1',
		'date_posted': 'March 15 2019'
	},
	{
		'author': 'John Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'title': 'Blog Post 2',
		'date_posted': 'March 16 2019'
	}
]
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)