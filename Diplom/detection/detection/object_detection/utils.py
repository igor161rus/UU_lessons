import base64
import io

import matplotlib
import matplotlib.pyplot as plt

import cv2
import numpy as np
# import requests
import torch
from exif import Image as ExifImage
from django.core.files.base import ContentFile
from django.db.models import Count
from django_admin_geomap import GeoItem
from .models import *
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from translate import Translator

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Приборная доска', 'url_name': 'dashboard'},
        {'title': 'О нас', 'url_name': 'about'},
        ]

VOC_LABELS = [
    "background", "aeroplane", "bicycle", "bird", "boat", "bottle",
    "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.annotate(Count('women'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        # context['cats'] = cats
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context


def process_image(image_feed_id):
    try:
        image_feed = ImageFeed.objects.get(id=image_feed_id)
        # detected_objects = DetectedObject.objects.filter(image_feed=image_feed)
        image_path = image_feed.image.path

        model_path = 'object_detection/mobilenet_iter_73000.caffemodel'
        config_path = 'object_detection/mobilenet_ssd_deploy.prototxt'
        net = cv2.dnn.readNetFromCaffe(config_path, model_path)

        img = cv2.imread(image_path)
        if img is None:
            print("Failed to load image")
            return False

        h, w = img.shape[:2]
        blob = cv2.dnn.blobFromImage(img, 0.007843, (300, 300), 127.5)

        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.6:
                class_id = int(detections[0, 0, i, 1])
                class_label = VOC_LABELS[class_id]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
                label = f"{class_label}: {confidence:.2f}"
                cv2.putText(img, label, (startX + 5, startY + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                DetectedObject.objects.create(
                    image_feed=image_feed,
                    object_type=class_label,
                    location=f"{startX},{startY},{endX},{endY}",
                    confidence=float(confidence),
                    # processed_image=''
                )

        result, encoded_img = cv2.imencode('.jpg', img)

        detected_objects = DetectedObject.objects.filter(image_feed=image_feed).first()
        print(detected_objects)
        print(result)
        if detected_objects:
            if result:
                content = ContentFile(encoded_img.tobytes(), f'{image_feed.image.name}')
                print(content)
                print(content.name)
                # image_feed.processed_image.save(content.name, content, save=True)
                detected_objects.method_detected = 'Caffe'
                detected_objects.processed_image.save(content.name, content, save=True)

        return True

    except ImageFeed.DoesNotExist:
        print("ImageFeed not found.")
        return False


def process_image_detr(image_feed_id):
    """
        Функция определения объектов на изображении с использованием библиотеки DEtection TRansformers (DETR).
        Args:
            image_feed_id (int): идентификатор изображения для обработки.
        Returns:
            bool: True, если обработка прошла успешно.
    """
    image_feed = ImageFeed.objects.get(id=image_feed_id)
    image_path = image_feed.image.path

    image = Image.open(image_path)

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )

        DetectedObject.objects.create(
            image_feed=image_feed,
            object_type=model.config.id2label[label.item()],
            location=f"{box[0]},{box[1]},{box[2]},{box[3]}",
            confidence=float(score.item())
            # processed_image=''
        )

        image = cv2.rectangle(np.array(image), (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        label = f'{model.config.id2label[label.item()]}: {round(score.item(), 2)}'
        image = cv2.putText(np.array(image), label, (int(box[0]) + 5, int(box[1]) + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        result, encoded_img = cv2.imencode('.jpg', image)
        detected_objects = DetectedObject.objects.filter(image_feed=image_feed).first()
        if result:
            # content = ContentFile(encoded_img.tobytes(), f'processed_{image_feed.image.name}')
            content = ContentFile(encoded_img.tobytes(), image_feed.image.name)
            # image_feed.processed_image.save(content.name, content, save=True)
            detected_objects.method_detected = 'Torch'
            detected_objects.processed_image.save(content.name, content, save=True)

    return True


def image_caption(image_feed_id):
    """
        Функция возвращает описание изображения.
        Parameters:
            image (PIL.Image): изображение.
        Returns:
            str: описание изображения.
    """
    image_feed = ImageFeed.objects.get(id=image_feed_id)
    image_path = image_feed.image.path

    image = Image.open(image_path)

    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    # def predict_step(image_paths):
    #     images = []
    #     for image_path in image_paths:
    #         i_image = Image.open(image_path)
    #         if i_image.mode != "RGB":
    #             i_image = i_image.convert(mode="RGB")
    #
    #         images.append(i_image)

    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    print(preds)
    if preds:
        translator = Translator(from_lang="english", to_lang="russian")
        translation = translator.translate(preds[0])
        image_feed.description = translation
        image_feed.save()
    return preds

    # predict_step(['doctor.e16ba4e4.jpg'])  # ['a woman in a hospital bed with a woman in a hospital bed']


def get_graph():
    """
        Функция генерирует изображение текущего графика в кодировке Base64.
        Returns:
            str: изображение графика в кодировке Base64.
    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, type_graph):
    """
        Функция создает график с помощью библиотеки matplotlib и с логарифмической шкалой y.
        Parameters:
            x (array-like): список значений по оси x.
            y (array-like): список значений по оси y.
            type_graph (str): тип графика для сохранения графика.
        Returns:
            matplotlib.figure.Figure: сгенерированный график.
    """
    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 'large',
            }
    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)

    matplotlib.rc('font', size=20)
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0), useMathText=True)
    # plt.rc('axes.formatter', use_mathtext=True)

    # plt.style.use('_mpl-gallery')
    plt.switch_backend('AGG')
    plt.figure(figsize=(15, 5))
    # plt.subplot(1, 1, 1)
    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    plt.yscale('log')
    plt.title("График", fontdict=font)
    plt.xlabel('Объекты', fontdict=font)
    plt.ylabel('Вероятность', fontdict=font)
    plt.tight_layout()
    plt.savefig(type_graph + '.png')

    # read_exif_data(42)

    return get_graph()


def get_plot_stat(x, y, type_graph):
    """
        Функция создает график метода определения объектов с помощью библиотеки matplotlib и с логарифмической шкалой y.
        Parameters:
            x (array-like): список значений по оси x.
            y (array-like): список значений по оси y.
            type_graph (str): тип графика для сохранения графика.
        Returns:
            matplotlib.figure.Figure: сгенерированный график.
    """
    # plt.style.use('_mpl-gallery')
    plt.switch_backend('AGG')
    # plt.figure(figsize=(15, 5))
    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    plt.yscale('log')
    plt.title("График")
    plt.xlabel('Метод', fontsize=12)
    plt.ylabel('Количество', fontsize=12)
    plt.savefig(type_graph + '.png')

    # read_exif_data(42)
    return get_graph()


def read_exif_data(file_id):
    lat = lon = None
    image_name = ImageFeed.objects.get(id=file_id).image.name
    print(1, image_name)
    file_path = settings.MEDIA_ROOT + '/' + image_name
    with open(file_path, 'rb') as f:
        f_exif = ExifImage(f)
        print(2, f_exif.has_exif)
        if f_exif.has_exif:
            lat, lon = f_exif.gps_latitude, f_exif.gps_longitude
            print(3, f_exif.list_all())
            print(4, f_exif.gps_latitude)
            print(5, f_exif.gps_longitude)

    return lat, lon

    # print(2,  f_exif.info.decode('utf-8'))
