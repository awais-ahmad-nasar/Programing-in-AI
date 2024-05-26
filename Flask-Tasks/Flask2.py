'''
1) Write a function of POST API to insert data in CSV file
2) Write a function of GET API to get data from CSV file
'''


from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
csv_file_path = '../Task6.csv'


# Endpoint for reading data from the CSV file
@app.route('/read_csv', methods=['GET'])
def read_csv():
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Convert DataFrame to JSON and return
        return jsonify(df.to_dict(orient='records'))
    except FileNotFoundError:
        return jsonify({'error': 'CSV file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint for writing data to the CSV file
@app.route('/write_csv', methods=['GET', 'POST'])
def write_csv():
    try:
        if request.method == 'POST':
            # If it's a POST request, read CSV and append new data

            try:
                df = pd.read_csv(csv_file_path)
            except FileNotFoundError:
                df = pd.DataFrame()

            # Get user input
            reg_no=request.form.get('std_reg')
            name = request.form.get('name')
            course=request.form.get('course')
            cgpa=request.form.get('cgpa')
            age = request.form.get('age')
            email = request.form.get('email')


            if not all([reg_no,name,course,cgpa, age, email]):
                return jsonify({'error': 'Please provide all required fields (name, age, email)'}), 400

            new_data = pd.DataFrame([{'std_reg':reg_no,'name': name,'course':course,'cgpa':cgpa, 'age': age, 'email': email}])

            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(csv_file_path, index=False)

            return jsonify({'message': 'Data written to CSV file successfully'})
        else:
            # If it's a GET request, show a form to enter data
            return """
            <form method="post">
                <label for="std_reg">Reg Number:</label><br>
                <input type="int" name="std_reg" required><br>
                
                <label for="name">Name:</label><br>
                <input type="text" name="name" required><br>
                
                <label for="course">Course:</label><br>
                <input type="text" name="course" required><br>
                
                <label for="cgpa">CGPA:</label><br>
                <input type="float" name="cgpa" required><br>
                
                <label for="age">Age:</label><br>
                <input type="int" name="age" required><br>
                
                <label for="email">Email:</label><br>
                <input type="email" name="email" required><br><br>
                
                <input type="submit" value="Submit">
                
            </form>
            """

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=8050, host="0.0.0.0")