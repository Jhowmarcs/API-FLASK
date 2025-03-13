from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


import mysql.connector

# Conexão
db = mysql.connector.connect(
    host="mysql-container",  
    user="root",             
    password="1234", 
    database="tfpy"  )




@app.route('/alunos', methods=['GET'])
def get_alunos():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    
    #  JSON
    alunos_list = []
    for aluno in alunos:
        aluno_dict = {
            "id": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2]
        }
        alunos_list.append(aluno_dict)

    return jsonify(alunos_list)

if __name__ == '__main__':
    app.run(debug=True)
