from flask import Flask, render_template, request
from amazon_scarper import amazon_input
from flipkart_scraper import flipkart_input





app = Flask(__name__)



@app.route('/')
def home():

    return render_template('index.html')

@app.route('/navigate')
def navigate():

    return render_template('github_navigate.html')


@app.route('/compare', methods=['POST', 'GET'])
def compare():
    amazon_result1 = amazon_input(request.form['amazon'])
    flipkart_result2 = flipkart_input(request.form['amazon'])
    flipkart_result1 = flipkart_input(request.form['flipkart'])
    amazon_result2 = amazon_input(request.form['flipkart'])


    return render_template('comparison.html', am_result=amazon_result1, fp_result=flipkart_result1,am_result1=amazon_result2, fp_result1=flipkart_result2)


if __name__ == '__main__':
    app.run(debug=True)


