import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
import mysql.connector
import speech_recognition as sr
import re
from datetime import datetime

def Portero_verif(text, e_s):
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ui3r4',
            database='porterobd',
        )
        cursor = conexao.cursor()
        texto = re.sub(r'\s+', '', text.strip().upper())
        print(f"Placa normalizada: {texto}")

        query = "SELECT * FROM veiculo WHERE Placa = %s"
        cursor.execute(query, (texto,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"Placa encontrada: {resultado}")
            if e_s == 2:
                from Saida import Portero_speak_saida
                Portero_speak_saida(texto)
            elif e_s == 1:
                from Entrada import Portero_speak_entrada
                Portero_speak_entrada(texto)
            else:
                print("Erro: Tipo de verificação inválido.")
                return False
            return True
        else:
            print(f"Nenhuma placa encontrada: {texto}.")
            return False

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou executar o comando SQL: {erro}")
        return False

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
        print("Conexão com o banco de dados encerrada.")

# -------------------------------
# Função de Entrada
# -------------------------------
def Portero_entrada(placa, nova_km):
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ui3r4',
            database='porterobd',
        )
        cursor = conexao.cursor()

        # Obter ID do veículo
        cursor.execute("SELECT idveiculo FROM veiculo WHERE Placa = %s", (placa,))
        veiculo = cursor.fetchone()

        if not veiculo:
            print(f"Erro: Placa '{placa}' não encontrada.")
            return False

        id_veiculo = veiculo[0]

        # Obter motorista e ID do último registro de saída
        cursor.execute("SELECT idUsuario FROM registro_saida WHERE idVeiculo = %s ORDER BY idRegistroSaida DESC LIMIT 1", (id_veiculo,))
        mot_result = cursor.fetchone()

        cursor.execute("SELECT idRegistroSaida FROM registro_saida WHERE idVeiculo = %s ORDER BY idRegistroSaida DESC LIMIT 1", (id_veiculo,))
        saida_result = cursor.fetchone()

        if not mot_result or not saida_result:
            print("Erro ao buscar motorista ou registro de saída.")
            return False

        id_usuario = mot_result[0]
        id_saida = saida_result[0]

        # Atualizar KM
        cursor.execute("UPDATE veiculo SET KMveiculo = %s WHERE idveiculo = %s", (nova_km, id_veiculo))

        # Inserir entrada
        hora_chegada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO registro_entrada (idVeiculo, idUsuario, idRegistroSaida, KMEntrada, HoraEntrada) VALUES (%s, %s, %s, %s, %s)",
            (id_veiculo, id_usuario, id_saida, nova_km, hora_chegada)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Entrada registrada com sucesso para '{placa}'.")
            return True
        else:
            print("Erro ao registrar entrada.")
            return False

    except mysql.connector.Error as erro:
        print(f"Erro SQL: {erro}")
        return False

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
        print("Conexão com o banco de dados encerrada.")

# -------------------------------
# Função de Saída
# -------------------------------
def Portero_saida(placa, cod_mot, det_mot):
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ui3r4',
            database='porterobd',
        )
        cursor = conexao.cursor()

        cursor.execute("SELECT idveiculo FROM veiculo WHERE Placa = %s", (placa,))
        veiculo = cursor.fetchone()

        if not veiculo:
            print(f"Erro: Placa '{placa}' não encontrada.")
            return False

        id_veiculo = veiculo[0]
        id_usuario = cod_mot  # Usa diretamente o código informado

        # Obter KM atual
        cursor.execute("SELECT KMveiculo FROM veiculo WHERE idveiculo = %s", (id_veiculo,))
        km_result = cursor.fetchone()

        if not km_result:
            print("Erro: Não foi possível obter a quilometragem.")
            return False

        km_saida = km_result[0]
        hora_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registrar saída
        cursor.execute(
            "INSERT INTO registro_saida (idVeiculo, idUsuario, KMSaida, HoraSaida, Destino) VALUES (%s, %s, %s, %s, %s)",
            (id_veiculo, id_usuario, km_saida, hora_saida, det_mot)
        )
        conexao.commit()
        reg_saida = cursor.lastrowid

        if cursor.rowcount > 0:
            print(f"Saída registrada para '{placa}'.")
            # Cria entrada básica vinculada
            cursor.execute(
                "INSERT INTO registro_entrada (idVeiculo, idUsuario, idRegistroSaida) VALUES (%s, %s, %s)",
                (id_veiculo, id_usuario, reg_saida)
            )
            conexao.commit()
            return True
        else:
            print("Erro ao registrar saída.")
            return False

    except mysql.connector.Error as erro:
        print(f"Erro SQL: {erro}")
        return False

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
        print("Conexão com o banco de dados encerrada.")
