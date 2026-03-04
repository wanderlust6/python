from flask import Flask, render_template, request

app = Flask(__name__)

# 初始化计数器
counter = 0


@app.route("/", methods=["GET", "POST"])
def home():
    global counter
    if request.method == "POST":
        counter += 1
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>计数器</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                font-size: 3em;
            }}
            p {{
                font-size: 1.5em;
            }}
            button {{
                font-size: 1.2em;
                padding: 10px 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>计数器</h1>
        <p>当前计数：{counter}</p>
        <form method="POST">
            <button type="submit">点击我</button>
        </form>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
