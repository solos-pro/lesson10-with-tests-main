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
task_path = basepath.joinpath('part1', 'company')
os.chdir(task_path)

class SettingsTestCase(SkyproTestCase):
    def setUp(self):
        with open("company.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, 'Профиль компании',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")

    def test_paragraphs(self):
        paragraphs = self.main.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что добавили абзац в тело тега main"
        )
        expected = {
            0: ['strong', "Sky.pro"],
            1: ['i', 'Онлайн-университет Рентабельного образования'],
            2: ['Освойте новую профессию и улучшите качество жизни. Поменяйте свою жизнь к лучшему за полгода!'],
            3: ['26 постов 2K подписчиков']
        }

        paragraphs = self.main.find_all('p', recursive=False)

        for paragraph, index in zip(paragraphs, range(len(expected))):
            expected_list = expected.get(index)
            if len(expected_list) > 1:
                tag = getattr(paragraph, expected_list[0])
                self.assertIsNotNone(
                    tag, 
                    f"%@Проверьте, что добавили тег {tag.name} в абзац {index+1}"
                )
                self.assertEqual(
                    tag.text, expected.get(index)[1],
                    f"%@Проверьте, правильный ли текст в абзаце {index+1}")
            else:
                self.assertEqual(
                    paragraph.text, expected.get(index)[0],
                    f"%@Проверьте, правильный ли текст в абзаце {index+1}")
            if index == 3:
                strongs = paragraph.find_all('strong')
                len_strongs = len(strongs)
                self.assertEqual(
                    len_strongs, 2,
                    "%@Проверьте что выделяли текст жирным в последнем абзаце."
                )
                expected_list = ['26', '2K']
                for strong, expected in zip(strongs, expected_list):
                    self.assertEqual(
                        strong.text, expected,
                        f'%@Проверьте что текст {strong.text} выделен жирным'
                    )
    
    def test_image(self):
        image = self.main.img
        self.assertIsNotNone(
            image,
            "%@Проверьте, что добавили картинку.")

    def test_has_hr(self):
        hrs = self.main.find_all('hr')
        len_hrs = len(hrs)
        self.assertEqual(
            len_hrs, 2,
            f"%@ Проверьте, что не забыли про разделители. Их должно быть 2, тогда как у Вас {len_hrs}"
        )


if __name__ == "__main__":
    unittest.main()