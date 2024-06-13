import base64
import io
import matplotlib.pyplot as plt

import cv2
import numpy as np
# import requests
import torch
from django.core.files.base import ContentFile
from django.db.models import Count
from .models import *
from PIL import Image
from transformers import DetrImageProcessor, DetrForObjectDetection

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
                    processed_image=''
                )

        result, encoded_img = cv2.imencode('.jpg', img)

        detected_objects = DetectedObject.objects.filter(image_feed=image_feed).first()
        print(detected_objects)
        print(result)
        if detected_objects:
            if result:
                content = ContentFile(encoded_img.tobytes(), f'processed_{image_feed.image.name}')
                # image_feed.processed_image.save(content.name, content, save=True)
                detected_objects.method_detected = 'Caffe'
                detected_objects.processed_image.save(content.name, content, save=True)

        return True

    except ImageFeed.DoesNotExist:
        print("ImageFeed not found.")
        return False


def process_image_detr(image_feed_id):
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
            content = ContentFile(encoded_img.tobytes(), f'processed_{image_feed.image.name}')
            # image_feed.processed_image.save(content.name, content, save=True)
            detected_objects.method_detected = 'Torch'
            detected_objects.processed_image.save(content.name, content, save=True)

    return True


def get_graph():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y, type_graph):

    # plt.style.use('_mpl-gallery')
    plt.switch_backend('AGG')
    # plt.figure(figsize=(15, 5))
    if type_graph == 'bar':
        plt.subplot(1, 1, 1)
        plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    elif type_graph == 'line':
        plt.subplot(1, 2, 1)
        plt.plot(x, y)
    # elif type_graph == 'pie':
    #     plt.pie(x, labels=y, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.yscale('log')
    plt.title("График")
    plt.xlabel('Объекты', fontsize=12)
    plt.ylabel('Вероятность', fontsize=12)
    plt.tight_layout()
    plt.savefig(type_graph + '.png')

    return get_graph()


def get_plot_stat(x, y, type_graph):
    # plt.style.use('_mpl-gallery')
    plt.switch_backend('AGG')
    # plt.figure(figsize=(15, 5))
    plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    plt.yscale('log')
    plt.title("График")
    plt.xlabel('Метод', fontsize=12)
    plt.ylabel('Количество', fontsize=12)
    plt.savefig(type_graph + '.png')

    return get_graph()
