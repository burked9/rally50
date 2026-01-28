import json

raw_json = """
[
{
    "name": "",
    "id": "0B4ubLJPS0mdTMnNzS0lXTy1FQWM"
  },
  {
    "name": "Derg Rally 02",
    "id": "0B4ubLJPS0mdTMnNzS0lXTy1FQWM"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTbWRBTndEeW43ekk"
  },
  {
    "name": "Derg Rally 03",
    "id": "0B4ubLJPS0mdTbWRBTndEeW43ekk"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTWE5uR3FMaWVUNWc"
  },
  {
    "name": "Derg Rally 04",
    "id": "0B4ubLJPS0mdTWE5uR3FMaWVUNWc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTzc4eC1jXzU0QVU"
  },
  {
    "name": "Derg Rally 05",
    "id": "0B4ubLJPS0mdTTzc4eC1jXzU0QVU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTcmFheWphX1ZZUjQ"
  },
  {
    "name": "Derg Rally 06",
    "id": "0B4ubLJPS0mdTcmFheWphX1ZZUjQ"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTeklUc0FZQXJjVEU"
  },
  {
    "name": "Derg Rally 07",
    "id": "0B4ubLJPS0mdTeklUc0FZQXJjVEU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTYUl5ckdvWnlFZHc"
  },
  {
    "name": "Derg Rally 08",
    "id": "0B4ubLJPS0mdTYUl5ckdvWnlFZHc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTZTZaeVVGMjFJR2s"
  },
  {
    "name": "Derg Rally 09",
    "id": "0B4ubLJPS0mdTZTZaeVVGMjFJR2s"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTZ2FrVXhoVHV5ejQ"
  },
  {
    "name": "Derg Rally 10",
    "id": "0B4ubLJPS0mdTZ2FrVXhoVHV5ejQ"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTMDhPNktIQVZueXM"
  },
  {
    "name": "Derg Rally 11",
    "id": "0B4ubLJPS0mdTMDhPNktIQVZueXM"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTaVo1NW5sQnNPbFk"
  },
  {
    "name": "Derg Rally 12",
    "id": "0B4ubLJPS0mdTaVo1NW5sQnNPbFk"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTU1dUbnd0Q2pjb1k"
  },
  {
    "name": "Derg Rally 13",
    "id": "0B4ubLJPS0mdTU1dUbnd0Q2pjb1k"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTeHR4NThVd2sxS0U"
  },
  {
    "name": "Derg Rally 14",
    "id": "0B4ubLJPS0mdTeHR4NThVd2sxS0U"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTVEdpMXFqNjhTbmc"
  },
  {
    "name": "Derg Rally 15",
    "id": "0B4ubLJPS0mdTVEdpMXFqNjhTbmc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTN29uckVick1UeUk"
  },
  {
    "name": "Derg Rally 16",
    "id": "0B4ubLJPS0mdTN29uckVick1UeUk"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTQ0ZHdVBlOGlpbkU"
  },
  {
    "name": "Derg Rally 17",
    "id": "0B4ubLJPS0mdTQ0ZHdVBlOGlpbkU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTemRxa29EN3hKX1E"
  },
  {
    "name": "Derg Rally 18",
    "id": "0B4ubLJPS0mdTemRxa29EN3hKX1E"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTQXlhel9XNG0tUHc"
  },
  {
    "name": "Derg Rally 19",
    "id": "0B4ubLJPS0mdTQXlhel9XNG0tUHc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTVHJDalF2Wi1zYmc"
  },
  {
    "name": "Derg Rally 20",
    "id": "0B4ubLJPS0mdTVHJDalF2Wi1zYmc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTMTYwUTM2MVNWVnM"
  },
  {
    "name": "Derg Rally 21",
    "id": "0B4ubLJPS0mdTMTYwUTM2MVNWVnM"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTSzdwMjhrbEFId2c"
  },
  {
    "name": "Derg Rally 22",
    "id": "0B4ubLJPS0mdTSzdwMjhrbEFId2c"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTZUpCSkRCWE04Vkk"
  },
  {
    "name": "Derg Rally 23",
    "id": "0B4ubLJPS0mdTZUpCSkRCWE04Vkk"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTXR4RXMtSmhfWXc"
  },
  {
    "name": "Derg Rally 24",
    "id": "0B4ubLJPS0mdTTXR4RXMtSmhfWXc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTMy14eG4wNkxVM3c"
  },
  {
    "name": "Derg Rally 25",
    "id": "0B4ubLJPS0mdTMy14eG4wNkxVM3c"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTUhQSklPTjZvSk0"
  },
  {
    "name": "Derg Rally 26",
    "id": "0B4ubLJPS0mdTTUhQSklPTjZvSk0"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTWWFaakR5QUstRlU"
  },
  {
    "name": "Derg Rally 27",
    "id": "0B4ubLJPS0mdTWWFaakR5QUstRlU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTUWpRS3haTks5NXc"
  },
  {
    "name": "Derg Rally 28",
    "id": "0B4ubLJPS0mdTUWpRS3haTks5NXc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTc3FXaVBkNXlVZzA"
  },
  {
    "name": "Derg Rally 29",
    "id": "0B4ubLJPS0mdTc3FXaVBkNXlVZzA"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTMmFUOC16d2dkcEE"
  },
  {
    "name": "Derg Rally 30",
    "id": "0B4ubLJPS0mdTMmFUOC16d2dkcEE"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTYlpVSmRtMWp5ekU"
  },
  {
    "name": "Derg Rally 31",
    "id": "0B4ubLJPS0mdTYlpVSmRtMWp5ekU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTajl1WWNXbWc3MVU"
  },
  {
    "name": "Derg Rally 32",
    "id": "0B4ubLJPS0mdTajl1WWNXbWc3MVU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTWDVEeFlSSGNqLUE"
  },
  {
    "name": "Derg Rally 33",
    "id": "0B4ubLJPS0mdTWDVEeFlSSGNqLUE"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTREwxejdpckV4X2c"
  },
  {
    "name": "Derg Rally 34",
    "id": "0B4ubLJPS0mdTREwxejdpckV4X2c"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTWHUtTlVtWEpOTFU"
  },
  {
    "name": "Derg Rally 35",
    "id": "0B4ubLJPS0mdTWHUtTlVtWEpOTFU"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTGdXazVtbVNXYjA"
  },
  {
    "name": "Derg Rally 36",
    "id": "0B4ubLJPS0mdTTGdXazVtbVNXYjA"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTMFZNaHcySWhOWmc"
  },
  {
    "name": "Derg Rally 37",
    "id": "0B4ubLJPS0mdTMFZNaHcySWhOWmc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTmROUlBGTHpFbGc"
  },
  {
    "name": "Derg Rally 38",
    "id": "0B4ubLJPS0mdTTmROUlBGTHpFbGc"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTY05IQ3BaR2dpQ3c"
  },
  {
    "name": "Derg Rally 39",
    "id": "0B4ubLJPS0mdTY05IQ3BaR2dpQ3c"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTTFFWMUZzalJtaDg"
  },
  {
    "name": "Derg Rally 40",
    "id": "0B4ubLJPS0mdTTFFWMUZzalJtaDg"
  },
  {
    "name": "",
    "id": "0B4ubLJPS0mdTRGZMLTlYSUNIaG8"
  },
  {
    "name": "Derg Rally 41",
    "id": "0B4ubLJPS0mdTRGZMLTlYSUNIaG8"
  },
  {
    "name": "",
    "id": "1e9QjP4ojAxLjnj2m_nmTnvkDyisMOtHr"
  },
  {
    "name": "Derg Rally 42",
    "id": "1e9QjP4ojAxLjnj2m_nmTnvkDyisMOtHr"
  },
  {
    "name": "",
    "id": "1YI7sgI0LnIK91tf6X_M9hELcCHhdF0SV"
  },
  {
    "name": "Derg Rally 43",
    "id": "1YI7sgI0LnIK91tf6X_M9hELcCHhdF0SV"
  },
  {
    "name": "",
    "id": "1vEz4SuCDEkr4Q28cl4cCw7quWwzK-dzH"
  },
  {
    "name": "Derg Rally 44",
    "id": "1vEz4SuCDEkr4Q28cl4cCw7quWwzK-dzH"
  },
  {
    "name": "Old Rally Magazines",
    "id": "0B4ubLJPS0mdTSmk3b25PUmlrbFU"
  }
]
"""

data = json.loads(raw_json)
# Filter duplicates: Keep items with names
cleaned = [ item for item in data if item.get('name') ]

print(json.dumps(cleaned, indent=4))
