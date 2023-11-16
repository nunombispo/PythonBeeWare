"""
Daily Quote application
"""
import requests
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class DailyQuote(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button = toga.Button(
            "Get Random Quote",
            on_press=self.get_random_quote,
            style=Pack(padding=5)
        )

        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def get_random_quote(self, widget):
        """
        Get a random quote from the API
        """
        response = requests.get("https://api.quotable.io/quotes/random?limit=1")
        if response.status_code == 200:
            json_response = response.json()[0]
            quote = json_response["content"]
            author = json_response["author"]
            self.main_window.info_dialog(
                "Random Quote",
                f"{quote} \n- {author}"
            )


def main():
    return DailyQuote()
