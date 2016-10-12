from flask import Flask
app = Flask('HelloWorldV1')

# Warm Up exercise
# Write a hello world web application that just renders the text "Hello, world!" inside of an HTML tag at the root URL: /.

@app.route('/')
def hello():
    return '<h1>Hello, world!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
