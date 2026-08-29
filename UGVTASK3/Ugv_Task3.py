
import cv2
import numpy as np
import os

INPUT_IMAGE_PATH = "UGVTASK3/Input Image 3/10.png"     
OUTPUT_IMAGE_PATH = "output10.jpg"


WHITE_LOWER = np.array([0,   0,   170])
WHITE_UPPER = np.array([179, 60,  255])


YELLOW_LOWER = np.array([18, 90, 90])
YELLOW_UPPER = np.array([35, 255, 255])


GREEN_LOWER = np.array([36, 60, 60])
GREEN_UPPER = np.array([85, 255, 255])


MORPH_KERNEL_SIZE = (5, 5)


MIN_CONTOUR_AREA = 300
MAX_CONTOUR_AREA_FRACTION = 0.25 

MIN_CIRCULARITY_FOR_WHITE = 0.35
MAX_ASPECT_RATIO_FOR_WHITE = 2.5  
DEDUPLICATION_DISTANCE = 20


BOX_COLOR = (0, 0, 255)        
BOX_THICKNESS = 2
TEXT_COLOR = (0, 255, 0)       
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.45
FONT_THICKNESS = 1


def build_mask(hsv_image, lower, upper):

    mask = cv2.inRange(hsv_image, lower, upper)

    kernel = np.ones(MORPH_KERNEL_SIZE, np.uint8)
 
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    return mask


def get_valid_contours(mask, image_area, shape_filter=False):
   
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    valid_contours = []
    max_area = image_area * MAX_CONTOUR_AREA_FRACTION

    for cnt in contours:
        area = cv2.contourArea(cnt)

        
        if area < MIN_CONTOUR_AREA or area > max_area:
            continue

        if shape_filter:
            perimeter = cv2.arcLength(cnt, True)
            if perimeter == 0:
                continue

            circularity = 4 * np.pi * area / (perimeter ** 2)

            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = max(w, h) / float(min(w, h))

            
            if circularity < MIN_CIRCULARITY_FOR_WHITE and \
               aspect_ratio > MAX_ASPECT_RATIO_FOR_WHITE:
                continue

        valid_contours.append(cnt)

    return valid_contours


def contours_to_boxes(contours, label):
    """Convert a list of contours into bounding-box dictionaries."""
    boxes = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cx, cy = x + w // 2, y + h // 2
        boxes.append({
            "label": label,
            "x": x, "y": y, "w": w, "h": h,
            "cx": cx, "cy": cy
        })
    return boxes


def deduplicate_boxes(boxes):
    
    unique_boxes = []

    for box in boxes:
        is_duplicate = False
        for kept in unique_boxes:
            dist = np.hypot(box["cx"] - kept["cx"], box["cy"] - kept["cy"])
            if dist < DEDUPLICATION_DISTANCE:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_boxes.append(box)

    return unique_boxes


def draw_detections(image, boxes):

    for i, box in enumerate(boxes, start=1):
        x, y, w, h = box["x"], box["y"], box["w"], box["h"]
        cx, cy = box["cx"], box["cy"]

     
        cv2.rectangle(image, (x, y), (x + w, y + h), BOX_COLOR, BOX_THICKNESS)

        cv2.circle(image, (cx, cy), 3, TEXT_COLOR, -1)

        label_text = f"#{i} {box['label']}"
        coord_text = f"({x},{y}) {w}x{h} c=({cx},{cy})"

        text_y = y - 8 if y - 8 > 10 else y + h + 15
        cv2.putText(image, label_text, (x, text_y),
                    FONT, FONT_SCALE, TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)
        cv2.putText(image, coord_text, (x, text_y + 14),
                    FONT, FONT_SCALE, TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return image



def detect_potholes_and_obstacles(image_path, output_path):
    
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not read image at: {image_path}")

    output_image = image.copy()
    image_area = image.shape[0] * image.shape[1]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    white_mask = build_mask(hsv, WHITE_LOWER, WHITE_UPPER)
    yellow_mask = build_mask(hsv, YELLOW_LOWER, YELLOW_UPPER)
    green_mask = build_mask(hsv, GREEN_LOWER, GREEN_UPPER)

    white_contours = get_valid_contours(white_mask, image_area, shape_filter=True)
    yellow_contours = get_valid_contours(yellow_mask, image_area, shape_filter=False)
    green_contours = get_valid_contours(green_mask, image_area, shape_filter=False)

    all_boxes = []
    all_boxes += contours_to_boxes(white_contours, "Object")
    all_boxes += contours_to_boxes(yellow_contours, "Object")
    all_boxes += contours_to_boxes(green_contours, "Object")

    all_boxes = deduplicate_boxes(all_boxes)
    output_image = draw_detections(output_image, all_boxes)

    count_text = f"Total Detected: {len(all_boxes)}"
    cv2.putText(output_image, count_text, (15, 30),
                FONT, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

    print(f"\nTotal objects detected: {len(all_boxes)}\n")
    for i, box in enumerate(all_boxes, start=1):
        print(f"Object #{i}:")
        print(f"  Top-left (x, y): ({box['x']}, {box['y']})")
        print(f"  Width x Height : {box['w']} x {box['h']}")
        print(f"  Center (cx, cy): ({box['cx']}, {box['cy']})")
        print("-" * 40)
    cv2.imwrite(output_path, output_image)
    print(f"\nAnnotated image saved to: {output_path}")

    return all_boxes, output_image

if __name__ == "__main__":
    if not os.path.exists(INPUT_IMAGE_PATH):
        print(f"Input image not found at '{INPUT_IMAGE_PATH}'.")
        print("Update INPUT_IMAGE_PATH at the top of this script.")
    else:
        detect_potholes_and_obstacles(INPUT_IMAGE_PATH, OUTPUT_IMAGE_PATH)