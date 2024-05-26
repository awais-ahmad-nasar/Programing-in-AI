from flask import Flask,jsonify,request


app=Flask(__name__)
dlist=[]
@app.route('/get_all_data',methods=['GET'])
def get_all_data():
    return jsonify(dlist)

@app.route('/post_data',methods=['POST'])
def post_data():
    data=request.form
    id=data['id']
    name=data['name']
    sem=data['semester']
    l={'id':id,'name':name,'semester':sem}
    dlist.append(l)
    return 'Data Saved',200


if __name__=="__main__":
    print('Start')
    app.run(port=8050,host="0.0.0.0")
