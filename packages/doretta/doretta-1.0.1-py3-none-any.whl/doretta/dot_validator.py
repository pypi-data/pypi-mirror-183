import cv2
import random
import numpy as np

# Class to encapsulate the settings for detection
class DotDetectorParams():
    def __init__(self, radius: int = -1, mapping: bool = True, scaling: float = 4.0) -> None:
        self.radius = radius
        self.mapping = mapping
        self.scaling = scaling

# Class to actually perform the detection
class DotDetector():
    def __init__(self, params: DotDetectorParams=None):
        if params is None:
            self.params = DotDetectorParams()
        else:
            self.params = params
        
        self.cv2_detector = cv2.SimpleBlobDetector_create()

    def __opencv_detect__(self, image: np.ndarray) -> np.ndarray:
        keypoints = self.cv2_detector.detect(image)

        coordinates = []

        for kp in keypoints:
            if (self.params.radius != -1): 
                if (abs(self.params.radius - (kp.size/2) - 1) < 2):
                    coordinates.append(kp.pt)

            else:
                coordinates.append(kp.pt)

        return np.array(coordinates)

    def __contour_detect__(self, image: np.ndarray):
        if (len(image.shape) >= 3):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # TODO: Binarize the image for better accuracy
        predictions, heirarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        try:
            predictions = np.array(predictions)
            predictions = np.squeeze(predictions)
            predictions = np.average(predictions, axis=1)
        
        except ValueError as error:
            print("Predictions: ", predictions)
            raise ValueError

        return predictions


    def __generate_image__(self, radius: int) -> tuple:
        gen_img = np.ones((1024, 1024, 3), dtype="uint8") * 255
        coordinates = []
        
        num_points = random.randint(4, 10)

        for i in range(num_points):
            ccrd = np.random.randint(100, high=924, size=(2, ))
            coordinates.append(ccrd)
            cv2.circle(gen_img, tuple(ccrd), radius, (0, 0, 0), -1, lineType=cv2.LINE_AA)

        return gen_img, coordinates

    def __convert_to_distance__(self, center_coordinates: np.ndarray) -> np.ndarray:
        part_center = np.average(center_coordinates, axis=0)
        center_coordinates -= part_center

        return center_coordinates * self.params.scaling

    def test_module(self, episodes: int):
        print(f"Testing the OpenCV algorithm for large dots for {episodes} episodes ...")
        accuracy = 0
        errors = 0
        num_instances = 0

        for i in range(episodes):
            image, label_coordinates = self.__generate_image__(8)  
            predicted_coordinates = self.cv2_detector.detect(image) 
            predicted_array = []

            for kp in predicted_coordinates:
                predicted_array.append(kp.pt)

            predicted_array = np.array(predicted_array)

            num_detected = 0

            for ccrd in label_coordinates:
                tiled_ccrd = np.stack([ccrd] * len(predicted_coordinates))
                distances = np.linalg.norm(predicted_array - tiled_ccrd, axis=1)
                errors += min(distances)
                num_instances += 1

                if min(distances) < 10:
                    num_detected += 1

            accuracy += (num_detected / len(label_coordinates))

            if i % 100 == 0:
                print(f"Average error so far {errors / num_instances} ...")

        print(f"Accuracy for OpenCV algorithm {accuracy / episodes}")

        print(f"Testing the contour algorithm for small dots for {episodes} episodes ...")
        accuracy = 0
        errors = 0
        num_instances = 0

        for i in range(episodes):
            image, label_coordinates = self.__generate_image__(1) 

            try:
                predicted_coordinates = self.__contour_detect__(image) 

            except ValueError as error:
                print(f"Value error on episode {i}. Skipping the current episode ...")
                continue

            num_detected = 0

            for ccrd in label_coordinates:
                tiled_ccrd = np.stack([ccrd] * len(predicted_coordinates))
                distances = np.linalg.norm(predicted_coordinates - tiled_ccrd, axis=1)
                errors += min(distances)
                num_instances += 1

                if min(distances) < 10:
                    num_detected += 1

            accuracy += (num_detected / len(label_coordinates))

            if i % 100 == 0:
                print(f"Average error so far {errors / num_instances} ...")

        print(f"Accuracy for contour algorithm {accuracy / episodes}")


    def detect_dot(self, image: np.ndarray) -> np.ndarray:
        # Decide the mode of detection
        
        # If the radius is 1 then use the contour algorithm to detect the points
        if self.params.radius == 1:
            dot_coordinates = self.__contour_detect__(image)
    
        # If the radius is greater than or equal to 2, use the default contour algorithm
        else:
            dot_coordinates = self.__opencv_detect__(image)

        if self.params.mapping:
            dot_coordinates = self.__convert_to_distance__(dot_coordinates)

        return dot_coordinates