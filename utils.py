import os
from dotenv import load_dotenv
import json


def get_openai_api_key():
    """
    .env fayldan OPENAI_API_KEY ni o'qiydi.
    Agar topilmasa, xatolik qaytaradi.
    """
    # .env faylni yuklash
    load_dotenv()

    # Kalitni olish
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY topilmadi! .env faylga qo‘shing.")

    return api_key


def get_serper_api_key():
    """
    .env fayldan SERPER_API_KEY ni o'qiydi.
    Agar topilmasa, xatolik qaytaradi.
    """
    # .env faylni yuklash
    load_dotenv()

    api_key = os.getenv("SERPER_API_KEY")

    if not api_key:
        raise ValueError("SERPER_API_KEY topilmadi! .env faylga qo‘shing.")

    return api_key


def pretty_print_result(result):
    """
    Natijani chiroyli JSON formatda bosib chiqaradi.
    """
    print(json.dumps(result, indent=4, ensure_ascii=False))
