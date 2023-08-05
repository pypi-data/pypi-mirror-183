from requests import Response, get
from bs4 import BeautifulSoup, Tag
from ktu_mon.utils.constants import PAGE_URL, TABLE_CLASS, DATE_CLASS
from datetime import datetime


def scrape_it(time_func) -> tuple[list[tuple], str]:
    page: Response = get(PAGE_URL)
    soup: BeautifulSoup = BeautifulSoup(page.text, "html.parser")
    table: Tag = soup.find("table", class_=TABLE_CLASS)  # type: ignore
    notification_dates: list[str] = list()
    notification_titles: list[str] = list()
    timestamp: str = time_func()
    for notification in table.find_all("tr"):
        for label in notification.find_all("label", class_=DATE_CLASS):
            notification_dates.append(
                datetime.strptime(str(label.text), "%a %b %d %H:%M:%S IST %Y").strftime("%Y-%m-%dT%H:%M:%S")
            )
        for td in notification.find_all("td"):
            for li in td.find_all("li"):
                for b in li.find_all("b", limit=1):
                    notification_titles.append(b.text)

    notification_tuple: list[tuple] = list()
    for i in range(len(notification_titles)):
        notification_tuple.append((notification_dates[i], notification_titles[i]))

    return (notification_tuple, timestamp)
