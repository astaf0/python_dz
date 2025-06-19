from flask import Flask, render_template

app = Flask(__name__)

purchases_list = [
    {'name': 'апельсин', 'cost': 200, 'date': '2025-05-01'},
    {'name': 'термос', 'cost': 2000, 'date': '2025-06-02'},
    {'name': 'плед', 'cost': 1500, 'date': '2025-07-03'},
]

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/products')
def products_page():
    return render_template('products.html', purchases=purchases_list)

@app.route('/products/<int:index>')
def details(index):
    return render_template('products_details.html', product=purchases_list[index])

if __name__ == "__main__":
    app.run(debug=True)