import os
import requests

from flask import render_template, request, flash, redirect, app, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename
import cv2 as cv
from imageDatabase.forms import UploadImageForm
from imageDatabase.model import Image, Type


class InsertIntoImageDatabseView(MethodView):
    init_every_request = False

    def get(self):
        form = UploadImageForm()
        return render_template('imageUpload.html', form=form)

    def post(self):
        form = UploadImageForm()

        if form.validate():
            if form.file.data.filename:
                file = request.files['file']
                if file:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join('protected/', filename))
            if form.url:
                img_data = requests.get(form.url.data).content
                filename = secure_filename(form.url.data.split('/')[-1])
                with open(os.path.join('protected/' + filename), 'wb') as handler:
                    handler.write(img_data)

            img = cv.imread(cv.samples.findFile(os.path.join('protected/', filename), cv.IMREAD_GRAYSCALE))
            minHessian = 400
            detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
            keypoints, descriptors = detector.detectAndCompute(img, None)

            image = Image()
            image.title = filename
            if form.url:
                image.type = Type.URL
                image.url = form.url.data
            else:
                image.type = Type.FILE
                image.path = os.path.join('protected/', filename)

            image.descriptors = descriptors.tolist()
            # image.keypoints = list(keypoints)
            image.save()

            flash("Upload Complete", 'success')
            return redirect(url_for('imageUpload'))

        else:
            return render_template('imageUpload.html', form=form, errors=form.errors)


class GetImagesInDB(MethodView):

    def get(self):
        images = Image.objects.all()
        return render_template('imageList.html', images=images)
