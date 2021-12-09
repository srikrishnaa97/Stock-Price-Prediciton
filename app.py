from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

stocks = []
with open('stocks.txt','r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        stocks.append(line.strip())

#@app.route('/')
#def index():
#    return render_template('index.html',stocks=stocks,curr_stock='')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':

        future_data = []
        train_data = [] 
        test_data = []
        together_data = []
        
        try:
            curr_stock = request.form['stock'].strip()
            if not curr_stock in stocks:
                raise('Error!')
            
            future_data = pd.read_csv('plot data/'+curr_stock+'_future.csv',header=None).astype(float).fillna(-1).values.tolist()
            train_data = pd.read_csv('plot data/'+curr_stock+'_train.csv',header=None).astype(float).fillna(-1).values.tolist()
            test_data = pd.read_csv('plot data/'+curr_stock+'_test.csv',header=None).astype(float).fillna(-1).values.tolist()
            together_data = pd.read_csv('plot data/'+curr_stock+'_together.csv',header=None).astype(float).fillna(-1).values.tolist()


        except:
            curr_stock = 'Error!'
        finally:
            return render_template('index.html',stocks=stocks,curr_stock=curr_stock,
                                    future_data=future_data,
                                    train_data=train_data,
                                    test_data=test_data,
                                    together_data=together_data)

    else:
        return render_template('index.html',stocks=stocks,curr_stock='',
                                    future_data=[],
                                    train_data=[],
                                    test_data=[],
                                    together_data=[])


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)