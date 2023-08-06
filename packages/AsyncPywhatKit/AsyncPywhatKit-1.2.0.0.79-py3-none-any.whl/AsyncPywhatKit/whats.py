import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
from typing import List
from urllib.parse import quote
import pyperclip
import keyboard
import pathlib
import asyncio
import pyautogui as pg
import asyncio
import os
from AsyncPywhatKit.Core import core, log, exceptions

pg.FAILSAFE = False


async def main():
    await core.check_connection()



loop = asyncio.get_event_loop()
loop.run_until_complete(main())


async def sendwhatmsg_instantly(
        message: str,
        phone_no: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3
) -> None:
    print(phone_no)
    """Send a whatsapp Message Instantly"""
    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")
    phone_no = phone_no.replace(" ", "")
    print(phone_no)
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")
    phone_no = phone_no.replace(" ", "")
    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}", new=0)
    await asyncio.sleep(wait_time)
    pg.press('enter')
    await asyncio.sleep(close_time)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg(
        phone_no: str,
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    await asyncio.sleep(sleep_time)
    await sendwhatmsg_instantly(message,phone_no)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg_to_group(
        group_id: str,
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group at a Certain Time"""

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and after {wait_time} Seconds Message will be Delivered!"
    )
    await asyncio.sleep(sleep_time)
    await sendwhatmsg_instantly(group_id, message)
    await log.log_message(_time=current_time, receiver=group_id, message=message)
    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatmsg_to_group_instantly(
        group_id: str,
        message: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message to a Group Instantly"""

    current_time = time.localtime()
    await asyncio.sleep(4)
    await sendwhatmsg_instantly(group_id, message)
    await log.log_message(_time=current_time, receiver=group_id, message=message)

    if tab_close:
        await core.close_tab(wait_time=close_time)


async def sendwhatsmsg_to_all(
        phone_nos: List[str],
        message: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
):
    for phone_no in phone_nos:
        await sendwhatmsg(
            phone_no, message, time_hour, time_min, wait_time, tab_close, close_time
        )



async def sendimg_or_video_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = False,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    await core.find_link()
    time.sleep(1)
    await core.find_photo_or_video()
    if type(path) == str:
        path = pathlib.Path(path)
        pyperclip.copy(str(path.resolve()))
        print("Copied")
    else:
        strn = []
        for paths in path:
            patha = str(pathlib.Path(paths).resolve())
            strn.append(f'"{patha}"')

        print(" ".join(strn))
        pyperclip.copy(" ".join(strn))
    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        await core.close_tab(wait_time=close_time)

async def sendwhatsdoc_immediately(
        phone_no: str,
        path: str,
        wait_time: int = 15,
        tab_close: bool = True,
        close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not await core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r"^\+?[0-9]{2,4}\s?[0-9]{9,15}", phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    time.sleep(wait_time)
    await core.find_link()
    time.sleep(1)
    await core.find_document()
    if type(path) == str:
        path = pathlib.Path(path)
        pyperclip.copy(str(path.resolve()))
        print("Copied")
    else:
        strn = []
        for paths in path:
            patha = str(pathlib.Path(paths).resolve())
            strn.append(f'"{patha}"')

        print(" ".join(strn))
        pyperclip.copy(" ".join(strn))

    time.sleep(1)
    keyboard.press("ctrl")
    keyboard.press("v")
    keyboard.release("v")
    keyboard.release("ctrl")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(1)
    keyboard.press("enter")
    keyboard.release("enter")
    if tab_close:
        await core.close_tab(wait_time=close_time)



def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True
