from flask import Flask, render_template, request
from services import pwned_api_check

app = Flask(__name__)

@app.route("/")
def index():
    """
    Display the home page with the password input form.
    """
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_password():
    """
    Process the password entered by the user and display the result.
    """
    password = request.form.get("password")
    if not password:
        return render_template("result.html", message="Please enter a password.")

    try:
        count = pwned_api_check(password)
        if count:
            message = f"Oops! The password you entered has been found {count} times in data breaches. Consider changing it!"
        else:
            message = "Great! Your password was not found in any known data breaches. Keep it safe!"
    except RuntimeError as e:
        message = f"An error occurred: {e}"

    return render_template("result.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
