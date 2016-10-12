from flask import Flask, render_template
app = Flask("HelloWorldV2")

# Warm Up exercise
# Same as 1, but use a template file in the templates folder with the render_template instead.

@app.route("/")
def hello():
    return render_template(
        "hello_world.html",
        title = "Hello, World!"
    )

if __name__ == '__main__':
    app.run(debug=True)
