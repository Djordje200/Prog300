def super(self):
    if not self.dialog:
        self.dialog = MDDialog(
            title = "problem 2",
            text = "odje se nalazi rjesenje problema",
            buttons = [
                MDFlatButton(                       
                    text = "ok", text_color=self.theme_cls.primary_color, on_release = self.superc
                    ),
                ],
            )
        
    self.dialog.open()

def superc(self, obj):
    self.dialog.close()