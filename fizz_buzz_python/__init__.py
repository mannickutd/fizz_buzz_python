from aiohttp import web
from fizz_buzz_python.fizz_buzz_pink_flamingo import is_fizz_buzz_number
from fizz_buzz_python.roman_numerals_calculator import roman_numeral_calculator


async def roman_numeral_calculator_handler(request):
    roman_numeral = request.rel_url.query.get('roman_numeral', '')
    try:
        num = roman_numeral_calculator(roman_numeral)
        return web.json_response({
            'number': num,
        })
    except ValueError as e:
        raise web.HTTPBadRequest()


async def is_fizz_buzz_number_handler(request):
    return web.json_response({
        'fizz_buzz_numbers': [is_fizz_buzz_number(i) for i in range(100)],
    })


def create_app():
    app = web.Application()
    app.add_routes([
        web.get('/roman_calculator', roman_numeral_calculator_handler),
    ])
    app.add_routes([
        web.get('/fizz_buzz_numbers', is_fizz_buzz_number_handler),
    ])
    return app
