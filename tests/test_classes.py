from src.classes import HeadHunterAPI, Vacancy, JSONSaver
import pytest

def test_get_vacancies():
    vac = HeadHunterAPI()
    assert vac.get_vacancies("Python", 2) != None

def test__str__():
    vac = Vacancy()
    assert vac != None

def test__lt__():
    vac = JSONSaver()
    assert len(vac.read_vacancy()) == 2