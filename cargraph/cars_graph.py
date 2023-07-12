from flask import Flask, render_template, request

app = Flask(__name__)

# Car dictionary with car names 
car_images = {
    'Car1': 'i1.jpg',
    'Car2': 'i2.jpg',
    'Car3': 'i3.jpg'
}

@app.route('/')
def index():
    car_list = list(car_images.keys())
    return render_template('index.html', car_list=car_list)

@app.route('/display', methods=['POST'])
def display():
    selected_car = request.form.get('car')
    image_url = car_images.get(selected_car, 'i4.jpg')
    return render_template('display.html', image_url=image_url)

if __name__ == '__main__':
    app.debug = True
    app.run()
