import json
import os

class Config:
	"""Класс с константами"""
	def __init__(self):
		self.json_file_name = 'db.json'

		self.payload = {
		'phone': '89872745052',
		'body': 'Соболев Артем, телефон: +7(925)537-39-10',
		'typeMsg': 'text',
		'title': 'Тестовое задание WhatCRM'
		}

		self.headers = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
		self.base_url = 'https://dev.whatsapp.sipteco.ru/v3/'
		self.instance = self.get_instance() if os.path.exists(self.json_file_name) else ''
		self.token = self.get_token() if os.path.exists(self.json_file_name) else ''
		self.params = {'full': '1'}
		self.QR_code = ''
	


	def get_instance(self):
		with open(self.json_file_name, 'r') as f:
			data = f.read()
			return json.loads(f).get('id') if data else ''

	def get_token(self):
		with open(self.json_file_name, 'r') as f:
			data = f.read()
			return json.loads(data).get('token') if data else ''

	def save_chat_info(self, json: str):
		self.instance = json.get("id")
		self.token = json.get('token')
		with open(self.json_file_name, 'w') as f:
			f.write(json)

	def save_qr_response(self, qr_code):
		self.QR_code = qr_code


