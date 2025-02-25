def display_image(image, title="Image"):
    import cv2
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def log_message(message):
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info(message)

def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config