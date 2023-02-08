#!/usr/bin/python3
from asyncio import timeout
import requests
from requests.exceptions import Timeout
import json
import pyodbc
import time
import logging


# logging configuration
logging.basicConfig(filename='logs/application.log',
                    format='%(asctime)s\t%(levelname)s\t%(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    level=logging.INFO)

def get_token(sms_server,sms_username,sms_password):
    while True:
        url = "http://" + sms_server + "/api/token/"
        headers_token = {'content-type': "application/json"}
        payload_json_token = {"username": sms_username, "password": sms_password}
        try:
            response_token = requests.post(url, headers=headers_token, json=payload_json_token, timeout=(2,5))
            json_response_token = json.loads(response_token.text)
            token = "Bearer " + json_response_token["access"]
            logging.info("Renew Token")
            return token
        except timeout:
            logging.error("The request timed out. request is : {}".format(url))

def send_sms(sms_server,token,dest_number,text):
    url = "http://" + sms_server + "/api/message/send/single/"
    headers_send = {'content-type': "application/json", 'Authorization': token}
    #sar shomare default
    #payload_json_send = 
    # {'sender': 'Wek9B9JZFqp2MdwgVE8g6Z', 'recipient': dest_number, 'message': text}
    payload_json_send = {'sender': '74kAiay7anTRt33NECebkS', 'recipient': dest_number, 'message': text}
    try:
        response_send = requests.post(url, headers=headers_send, json=payload_json_send, timeout=(2,5))
        json_response_send = json.loads(response_send.text)
        return json_response_send,response_send.status_code

    except timeout:
        logging.error("The request timed out. request is : {}".format(url))

def main(): 
    db_server = 'tcp:172.16.48.206'
    sms_server = '172.18.122.112'
    db_database = 'magfadb'
    db_username = 'qmMagfa'
    db_password = 'password'
    sms_user = "n_mirhoseini@rasana.ir"
    sms_pass = "password"

    #select_query = "SELECT top 1000 * from outbox where processed=0 and CONVERT(TIME, GETDATE()) >= not_before and CONVERT(TIME, GETDATE()) <=not_after and priority=255 and src_number=300085264;"
    #select_query = "SELECT top 500 id,text,dest_number from outbox where processed=0 and CONVERT(TIME, GETDATE()) >= not_before and CONVERT(TIME, GETDATE()) <=not_after and priority=255 and src_number='300085264' order by id desc;"

    select_query = "SELECT top 500 id,text,dest_number from outbox where processed=0 and CONVERT(TIME, GETDATE()) >= not_before and CONVERT(TIME, GETDATE()) <=not_after order by id desc;"
    token = get_token(sms_server,sms_user,sms_pass)
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_server + ';DATABASE=' + db_database + ';UID=' + db_username + ';PWD=' + db_password)
        cursor = cnxn.cursor()
        logging.info("Successfuly Connect to Database")
    except pyodbc.Error as ex:
        logging.error(ex)
        cursor.close()
        exit(25)

    while True:
        try:
            cursor.execute(select_query)
            rows = cursor.fetchall()
            rows_count = len(rows)
        except pyodbc.Error as ex:
            logging.error(ex)
            cursor.close()
            exit(25)
        

        if int(rows_count) == 0:
            pass
        else:
            for row in rows:
                sms_result = send_sms(sms_server,token,row.dest_number[1:],row.text)
                update_guery_seccess = "UPDATE outbox SET processed = 1, processed_date = GETDATE(), error_core = " + str(sms_result[1]) + ",returned_id = '" + str(sms_result[0]["reference_id"]) + "' where id = " + str(row.id)
                update_query_fail = "UPDATE outbox SET processed_date = GETDATE(), error_core = "+ str(sms_result[1]) +" where id=" + str(row.id)
                update_query_fail_bad_number = "UPDATE outbox SET processed = 1, processed_date = GETDATE(), error_core = 400, returned_id = 'Bad-Number' where id=" + str(row.id)

                if int(sms_result[1]) == 401:
                    logging.error("Send SMS error 401 Detail Is : {}".format(sms_result[0]))
                    logging.info(sms_result[0])
                    token = get_token(sms_server,sms_user,sms_pass)
                    break

                elif int(sms_result[1]) == 200:
                    try:
                        cursor.execute(update_guery_seccess)
                        cnxn.commit()
                        logging.info("Send SMS From ID : {} to : {} with returned_id : {}".format(row.id, row.dest_number, sms_result[0]["reference_id"]))
                    except pyodbc.Error as ex:
                        logging.error("Send SMS From ID : {} to : {} with returned_id : {}".format(row.id, row.dest_number, sms_result[0]["errors"]))
                        logging.error(ex)
                        cursor.close()
                        exit(25)
                else:
                    if len(row.dest_number[1:]) != 12:
                        try:
                            cursor.execute(update_query_fail_bad_number)
                            cnxn.commit()
                            logging.warn("Send SMS From ID : {} to : {} Failed Because Number Is Not Currect".format(row.id, row.dest_number))
                        except pyodbc.Error as ex:
                            logging.error(ex)
                            cursor.close()
                            exit(25)
                    else:
                        try:
                            cursor.execute(update_query_fail)
                            cnxn.commit()
                            logging.error("Send SMS error Detail Is : {}".format(sms_result[0]))
                        except pyodbc.Error as ex:
                            logging.error(ex)
                            cursor.close()
                            exit(25)

            time.sleep(5)

if __name__ == "__main__":
    main()
