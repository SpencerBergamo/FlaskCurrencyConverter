# Author: Spencer Bergamo

# Setup Instructions:
# python3 -m venv venv
# source venv/bin/activate
# pip3 isntall requests
# To RUN : python3 currency.py

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        # from_currency = str(request.form['from_currency']).upper()
        to_currency = str(request.form['to_currency']).upper()
        amount = float(request.form['amount'])

        response = requests.get(f'https://api.exchangerate.host/convert?amount={amount}&from={from_currency}&to={to_currency}')
        data = response.json()

        rate = data['result']

        return f"""
        <html>
            <head>
                <title>Currency Converter</title>
            </head>
            <body>
                <h1>Conversion Result</h1>
                <p>{amount} {from_currency} = {rate} {to_currency}</p>
            </body>
        </html>
            """
    
    return """
    <html>
        <title>Currency Converter</title>
        <head>
            <h1>Currency Converter</h1>
        </head>
        <body>
            <h1>Convert Currency</h1>
            <form method="POST">
                <label for="amount">Amount:</label>
                <input type="text" id="amount" name="amount"><br><br>
                <label for="from_currency">From Currency:</label>
                <input type="text" id="from_currency" name="from_currency" required><br><br>
                <label for="to_currency">To Currency:</label>
                <input type="text" id="to_currency" name="to_currency" required><br><br>
                <input type="submit" value="Convert">
            </form>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# from_currency = str(input("From Currency: ")).upper()

# to_currency = str(input("To Currency: ")).upper()

# amount = float(input("Amount: "))

# url = f"https://api.exchangerate.host/convert?amount={amount}&from={from_currency}&to={to_currency}"
# response = requests.get(url)
# data = response.json()
# # print(response.status_code)
# # print(data)

# rate = data['result']
# print(f"{amount} {from_currency} = {rate} {to_currency}")
