import unittest
import requests
import json

class httpRequestsTest(unittest.TestCase):
	def test_getRoot(self):
		url = "http://localhost:8080/"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code) # add assertion here

	def test_getAvengers(self):
		url = "http://localhost:8080/avengers"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code) # add assertion here

	def test_getVillan(self):
		url = "http://localhost:8080/villan"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)

	def test_getAvengerName(self):
		url = "http://localhost:8080/avengername?name=Thor"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)

	def test_getMovieName(self):
		url = "http://localhost:8080/moviename?movie=Thor:%20Ragnarok"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_getVillans(self):
		url = "http://localhost:8080/villans?villans=Hela"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_getGadget(self):
		url = "http://localhost:8080/gadget/Miljoner/Thor"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_getAvengerQuotes(self):
		url = "http://localhost:8080/quotes/Hulk"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_getVillanrQuotes(self):
		url = "http://localhost:8080/quotesvillan/Loki"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_getYourAvenger(self):
		url = "http://localhost:8080/yourAvenger"
		response = requests.get(url)
		print("Status Code:", response.status_code)
		print("Response Body:", response.json())
		self.assertEqual(200, response.status_code)
  
	def test_verify_avenger_with_header(self):
		headers = {"X-Avenger-Code": "Av1234"}
		response = requests.get("http://localhost:8080/verify-avenger", headers=headers)
		self.assertEqual(response.status_code, 200)
		self.assertIn("Access granted", response.json()["message"])

	def test_welcome_user_with_cookie(self):
		cookies = {"username": "SpiderMan"}
		response = requests.get("http://localhost:8080/welcome", cookies=cookies)
		self.assertEqual(response.status_code, 200)
		self.assertIn("SpiderMan", response.json()["message"])