from datetime import datetime
from ktu_mon.utils.scraper import scrape_it
from ktu_mon.utils.dbops import (
    db_init,
    insert_log,
    insert_log_date,
    config_mod,
    fetch_config,
    fetch_comp,
    fetch_log_list,
    fetch_log,
    delete_log,
)
from ktu_mon.utils.constants import PROC_ID_INITIALIZER

scraper_active_ind = 0


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def init_db():
    try:
        db_init(get_time)
        scraping(PROC_ID_INITIALIZER)
    except Exception as e:
        print(e)


def scraping(proc_id) -> None:
    global scraper_active_ind
    if scraper_active_ind == 0:
        scraper_active_ind = 1
        data = scrape_it(get_time)
        time = get_time()
        for notif in data[0]:
            insert_log(notif[0], notif[1], proc_id, time, "temp")
        config_mod("last_checked", time, proc_id, get_time)
        added, removed, _ = log_insight(None, fetch_config("last_logged")[0][1], "temp")
        if added + removed > 0:
            for notif in data[0]:
                insert_log(notif[0], notif[1], proc_id, time, None)
            insert_log_date(time, proc_id, time)
            config_mod("last_logged", time, proc_id, get_time)
            config_mod("notification_ind", "1", proc_id, get_time)
            delete_log(time, "temp")
        else:
            delete_log(time, "temp")
        scraper_active_ind = 0
    else:
        print("Scraper in use!")


def log_insight(left_ts, right_ts, mode) -> tuple:
    if mode == "temp":
        data = fetch_comp(None, right_ts, "temp")
    else:
        data = fetch_comp(left_ts, right_ts, None)
    added_log_count = 0
    removed_log_count = 0
    notifications = list()
    for notification in data:
        if notification[2] is None:
            added_log_count += 1
            notifications.append([notification[0], notification[1], 1])
        elif notification[1] is None:
            removed_log_count += 1
            notifications.append([notification[0], notification[2], 2])
        else:
            notifications.append([notification[0], notification[1], 0])
    return (added_log_count, removed_log_count, notifications)


def log_deleter(date) -> None:
    delete_log(date, None)
    if fetch_config("last_logged")[0][1] == date:
        try:
            config_mod(
                "last_logged",
                fetch_log_list(0)[0][0],
                PROC_ID_INITIALIZER,
                get_time,
            )
        except IndexError:
            pass


def data_nodes() -> list:
    additions = list()
    removals = list()
    dates = list()
    length = len(fetch_log_list(0))
    added = int()
    removed = int()
    logs = list()
    total_logs = list()
    for i in range(length):  # type: ignore
        try:
            added, removed, logs = log_insight(fetch_log_list(0)[i][0], fetch_log_list(0)[i + 1][0], None)
        except IndexError:
            pass
        try:
            additions.append(added)
            removals.append(removed)
            dates.append(
                datetime.strptime(fetch_log_list(0)[i][0], "%Y-%m-%dT%H:%M:%S").strftime("%d %b %Y %I:%M %p")
            )
        except UnboundLocalError:
            pass
    try:
        dates.pop()
        additions.pop()
        removals.pop()
    except IndexError:
        pass

    for i in fetch_log(fetch_config("last_logged")[0][1], mode=None):
        total_logs.append(i[0])

    dateset = [*set(total_logs)]
    dateset.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S"))

    full_log_insight = list()
    log_dates = list()
    log_count = list()
    for date in dateset:
        count = total_logs.count(date)
        log_dates.append(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime("%d %b %Y"))
        log_count.append(count)

    full_log_insight.append(log_dates)
    full_log_insight.append(log_count)
    dates.reverse()
    additions.reverse()
    removals.reverse()
    return [dates, additions, removals, full_log_insight]
