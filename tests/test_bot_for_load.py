import os
import sys
import pytest
from telegram import Update, Message, Document, Chat

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tg_bot')))

from tg_bot.bot_for_load  import handle_file


@pytest.fixture
def update():
    chat = Chat(12345, 'test_chat')
    return Update(12345, message=Message(12345, chat=chat, date='2022-01-01', document=Document('12345', None, 'file.pdf'), caption='invalid_table_name'))


@pytest.fixture
def context():
    return {}


def test_handle_file_error_message(update, context):
    with pytest.raises(Exception) as e:
        handle_file(update, context)
    assert str(e.value) == "'NoneType' object has no attribute 'defaults'"
