class text_loading_scene:

    def __init__(self, time = 0, Text = "") -> None:
        self.time_loading = time
        self.TEXT = Text
        pass

    def RUN(self):
        text_output = ""
        if self.TEXT == "loading \ ":
            text_output = "loading | "
        elif self.TEXT == "loading | ":
            text_output = "loading / "
        elif self.TEXT == "loading / ":
            text_output = "loading _ "
        elif self.TEXT == "loading | ":
            text_output = "loading / "
        
        self.TEXT = self.text_output
        return self.text_output
    pass