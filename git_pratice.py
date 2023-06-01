from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="students",
    user="postgres",
    password="usman@123"
)


@app.route('/retrive', methods=['GET'])
def get_data():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)


@app.route('/insert', methods=['POST'])
def inser_data():
    # Access the JSON payload from the request
    data = request.get_json()
    #prepare sample json data with the data mobile=vivo model=z1pro storage=10gb price=10000
    cursor = connection.cursor()
    cursor.execute("INSERT INTO student (student_name, student_branch,student_email) VALUES (%s, %s, %s)",
                   (data['student_name'], data['student_branch'], data['student_email']))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Data inserted successfully"})



    '''# Extract the necessary data from the payload
    mobile = data.get('mobile')
    model = data.get('model')
    storage = data.get('storage')
    price = data.get('price')

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO mobile (mobile, model,storage,price) VALUES (%s, %s, %s, %s)",
        (mobile,model,storage,price)
    )
    connection.commit()
    cursor.close()

    return jsonify({'message': 'Record created successfully'})'''



'''@app.route('/create', methods=['POST'])
def create_data(data):
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mobile (mobile, model,storage,price) VALUES (%s, %s,%s,%s)", (data['mobile'], data['model'], data['storage'], data['price']))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Data created successfully"})'''


@app.route('/update', methods=['PUT'])
def update_user(mobile):
    try:

        conn = psycopg2.connect(host= 'localhost', port= 5432, dbname = 'mobile', user='postgres', password = 'usman@123')
        cursor = conn.cursor()

        new_model = request.json.get('model')
        new_storage = request.json.get('storage')

        update_query = "UPDATE moblie SET model = %s, storage = %s WHERE mobile = %s"
        cursor.execute(update_query, (new_model, new_storage, mobile))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({'message': 'User updated successfully'})

    except (psycopg2.Error, Exception) as error:
        
        return jsonify({'error': str(error)}), 500


@app.route('/remove', methods=['DELETE'])
def delete_item():
    try:
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM mobile WHERE model = %s", (model,))

        connection.commit()

        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Item deleted successfully'})

    except Exception as e:

        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True,port = 3005)




'''import requests
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:usman@123@localhost/mobile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@cross_origin()    
@app.route('/retrive', methods = ['GET'])
def getpets():
     all_pets = []
     pets = mobile.query.all()
     for pet in pets:
          results = {
                    "pet_id":pet.id,
                    "pet_name":pet.pet_name,
                    "pet_age":pet.pet_age,
                    "pet_type":pet.pet_type,
                    "pet_description":pet.pet_description, }
          all_pets.append(results)

     return jsonify(
            {
                "success": True,
                "pets": all_pets,
                "total_pets": len(pets),
            }
        )




if __name__ == '__main__':
  app.run(debug=True,port=5003)'''






import psycopg2 
import psycopg2.extras

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'usman@123'
port_id = 5432
conn = None
cur = None

def database():
    try:
        conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id)
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute('DROP TABLE IF EXISTS mobile')

        create_table_query = '''CREATE TABLE IF NOT EXISTS mobile 
            (
            MOBILE        varchar NOT NULL,
            MODEL         varchar    NOT NULL,
            STORAGE       varchar  NOT NULL,
            PRICE         int)'''
        cur.execute(create_table_query)
        insert_data = 'insert into mobile(MOBILE,MODEL,STORAGE,PRICE) values (%s,%s,%s,%s)'
        insert_values = [("iphone","14promax","256gb",100000),("mi","12","128gb",20000),("Realme","3pro","256gb",25000),("poco","x3pro","256gb",15000),("vivo","z1pro","64gb",12000)]
        for record in insert_values:
            #print(record)
            cur.execute(insert_data, record)

        update_data = ('update mobile set price = 300000 where mobile = %s ')
        update_phone = ('iphone',)
        cur.execute(update_data,update_phone)

        delete_data = ('delete from mobile where mobile = %s')
        delete_mobile = ('poco',)
        cur.execute(delete_data,delete_mobile)

        cur.execute('select * from  mobile')
        response = []
        for record in cur.fetchall():
            a = (record['mobile'],record['price'],record['storage'])
            data = {
                "mobile": record['mobile'],
                "price": record['price'],
                "storage":record['storage']
            }
            response.append(data)
        print(response)
        conn.commit()

    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
database()



from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mobile",
    user="postgres",
    password="usman@123"
)


@app.route('/retrive', methods=['GET'])
def get_data():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mobile")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/create/<string:data>', methods=['POST'])
def create_data(data):
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mobile (mobile, model,storage,price) VALUES (%s, %s,%s,%s)", (data['mobile'], data['model'], data['storage'], data['price']))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Data created successfully"})


