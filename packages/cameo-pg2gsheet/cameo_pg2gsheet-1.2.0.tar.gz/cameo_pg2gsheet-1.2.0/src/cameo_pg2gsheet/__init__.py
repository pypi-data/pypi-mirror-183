import os
import pathlib

import gspread
import psycopg2
import pandas as pd
from dotenv import load_dotenv, find_dotenv


def connect_to_pg():
	if not os.getenv('DATABASE_PASSWORD'):
		dotenv_path = f'{pathlib.Path().resolve()}/.env'
		load_dotenv(find_dotenv(dotenv_path))

	connection = psycopg2.connect(
		database=os.getenv('DATABASE_NAME'),
		user=os.getenv('DATABASE_USERNAME'),
		password=os.getenv('DATABASE_PASSWORD'),
		host=os.getenv('DATABASE_IP'),
		port=os.getenv('DATABASE_PORT')
	)

	return connection


def export_single_table_to_csv(csv_file_path, table_name, rename_columns=None):
	connection = connect_to_pg()
	df = pd.read_sql_query(f'SELECT * FROM {table_name}', connection)

	if rename_columns is not None:
		df = df.rename(columns=rename_columns)

	df.to_csv(csv_file_path, index=False)

	connection.close()


def export_csv_by_sql_command(csv_file_path, sql_command, rename_columns=None):
	connection = connect_to_pg()
	df = pd.read_sql_query(sql_command, connection)

	if rename_columns is not None:
		df = df.rename(columns=rename_columns)

	df.to_csv(csv_file_path, index=False)

	connection.close()


def import_csv_to_gsheet(
	google_api_credentials_file_path,
    gsheet_id, worksheet_name, csv_file_path,
):
    gc = gspread.service_account(filename=google_api_credentials_file_path)
    sh = gc.open_by_key(gsheet_id)

    try:
        worksheet = sh.add_worksheet(
            title=worksheet_name, rows='1', cols='10', index='0'
        )
    except Exception:
        worksheet = sh.worksheet(worksheet_name)
        sh.del_worksheet(worksheet)
        worksheet = sh.add_worksheet(
            title=worksheet_name, rows='1', cols='10', index='0'
        )

    df = pd.read_csv(csv_file_path)
    worksheet.update(
        [df.columns.values.tolist()] +
        df.values.tolist(),
    )
