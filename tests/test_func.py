from src.classes import HeadHunterAPI
from src.func import user_interaction, choise_command

import pytest

def test_user_interaction():
 quantity = 1
 keyword = "Python"
 hh_api = HeadHunterAPI()
 vacancies = hh_api.get_vacancies(keyword, quantity)
 assert len(vacancies) == 1

def test_user_interaction():
 quantity = 2
 keyword = "Python"
 hh_api = HeadHunterAPI()
 vacancies = hh_api.get_vacancies(keyword, quantity)
 assert vacancies != None
