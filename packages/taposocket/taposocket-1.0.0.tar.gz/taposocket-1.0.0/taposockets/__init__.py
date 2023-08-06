import hashlib
import json
import ast
import uuid
import json

from requests import Session, post
from base64 import b64encode, b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from taposockets.status_code import ERROR_CODES
from taposockets.cipher import TpLinkCipher

__version__ = "1.0.0"
__author__ = "Atul Singh"
__maintainer__ = __author__


class P100():
	def __init__ (self, ip_address, email, password):
		self.ip_address = ip_address
		self.terminal_UUID = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.session = None
		self.cookie_name = "TP_SESSIONID"
		self.error_codes = ERROR_CODES

		self.encrypt_credentials()
		self.generate_key_pair()


	def encrypt_credentials(self):
		self.encoded_password = b64encode(self.password.encode("UTF-8")).decode("UTF-8")
		self.encoded_email = self.sha_digest_username(self.email)
		self.encoded_email = b64encode(self.encoded_email.encode("utf-8")).decode("UTF-8")


	def generate_key_pair(self):
		keys = RSA.generate(1024)
		self.private_key = keys.exportKey("PEM")
		self.public_key = keys.publickey().exportKey("PEM")


	def decode_handshake_key(self, response_key):
		key = bytearray()
		iv = bytearray()

		encrypted_data: bytes = b64decode(response_key.encode("UTF-8"))
		private_key: bytes = self.private_key

		cipher = PKCS1_v1_5.new(RSA.importKey(private_key))
		do_final = cipher.decrypt(encrypted_data, None)
		if do_final is None:
			raise ValueError("Decryption failed!")

		for i in range(0, 16):
			key.insert(i, do_final[i])
		for i in range(0, 16):
			iv.insert(i, do_final[i + 16])

		return TpLinkCipher(key, iv)


	def sha_digest_username(self, data):
		return hashlib.sha1(data.encode("UTF-8")).digest().hex()


	def handshake(self):
		URL = f"http://{self.ip_address}/app"
		payload = {
			"method":"handshake",
			"params":{
				"key": self.public_key.decode("utf-8"),
				"requestTimeMils": 0
			}
		}
		# start new TCP session
		if self.session:
			self.session.close()
		self.session = Session()

		r = self.session.post(URL, json=payload, timeout=2)

		encryptedKey = r.json()["result"]["key"]
		self.tpLinkCipher = self.decode_handshake_key(encryptedKey)

		try:
			self.cookie = f"{self.cookie_name}={r.cookies[self.cookie_name]}"

		except:
			error_code = r.json()["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")

	
	def send_request(self, payload: dict, headers: dict={}, url: str=""):
		if not url:
			url = f"http://{self.ip_address}/app?token={self.token}"
		encrypted_payload = self.tpLinkCipher.encrypt(json.dumps(payload))
		secure_pass_through = {
			"method":"securePassthrough",
			"params":{
				"request": encrypted_payload
			}
		}
		r = self.session.post(url, json=secure_pass_through, headers=headers, timeout=2)
		return self.tpLinkCipher.decrypt(r.json()["result"]["response"])


	def login(self):
		URL = f"http://{self.ip_address}/app"
		payload = {
			"method":"login_device",
			"params":{
				"password": self.encoded_password,
				"username": self.encoded_email
			},
			"requestTimeMils": 0,
		}
		headers = {
			"Cookie": self.cookie
		}

		decrypted_response = self.send_request(payload, headers, URL)

		try:
			self.token = ast.literal_eval(decrypted_response)["result"]["token"]
		except:
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")


	def turn_on(self):
		payload = {
			"method": "set_device_info",
			"params":{
				"device_on": True
			},
			"requestTimeMils": 0,
			"terminalUUID": self.terminal_UUID
		}

		headers = {
			"Cookie": self.cookie
		}

		decrypted_response = self.send_request(payload, headers)

		if ast.literal_eval(decrypted_response)["error_code"] != 0:
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")


	def turn_off(self):
		payload = {
			"method": "set_device_info",
			"params":{
				"device_on": False
			},
			"requestTimeMils": 0,
			"terminalUUID": self.terminal_UUID
		}

		headers = {
			"Cookie": self.cookie
		}

		decrypted_response = self.send_request(payload, headers)

		if ast.literal_eval(decrypted_response)["error_code"] != 0:
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")


	def get_device_info(self):
		payload = {
			"method": "get_device_info",
			"requestTimeMils": 0,
		}

		headers = {
			"Cookie": self.cookie
		}

		return json.loads(self.send_request(payload, headers))


	def get_device_name(self):
		decrypted_response = self.get_device_info()

		if decrypted_response["error_code"] != 0:
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")
		else:
			encodedName = decrypted_response["result"]["nickname"]
			name = b64decode(encodedName)
			return name.decode("utf-8")


	def toggle_state(self):
		state = self.get_device_info()["result"]["device_on"]
		if state:
			self.turn_off()
		else:
			self.turn_on()


	def turn_on_with_delay(self, delay):
		payload = {
			"method": "add_countdown_rule",
			"params": {
				"delay": int(delay),
				"desired_states": {
					"on": True
				},
				"enable": True,
				"remain": int(delay)
			},
			"terminalUUID": self.terminal_UUID
		}

		headers = {
			"Cookie": self.cookie
		}

		decrypted_response = self.send_request(payload, headers)
		
		if ast.literal_eval(decrypted_response)["error_code"] != 0:
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")


	def turn_off_with_delay(self, delay):
		payload = {
			"method": "add_countdown_rule",
			"params": {
				"delay": int(delay),
				"desired_states": {
					"on": False
				},
				"enable": True,
				"remain": int(delay)
			},
			"terminalUUID": self.terminal_UUID
		}

		headers = {
			"Cookie": self.cookie
		}

		decrypted_response = self.send_request(payload, headers)
		
		if ast.literal_eval(decrypted_response)["error_code"] != 0:
			print(decrypted_response)
			error_code = ast.literal_eval(decrypted_response)["error_code"]
			error_message = self.error_codes[str(error_code)]
			raise Exception(f"Error Code: {error_code}, {error_message}")


# Old Functions to get device list from tplinkcloud
def get_token(email, password):
	URL = "https://eu-wap.tplinkcloud.com"
	payload = {
		"method": "login",
		"params": {
			"appType": "Tapo_Ios",
			"cloudUserName": email,
			"cloudPassword": password,
			"terminalUUID": "0A950402-7224-46EB-A450-7362CDB902A2"
		}
	}

	return post(URL, json=payload).json()['result']['token']


def get_device_list(email, password):
	URL = "https://eu-wap.tplinkcloud.com?token=" + get_token(email, password)
	payload = {
		"method": "getDeviceList",
	}

	return post(URL, json=payload).json()


class P115(P100):
	def get_energy_usage(self):
		URL = f"http://{self.ip_address}/app?token={self.token}"
		payload = {
			"method": "get_energy_usage",
			"requestTimeMils": 0,
		}
		headers = {
			"Cookie": self.cookie
		}
		encrypted_payload = self.tpLinkCipher.encrypt(json.dumps(payload))
		secure_passthrough_payload = {
			"method":"securePassthrough",
			"params":{
				"request": encrypted_payload
			}
		}
		r = self.session.post(URL, json=secure_passthrough_payload, headers=headers, timeout=2)
		decrypted_response = self.tpLinkCipher.decrypt(r.json()["result"]["response"])
		decrypted_response = json.loads(decrypted_response)
		decrypted_response['device'] = 'tapo_p115'
		return decrypted_response
