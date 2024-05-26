# import csv
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# file_path =r"E:\MY Documents\task7_PAI.csv"
#
#
# def get():
#     dlist = []
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         next(reader, None)  # Skip header
#         for row in reader:
#             if len(row) >= 4:
#                 d = {'id': row[0], 'name': row[1], 'course': row[2], 'cgpa': row[3]}
#                 dlist.append(d)
#             else:
#                 print(f"Skipping incomplete row: {row}")
#
#     return {'data': dlist}
#
# def post(data):
#     slist = [data.get('id'), data.get('name'), data.get('course'), data.get('cgpa')]
#     with open(file_path, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(slist)
#
# def put(data):
#     update_id = data.get('id')
#     dlist = []
#     updated = False
#
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#
#         for row in rows:
#             if row and row[0] == update_id:
#                 row[1] = data.get('name', row[1])
#                 row[2] = data.get('course', row[2])
#                 row[3] = data.get('cgpa', row[3])
#                 updated = True
#             d = {'id': row[0], 'name': row[1], 'course': row[2], 'cgpa': row[3]}
#             dlist.append(d)
#
#     if not updated:
#         print(f"ID {update_id} not found for update.")
#
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows([['id', 'name', 'course', 'cgpa']] + [[d['id'], d['name'], d['course'], d['cgpa']] for d in dlist])
# def delete(id):
#     dlist = []
#     deleted = False
#
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#
#         for row in rows:
#             if row and row[0] == id:
#                 deleted = True
#             else:
#                 # Check the length of the row before accessing its elements
#                 if len(row) >= 4:
#                     d = {'id': row[0], 'name': row[1], 'course': row[2], 'cgpa': row[3]}
#                     dlist.append(d)
#                 else:
#                     print(f"Skipping incomplete row: {row}")
#
#     if not deleted:
#         print(f"ID {id} not found for deletion.")
#
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         # Writing the header
#         writer.writerow(['id', 'name', 'course', 'cgpa'])
#         # Writing the data
#         writer.writerows([[d['id'], d['name'], d['course'], d['cgpa']] for d in dlist])
#
# @app.route('/api/data/<id>', methods=['PUT'])
# def put_api_data(id):
#     data = {
#         "name": "Updated Name",
#         "course": "Updated Course",
#         "cgpa": "4.0"
#     }
#     data['id'] = id
#     put(data)
#     return jsonify({"message": f"Data with ID {id} updated successfully"})
#
# @app.route('/api/data/<id>', methods=['DELETE'])
# def delete_api_data(id):
#     delete(id)
#     return jsonify({"message": f"Data with ID {id} deleted successfully"})
#
#
#
# @app.route('/api/data', methods=['GET'])
# def get_api_data():
#     data = get()
#     return jsonify(data)
#
# @app.route('/api/data', methods=['POST'])
# def post_api_data():
#     data = {
#         "id": "101",
#         "name": "John Doe",
#         "course": "Computer Science",
#         "cgpa": "3.8"
#     }
#     post(data)
#     return jsonify({"message": "Data posted successfully"})
#
# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=5000)
#
#



######################################################################################
######################################################################################
######################################################################################
#
# from flask import Flask, request, jsonify
# import csv
#
# app = Flask(__name__)
#
# file_path = "Task7_PAI_2.csv"
#
# def insert_data(data):
#     with open(file_path, 'a', newline='') as csvfile:
#         fieldnames = ['ID', 'NAME', 'SEMESTER']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         if csvfile.tell() == 0:
#             writer.writeheader()
#
#         writer.writerow(data)
#
# def get_data():
#     result = []
#     with open(file_path, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             result.append(row)
#     return result
# def post(data):
#     slist = [data.get('id'), data.get('name'), data.get('course'), data.get('cgpa')]
#     with open(file_path, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(slist)
#
# def put(data):
#     update_id = data.get('id')
#     dlist = []
#     updated = False
#
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#
#         for row in rows:
#             if row and row[0] == update_id:
#                 row[1] = data.get('name', row[1])
#                 row[2] = data.get('course', row[2])
#                 row[3] = data.get('cgpa', row[3])
#                 updated = True
#             d = {'id': row[0], 'name': row[1], 'course': row[2], 'cgpa': row[3]}
#             dlist.append(d)
#
#     if not updated:
#         print(f"ID {update_id} not found for update.")
#
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows([['id', 'name', 'course', 'cgpa']] + [[d['id'], d['name'], d['course'], d['cgpa']] for d in dlist])
# def delete(id):
#     dlist = []
#     deleted = False
#
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#
#         for row in rows:
#             if row and row[0] == id:
#                 deleted = True
#             else:
#                 # Check the length of the row before accessing its elements
#                 if len(row) >= 4:
#                     d = {'id': row[0], 'name': row[1], 'course': row[2], 'cgpa': row[3]}
#                     dlist.append(d)
#                 else:
#                     print(f"Skipping incomplete row: {row}")
#
#     if not deleted:
#         print(f"ID {id} not found for deletion.")
#
#     with open(file_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         # Writing the header
#         writer.writerow(['id', 'name', 'course', 'cgpa'])
#         # Writing the data
#         writer.writerows([[d['id'], d['name'], d['course'], d['cgpa']] for d in dlist])
#
#
#
# @app.route('/insert', methods=['POST'])
# def insert():
#     data = request.get_json()
#     insert_data(data)
#     return jsonify({'message': 'Data inserted successfully'}), 201
#
#
# @app.route('/get', methods=['GET'])
# def get():
#     data = 'zain'
#     return jsonify(data), 200
#
#
# if __name__ == '__main__':
#     app.run(debug=False)






######################################################################################
######################################################################################
######################################################################################

from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

csv_file_path = '../Task7_PAI_2.csv'


def insert_data(data):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'NAME', 'SEMESTER']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(data)


def get_data():
    result = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row)
    return result


def update_data(data):
    rows = get_data()
    updated_data = [data if row['ID'] == data['ID'] else row for row in rows]

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'NAME', 'SEMESTER']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)


def delete_data(data_id):
    rows = get_data()
    updated_data = [row for row in rows if row['ID'] != data_id]

    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'NAME', 'SEMESTER']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)


@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    insert_data(data)
    return jsonify({'message': 'Data inserted successfully'}), 201


@app.route('/get', methods=['GET'])
def get():
    data = get_data()
    return jsonify(data), 200


@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    update_data(data)
    return jsonify({'message': 'Data updated successfully'}), 200


@app.route('/delete/<string:data_id>', methods=['DELETE'])
def delete(data_id):
    delete_data(data_id)
    return jsonify({'message': 'Data deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=False)
