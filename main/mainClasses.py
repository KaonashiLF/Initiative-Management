import datetime as dt
import pandas as pd
import pyautogui
import mysql.connector

#minhas variáveis
hrNow = dt.datetime.now().hour
minNow = dt.datetime.now().minute
agora = str(hrNow)+":"+str(minNow)


#minha classe atividade




class admin():
    database = "I:\Documentos\Programacao\Repos\GitHub\Initiative-Management\main\db_user.xlsx"

    def __init__(self) -> None:
        pass

    def cadastrarUser(self, name, lastname, email, username):
        self.name = str(name)
        self.lname = str(lastname)
        self.email = str(email)
        self.username = str(username)
        database = admin().database

        conn = mysql.connector.connect(user='root', password='Devlkbd.2021', host='127.0.0.1',database='users')

        try:
            userDB = pd.read_excel(database,
                sheet_name="tbl_Users",
                index_col=None
                )

            newUser = pd.DataFrame(
                [[name,lastname,email,username]],
                columns=["Name","LastName","Email","username"],
                index=None
                )

            newUser.head()

            newdf = pd.concat([userDB,newUser],ignore_index=False)
            newdf.head()

            newdf.to_excel(database,sheet_name="tbl_Users",index=0)

            print(f"Usuário {name} cadastrado com sucesso. \n\nNome: {name}\nSobrenome: {lastname}\nE-mail: {email}\nUsername: {username}\n")
        except Exception as e:
            print("Erro apresentado: "+e)
    def delUser(self, username):
        #Função para deletar um user da base
        self.username = username
        database = admin().database

        df = pd.read_excel(database,sheet_name="tbl_Users", index_col=None)

        if type(username) is list:
            try:
                for users in username:
                    if users in list(df["username"]):
                        newdf = df[df["username"] != users]
                        newdf.to_excel(database,sheet_name="tbl_Users",index=0)
                        print(f"O usuário {users} foi removido com sucesso!")
                    else:
                        print(f"O usuário {users} não está cadastrado.")

            except Exception as e:
                print(e)


        elif type(username) is str:
            #if username in df["username"]:
                try:
                    newdf = df[df["username"] != username]
                    print(f"O usuário {username} foi removido com sucesso!")
                    newdf.to_excel(database,sheet_name="tbl_Users",index=0)
                except Exception as e:
                    print(e)
            #else:
                #print(f"O usuário {username} não está cadastrado")
        else:
            print("Tipo de dado não aceito para Username")
        



    def consultarUser(self):
        #self.name = str(name)
        #self.lname = str(lastname)
        #self.email = str(email)
        #self.username = str(username)

        database = admin().database
        y = pyautogui.prompt(text="Insira o nome do usuário da consulta",title="Consulta de usuário")
        y = str(y)
        df = pd.read_excel(database,sheet_name="tbl_Users",index_col=None)

        if y in list(df["username"]):
            df.head()
        else:
            print(f'O usuário {y} não foi localizado.')

        


a = admin()
#a.cadastrarUser("Lucas","Silva","lucasfrancs.contato@gmail.com", "Kaonashi")

a.delUser("Kaonashi")