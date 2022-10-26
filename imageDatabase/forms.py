from flask_wtf import FlaskForm
from wtforms import FileField, StringField


class UploadImageForm(FlaskForm):
    file = FileField(render_kw={'placeholder': "FilePath"})
    url = StringField(render_kw={'palceholder': 'Url'})

    def validate(self):
        if not super().validate():
            return False
        if self.file.data and self.url.data:
            msg = 'Choose only one method of image insertion'
            self.file.errors.append(msg)
            self.url.errors.append(msg)
            return False
        if not self.file.data and not self.url.data:
            msg = 'No file selected'
            self.file.errors.append(msg)
            self.url.errors.append(msg)
            return False
        return True
