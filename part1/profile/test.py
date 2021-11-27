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
task_path = basepath.joinpath('part1', 'profile')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("profile.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Профиль',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_table(self):
        html_table = self.main.table
        self.assertIsNotNone(
            html_table,
            "%@Проверьте, что добавили Таблицу в тег main"
        )
        expected_values = {
            0: ['1225 Просмотров', '250 Лайков'],
            1: ['65 Комментариев', '+ 12 Подписчиков'],
        }
        len_expected_columns = len(expected_values.get(0))
        len_expected_values = len(expected_values)
        html_table_rows = self.main.find_all('tr')
        ln_html_table_rows = len_expected_values
        self.assertEqual(
            ln_html_table_rows, len_expected_values,
            ("%@Проверьте, что у Вас правильное"
             f" количество cтрок в таблице. У Вас {ln_html_table_rows},"
             f" тогда как должно быть {len_expected_values}.")
        )
        for row, index in zip(html_table_rows, range(len_expected_values)):
            cells = row.find_all('td')
            self.assertEqual(
                len(cells), len_expected_columns,
               f"%@Проверьте, что в {index+1} строке таблицы только {len_expected_columns} ячейки")
            for column in range(len_expected_columns):
                self.assertEqual(
                    cells[column].text, expected_values.get(index)[column],
                    f"%@Проверьте что в строке {index+1} правильный текст"
                )

    def test_paragraphs(self):
        paragraphs = self.main.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что добавили абзац в тело тега main"
        )
        expected = {
            0: ['a', "Редактировать"]
        }

        paragraphs = self.main.find_all('p', recursive=False)

        for paragraph, index in zip(paragraphs, range(len(expected))):
            tag = getattr(paragraph, expected.get(index)[0])
            self.assertIsNotNone(
                tag, 
                f"%@Проверьте, что добавили тег {tag.name} в абзац"
            )
            self.assertEqual(
                tag.text, expected.get(index)[1],
                f"%@Проверьте, правильный ли текст в абзаце")


if __name__ == "__main__":
    unittest.main()