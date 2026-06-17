
app = Flask(___name_)

@app.route('/')
def home():
    return "<h1>Welcome to my Python Web App!</h1><p>It works perfectly.</p>"


if __name__ == '__main__':
    app.run(debug=True)
