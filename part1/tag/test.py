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
task_path = basepath.joinpath('part1', 'tag')
os.chdir(task_path)

class TagTestCase(SkyproTestCase):
    def setUp(self):
        with open("tag.html", 'r', encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        self.main = soup.body.main

    def test_main_span(self):
        span = self.main.span
        self.assertIsNotNone(
            span,
            "%@Проверьте, что добавили тег 'строка'(span)")
        span_tags = self.main.find_all('span', recursive=False)
        len_span = len(span_tags)
        self.assertEqual(
            len_span, 2,
            ("%@Проверьте что добавили все теги строка в блок main."
             f" Должно быть 2, тогда как у вас {len_span}"))
        expected_text = ['Посты по тегу', '3 поста']
        span_text = (span_text.text for span_text in span_tags)
        for expected, text, index in zip(expected_text, span_text, range(2)):
            self.assertEqual(
                expected, text,
                f"%@Проверьте что {index} строка в блоке main содержит правильный текст"
            )

    def test_header(self):
        header = self.main.h2
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 2 уровня.")
        self.assertEqual(
            header.text, '#Природа',
            "%@Проверьте что заголовок 2 уровня содержит правильный текст")


    def test_blocks(self):
        html_div = self.main.div
        self.assertIsNotNone(
            html_div,
            "%@Проверьте, что добавили блоки в тег main"
        )
        html_div_list = self.main.find_all('div')
        ln_div_list = len(html_div_list)
        self.assertEqual(
            ln_div_list, 3,
            ("%@Проверьте, что у Вас правильное"
             f" количество блоков. У Вас {ln_div_list},"
             " тогда как должно быть 3.")
        )
        tags = {
            'hr': 'орионтальный разделитель', 
            'a':'тег со ссылкой', 
            'img': 'картинку',
            'span':'тег со строкой'}
        users_text = {
            1: {'@happycorgi': ['Очень мило, мне все нравится!', 'img/tag_img_1.png']},
            2: {'@techirktsk': ['Нашел землю. Такая хорошенькая! Съем ее!', 'img/tag_img_2.png']},
            3: {'@awwawwaww': ['Смотрите, какой у меня пуховик, классно смотрится на фоне звездного неба, да?', 'img/tag_img_3.png']},
        }
        
        for div, index in zip(html_div_list, range(3)):
            for key in tags.keys():
                value = tags.get(key)
                self.assertIsNotNone(
                    getattr(div, key), f"%@Проверьте что {index+1} блок содержит {value}"
                )
            item = users_text.get(index+1).items()
            [[user, values]] = item
            self.assertEqual(
                div.a.text, user,
                f"%@Проверьте что {index+1} блок содержит ссылку с правильным пользователем."
            )
            self.assertEqual(
                div.span.text, values[0],
                f"%@Проверьте что {index+1} блок содержит правильный текст с комментарием."
            )
            self.assertEqual(
                div.img.attrs.get('src'), values[1],
                 f"%@Проверьте что {index+1} блок содержит нужную картинку."
            )

if __name__ == "__main__":
    unittest.main()