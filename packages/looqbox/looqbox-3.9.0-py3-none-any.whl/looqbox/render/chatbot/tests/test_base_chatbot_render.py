from looqbox.render.chatbot.base_chatbot_render import BaseChatbotRender
from looqbox.objects.visual.looq_message import ObjMessage
from looqbox.objects.visual.looq_text import ObjText
from looqbox.objects.visual.looq_table import ObjTable
from looqbox.view.response_frame import ResponseFrame
from looqbox.view.response_board import ResponseBoard
from pandas import DataFrame
import unittest


class TestBaseChatbotRender(unittest.TestCase):
    def setUp(self) -> None:
        self.render = BaseChatbotRender()

        self.message = ObjMessage("I'm a message")
        self.text = ObjText("I'm a text")
        self.table = ObjTable(DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))

        self.frame = ResponseFrame([self.message, self.text, self.table])
        self.board = ResponseBoard([self.frame])

    def test_obj_message(self):
        expected = {
            "type": "text/plain",
            "text": "I'm a message",
        }

        actual = self.message.to_json_structure(self.render)
        self.assertEqual(expected, actual)

    def test_obj_text(self):
        expected = {
            "type": "text/plain",
            "text": "I'm a text",
        }

        actual = self.text.to_json_structure(self.render)
        self.assertEqual(expected, actual)

    def test_obj_table(self):
        excepted = []
        actual = self.table.to_json_structure(self.render)
        self.assertEqual(excepted, actual)

    def test_obj_table_with_title(self):
        title = "I'm a title"
        self.table.title = title

        excepted = [{
            "type": "text/plain",
            "text": title,
        }]

        actual = self.table.to_json_structure(self.render)
        self.assertEqual(excepted, actual)

    def test_obj_table_with_total(self):
        total = {"a": 6, "b": 15}
        self.table.total = total

        excepted = [
            {
                "type": "text/plain",
                "text": "a 6\nb 15",
            }
        ]

        actual = self.table.to_json_structure(self.render)
        self.assertEqual(excepted, actual)

    def test_obj_table_with_total_format(self):
        total = {"a": 6, "b": 15}
        self.table.total_format = {"a": "number:2", "b": None, "c": "number:2"}
        self.table.total = total

        excepted = [
            {
                "type": "text/plain",
                "text": "a 6,00\nb 15",
            }
        ]

        actual = self.table.to_json_structure(self.render)
        self.assertEqual(excepted, actual)

    def test_response_frame(self):
        expected = [
            {
                "type": "text/plain",
                "text": "I'm a message"
            },
            {
                "type": "text/plain",
                "text": "I'm a text"
            },
        ]
        actual = self.frame.to_json_structure(self.render)
        self.assertEqual(expected, actual)

    def test_response_frame_with_title(self):
        title = "I'm a title"
        self.frame.title = title

        expected = [
            {
                "type": "text/plain",
                "text": title,
            },
            {
                "type": "text/plain",
                "text": "I'm a message"
            },
            {
                "type": "text/plain",
                "text": "I'm a text"
            },
        ]

        actual = self.frame.to_json_structure(self.render)
        self.assertEqual(expected, actual)

    def test_response_board(self):
        ...


if __name__ == '__main__':
    unittest.main()
