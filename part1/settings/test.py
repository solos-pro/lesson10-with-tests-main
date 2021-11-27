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
task_path = basepath.joinpath('part1', 'settings')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("settings.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Настройки',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_table(self):
        html_table = self.main.table
        self.assertIsNotNone(
            html_table,
            "%@Проверьте, что добавили Таблицу в тег main"
        )
        expected_values = {
            0: ['Показывать котов:', 'да'],
            1: ['Показывать еду:', 'нет'],
            2: ['Показывать сов:', 'нет'],
            3: ['Включить кэш:','нет'],
            4: ['Показывать рекламу:','да'],
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

    def test_crossed(self):
        paragraphs = self.main.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что добавили абзацы в тег main"
        )
        expected_len = 2
        paragraphs_with_crossed = self.main.find_all('p', recursive=False)
        current_len = len(paragraphs_with_crossed)
        self.assertEqual(
            current_len, expected_len,
            (f"%@Проверьте, что добавили все абзацы. У Вас их {current_len}, "
             f"тогда как должно быть {expected_len}"))
        cross_strings_values = {
            0: 'Включить кэш',
            1: 'Показывать рекламу',
        }
        for paragraph, index in zip(paragraphs_with_crossed, range(len(cross_strings_values))):
            cross_string = paragraph.s
            self.assertIsNotNone(
                cross_string, 
                "%@Проверьте, что добавили тег с зачеркнутой строкой во все теги <p>"
            )
            self.assertEqual(
                cross_string.text, cross_strings_values.get(index),
                "%@Проверьте, правильный ли текст в зачеркнутых строках")


if __name__ == "__main__":
    unittest.main()