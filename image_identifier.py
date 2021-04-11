from imageai.Detection import ObjectDetection
import os
from decouple import config


def getImageName():
    image_name = ''
    for subdir, dirs, files in os.walk('test_images'):
        image_name = files[-1]
    return image_name


def getDetectedObjects():
    execution_path = os.getcwd()
    detected_objects = []

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(
        os.path.join(execution_path, 'model/resnet50_coco_best_v2.1.0.h5'))
    detector.loadModel()

    detections = detector.detectObjectsFromImage(
        input_image=os.path.join(
            execution_path,
            f"{config('IMG_DIR')}/image.{getImageName().split('.')[-1]}"),
        output_image_path=os.path.join(
            execution_path,
            f"{config('IMG_DIR')}/result.{getImageName().split('.')[-1]}"))

    os.remove(
        os.path.join(execution_path,
                     f"{config('IMG_DIR')}/result.{getImageName().split('.')[-1]}"))
    os.remove(
        os.path.join(execution_path,
                     f"{config('IMG_DIR')}/image.{getImageName().split('.')[-1]}"))

    for eachObject in detections:
        detected_objects.append({
            'object_name':
            eachObject["name"],
            'percentage_probability':
            eachObject["percentage_probability"]
        })

    return detected_objects


if __name__ == '__main__':
    print(getDetectedObjects())