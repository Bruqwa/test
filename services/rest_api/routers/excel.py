from fastapi import APIRouter, Response
from openpyxl import Workbook
from datetime import datetime
from random import randint, choice, sample
from io import BytesIO


router = APIRouter()

@router.get('/files')
async def table()->Response:
    today = datetime.now()

    upper_letters = 'ABCDEFGHIJKLOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklopqrstuvwxyz'
    numbers = '0123456789'
    letters = upper_letters + lower_letters
    random_chars_lst = [choice(letters) for i in range(randint(1,6))] + [choice(numbers) for j in range(randint(1,6))]
    random_str = ''.join(sample(random_chars_lst, len(random_chars_lst)))

    wb = Workbook()
    ws = wb.active

    ws['A1'] = 'Дата'
    ws['B1'] = 'Время'
    ws['C1'] = 'Случайное число'
    ws['D1'] = 'Случайная строка'

    ws['A2'] = today.date()
    ws['B2'] = today.time()
    ws['C2'] = randint(0, 1000)
    ws['D2'] = random_str

    file = BytesIO()
    wb.save(file)
    file.seek(0)

    file_date = today.date().strftime('%Y%m%d')

    file_name = f'file_generated_at_{file_date}.xlsx'

    return Response(file.read(), headers = {'Content-Disposition': f'attachment; filename={file_name}'})
