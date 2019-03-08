import pytest


async def test_roman_numeral_calculator_handler(async_app):
	client, app = async_app
	resp = await client.get('/roman_calculator?roman_numeral=I*I')
	assert resp.status == 200
	json_resp = await resp.json()
	assert json_resp['number'] == 1


async def test_roman_number_calculator_handler_invalid_input(async_app):
	client, app = async_app
	resp = await client.get('/roman_calculator?roman_numeral=random')
	assert resp.status == 400


async def test_is_fizz_buzz_number_handler(async_app):
	client, app = async_app
	resp = await client.get('/fizz_buzz_numbers')
	assert resp.status == 200
	json_resp = await resp.json()
	assert len(json_resp['fizz_buzz_numbers']) == 100
