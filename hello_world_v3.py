from flask import Flask, render_template
app = Flask("HelloWorldV2")

# Warm Up exercise
# Same as 2, but use a layout template called layout.html, and have the index.html extend layout.html. layout.html should contain the standard elements: html, head, title, and body.

@app.route("/")
def hello():
    return render_template(
        "index.html",
        title = "Hello, World!"
    )

if __name__ == '__main__':
    app.run(debug=True)
