import pystray
from pystray import MenuItem as Item
from PIL import Image
from time import sleep
from pathlib import Path
from ktu_mon.utils.dbops import fetch_config
from ktu_mon.utils import scraping
from ktu_mon.gui import run_gui, GUI_DIR
from ktu_mon.utils.constants import APP_NAME, PROC_ID_SYSTRAY, PROC_ID_TIMER
import concurrent.futures
import multiprocessing
import os

ICON_FILE = str(Path(GUI_DIR, "static", "icons", "ktu-mon-32x32.ico"))


def systray():
    image = Image.open(ICON_FILE)
    appmenu = pystray.Menu(
        Item("Open", on_clicked, default=True, visible=False),
        Item("Check Now!", on_clicked),
        Item("Open Interface", on_clicked),
        pystray.Menu.SEPARATOR,
        Item("Shutdown", lambda: stop(icon)),
    )
    icon = pystray.Icon(name=APP_NAME, icon=image, title=APP_NAME, menu=appmenu)

    def routine_check():
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while icon.visible:
                timer_sec = 60 * int(fetch_config("time_interval")[0][1])
                executor.submit(timer)
                while timer_sec != 0:
                    if icon.visible:
                        if fetch_config("notification_ind")[0][1] == "1":
                            icon.notify("KTU Mon has new notifications for you!")
                            print("KTU Mon has new notifications for you!")
                        sleep(60)
                        timer_sec -= 60
                    else:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

    def stop(icon):
        icon.visible = False
        print("Shutting down...")
        icon.stop()
        os._exit(0)

    def setup(icon):
        icon.visible = True
        routine_check()

    icon.run(setup=setup)


def cre_gui_proc():
    return multiprocessing.Process(target=run_gui)


def on_clicked(icon, item):
    gui_process = cre_gui_proc()
    if str(item) == "Open":
        print("Web interface is opened!")
        gui_process.start()
        try:
            gui_process.join()
        except KeyboardInterrupt as e:
            print(e)
        print("GUI Server Stopped!")
    elif str(item) == "Check Now!":
        print("Checking!")
        scraping(PROC_ID_SYSTRAY)
    elif str(item) == "Open Interface":
        print("Web interface is opened!")
        gui_process.start()
        try:
            gui_process.join()
        except KeyboardInterrupt as e:
            print(e)
        print("GUI Server Stopped!")
    else:
        print("Not implemented!")


def timer():
    sleep(60 * int(fetch_config("time_interval")[0][1]))
    print("Checking!")
    scraping(PROC_ID_TIMER)
