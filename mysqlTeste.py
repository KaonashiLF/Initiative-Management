import mysql.connector
import pandas as pd



conn = mysql.connector.connect(user='root', password='Devlkbd.2021', host='127.0.0.1',database='thotwh')

csr = conn.cursor()



df = pd.read_sql(sql='SELECT * FROM users', con=conn)

