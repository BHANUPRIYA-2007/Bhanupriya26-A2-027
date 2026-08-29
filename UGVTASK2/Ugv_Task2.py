import matplotlib.pylab as plt
import cv2
import numpy as np

img = cv2.imread('UGVTASK2/Input Image 2/1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img.shape[:2]

pts = np.array([[
    (50, h - 80),
    (int(w * 0.25), int(h * 0.55)),
    (int(w * 0.58), int(h * 0.55)),
    (w - 100, h - 80)
]], dtype=np.int32)

def get_roi(image, vertices):
    mask = np.zeros_like(image)
    color = 255 if len(image.shape) == 2 else (255,) * image.shape[2]
    cv2.fillPoly(mask, vertices, color)
    return cv2.bitwise_and(image, mask)

def get_coords(image, line_params):
    slope, intercept = line_params
    y1 = int(image.shape[0] - 80)
    y2 = int(image.shape[0] * 0.55)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return [x1, y1, x2, y2]

def avg_lines(image, lines):
    left = []
    right = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.flatten()
            if x1 == x2:
                continue
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            if -1.5 < m < -0.3:
                left.append((m, b))
            elif 0.3 < m < 1.5:
                right.append((m, b))
    
    final = []
    if len(left) > 0:
        final.append(get_coords(image, np.average(left, axis=0)))
    if len(right) > 0:
        final.append(get_coords(image, np.average(right, axis=0)))
    return final

def draw_lines(image, lines):
    blank = np.zeros_like(image)
    for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(blank, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)
    return cv2.addWeighted(image, 0.8, blank, 1.0, 0.0)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray, 80, 180)
roi = get_roi(edges, pts)

segs = cv2.HoughLinesP(
    roi, rho=2, theta=np.pi/180, threshold=45,
    lines=np.array([]), minLineLength=35, maxLineGap=100
)

lanes = avg_lines(img, segs)
output = draw_lines(img, lanes)

# Save the final image to your directory (converted back to BGR for OpenCV saving)
cv2.imwrite('output1.png', cv2.cvtColor(output, cv2.COLOR_RGB2BGR))

plt.imshow(output)
plt.show()
