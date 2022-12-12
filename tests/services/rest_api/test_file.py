import datetime
import os
import pytest
from openpyxl import load_workbook
from services.rest_api.routers import API_PREFIX


@pytest.mark.asyncio
async def test_generation(client):
    response = await client.get(f"{API_PREFIX}/files/")
    assert response.status_code == 200, f"status_code={response.json()['success']}, response={response.text}"

    file_path = "tests/fixtures/test_file.xlsx"
    with open(file_path, "wb") as sf:
        sf.write(response.content)
    wb_response = load_workbook(file_path)
    wb_sheet = wb_response.active
    assert wb_sheet['A1'].value == 'Дата'
    assert wb_sheet['B1'].value == 'Время'
    assert wb_sheet['C1'].value == 'Случайное число'
    assert wb_sheet['D1'].value == 'Случайная строка'
    assert wb_sheet['E1'].value is None

    assert wb_sheet['A2'].value.year == datetime.date.today().year
    assert wb_sheet['A2'].value.month == datetime.date.today().month
    assert wb_sheet['A2'].value.day == datetime.date.today().day
    assert wb_sheet['B2'].value.hour == datetime.datetime.now().time().hour
    assert wb_sheet['B2'].value.minute == datetime.datetime.now().time().minute
    assert wb_sheet['B2'].value.second == datetime.datetime.now().time().second
    assert wb_sheet['C2'].value is not None
    assert wb_sheet['D2'].value is not None
    assert wb_sheet['A3'].value is None
    # wb.save(file_path)
    os.remove(file_path)
