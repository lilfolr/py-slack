import npyscreen


class TestApp(npyscreen.NPSApp):
    def main(self):
        F = npyscreen.Form(name="Py-Slack")
        F.add(npyscreen.BoxBasic, name="Stared Channels", max_width=40, relx=2, max_height=3, scroll_exit=True)

        t2 = F.add(npyscreen.BoxTitle, name="Channels", max_height=6, max_width=40, scroll_exit=True)
        F.add(npyscreen.BoxTitle, name="Direct Messages", max_height=6, max_width=40, scroll_exit=True)

        t2.values = []

        F.add(npyscreen.BoxBasic, name="Chat", rely=2, relx=42, scroll_exit=True)

        F.edit()


if __name__ == "__main__":
    App = TestApp()
    App.run()