@app.route('/update/<string:mobile>', methods=['PUT'])
def update_user(mobile):
    try:

        conn = psycopg2.connect(host= 'localhost', port= 5432, dbname = 'mobile', user='postgres', password = 'usman@123')
        cursor = conn.cursor()

        new_model = request.json.get('model')
        new_storage = request.json.get('storage')

        update_query = "UPDATE moblie SET model = %s, storage = %s WHERE mobile = %s"
        cursor.execute(update_query, (new_model, new_storage, mobile))
        conn.commit()

        cursor.close()
        conn.close()
        return jsonify({'message': 'User updated successfully'})

    except (psycopg2.Error, Exception) as error:
        
        return jsonify({'error': str(error)}), 500


@app.route('/remove/<int:modle>', methods=['DELETE'])
def delete_item(model):
    try:
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM mobile WHERE model = %s", (model,))

        connection.commit()

        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Item deleted successfully'})

    except Exception as e:

        return jsonify({'error': str(e)}), 500






if __name__ == '__main__':
    app.run(debug=True,port = 3005)






























'''from flask import Flask , request

app = Flask(__name__)

@app.route('/login' , method =['POST','GET'])
def login():
    if request.method =='Post':
        user = request.form['username']
        password = request.form['userpassword']
        if user == 'usman' and password == '12345':
            return "welcome usman"
        else:
            return "login failed"
    else:
        user = request.args.get['username']
        password = request.args.get['userpassword']
        if user == 'usman' and password == '12345':
            return "welcome usman"
        else:
            return "login failed"


if __name__ == 'main':
    app.run(debug=True,port=500)'''













# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/retrive', methods=['GET'])
# def get_method():
#     return 'This is a GET method'

# @app.route('/create', methods=['POST'])
# def post_method():
#     data = request.get_json()
#     return 'This is a POST method with data: {}'.format(data)

# @app.route('/update', methods=['PUT'])
# def put_method():
#     return 'This is a PUT method'

# @app.route('/remove', methods=['DELETE'])
# def delete_method():
#     return 'This is a DELETE method'

# if __name__ == '__main__':
#     app.run(port = 3003,debug = True)







# # from flask import Flask,jsonify
# # import psycopg2 
# # import psycopg2.extras


# # hostname = 'localhost'
# # database = 'mobile'
# # username = 'postgres'
# # pwd = 'usman@123'
# # port_id = 5432
# # conn = None
# # cur = None


# # from flask import Flask , request

# # app = Flask(__name__)

# # @app.route('/hey')
# # def hello():
# #     try:
# #         conn = psycopg2.connect(
# #                     host = hostname,
# #                     dbname = database,
# #                     user = username,
# #                     password = pwd,
# #                     port = port_id)
        
# #         cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# #         cur.execute('DROP TABLE IF EXISTS mobile')

# #         create_table_query = '''CREATE TABLE IF NOT EXISTS mobile 
# #             (
# #             MOBILE        varchar NOT NULL,
# #             MODEL         varchar    NOT NULL,
# #             STORAGE       varchar  NOT NULL,
# #             PRICE         int)'''
# #         cur.execute(create_table_query)
# #         insert_data = 'insert into mobile(MOBILE,MODEL,STORAGE,PRICE) values (%s,%s,%s,%s)'
# #         insert_values = [("iphone","14promax","256gb",100000),("mi","12","128gb",20000),("Realme","3pro","256gb",25000),("poco","x3pro","256gb",15000),("vivo","z1pro","64gb",12000)]
# #         for record in insert_values:
# #             #print(record)
# #             cur.execute(insert_data, record)

# #         update_data = ('update mobile set price = 300000 where mobile = %s ')
# #         update_phone = ('iphone',)
# #         cur.execute(update_data,update_phone)

# #         delete_data = ('delete from mobile where mobile = %s')
# #         delete_mobile = ('poco',)
# #         cur.execute(delete_data,delete_mobile)

# #         cur.execute('select * from  mobile')
# #         response = []
# #         for record in cur.fetchall():
# #             #a = (record['mobile'],record['price'],record['storage'])
# #             data = {
# #                 "mobile": record['mobile'],
# #                 "price": record['price'],
# #                 "storage":record['storage']
# #             }
# #             response.append(data)
# #         #print(response)
# #         conn.commit()
        
# #         return jsonify(response)
# #     except Exception as error:
# #         print(error)


# # if __name__ == '__main__':
# #     app.run(port=3001 , debug=True)




# # #app = Flask(__name__)


# # # @app.route('/')
    
# # # if __name__ == '__main__':
# # #     app.run(port = 3002,debug=True)



print("This is my first code in GitHUb ")
