import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
import os

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
task_path = basepath.joinpath('part1', 'trends')
os.chdir(task_path)

class TrendTestCase(SkyproTestCase):
    def setUp(self):
        with open("trends.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Cейчас в тренде',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")
        
    def test_paragraph(self):
        html_list_numbers = self.main.ol
        self.assertIsNotNone(
            html_list_numbers,
            "%@Проверьте, что добавили тег 'Нумерованный список'")
        li_elements = html_list_numbers.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 10,
            ("%@Проверьте что добавили все элементы списка."
             f" Должно быть 10, тогда как у вас {len_elements}"))
        trends = [
            '#супер',
            '#день',
            '#ночь',
            '#природа',
            '#семья',
            '#улыбка',
            '#селфи',
            '#кусь',
            '#следуйзамной',
            '#instagood',
        ]
        for trend, element, index in zip(trends, li_elements, range(10)):
            self.assertIsNotNone(
                element.a, "%@Проверьте что все элементы списка содержат тег 'ссылка'"
            )
            self.assertIsNotNone(
                element.a.attrs.get('href'),
                "%@Проверьте что все ссылки имеют аттрибут href"
            )
            self.assertEqual(
                element.a.attrs.get('href'), '#',
                "%@Проверьте, что всем аттрибутам href присвоено значение заглушки '#'"
            )
            self.assertEqual(
                element.a.text, trend,
                f"%@Проверьте, что {index+1} элемент списка имеет верное значение"
            )
        

if __name__ == "__main__":
    unittest.main()