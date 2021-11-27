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
task_path = basepath.joinpath('part1', 'rules')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("rules.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Правила сервиса',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_paragraphs(self):
        paragraphs = self.main.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что добавили абзацы в тег main"
        )
        expected = {
            0: ['i', ("Сервис предоставляется как "
                      "есть. Если вы не хотите чтобы "
                      "фото стало общедоступным - не "
                      "заружайте его.")],
            1: ['i', ("Мы храним Ваши данные и "
                      "следим за Вами, но не для того, "
                      "чтобы продать Ваши данные, "
                      "просто мы любопытные.")],
            2: ['a', "Я соглашаюсь"],
            3: ['a',"Мне нужно подумать"],
        }
        expected_len = len(expected)
        paragraphs = self.main.find_all('p', recursive=False)
        current_len = len(paragraphs)
        self.assertEqual(
            current_len, expected_len,
            (f"%@Проверьте, что добавили все абзацы. У Вас их {current_len}, "
             f"тогда как должно быть {expected_len}"))


        for paragraph, index in zip(paragraphs, range(len(expected))):
            tag = getattr(paragraph, expected.get(index)[0])
            self.assertIsNotNone(
                tag, 
                f"%@Проверьте, что добавили все теги {tag.name} в абзацы"
            )
            self.assertEqual(
                tag.text, expected.get(index)[1],
                f"%@Проверьте, правильный ли текст в абзаце {index+1}")


if __name__ == "__main__":
    unittest.main()