import cv2
import numpy as np

def test_opencv():
    # 1. Print OpenCV Version
    print(f"OpenCV version successfully detected: {cv2.__version__}")
    
    # 2. Create a simple test image (300x300 pixels, blue background)
    # OpenCV uses BGR color format: (Blue, Green, Red)
    test_image = np.zeros((300, 300, 3), dtype=np.uint8)
    test_image[:] = [255, 0, 0]  # Fill with blue
    
    # 3. Draw a green circle in the center
    cv2.circle(test_image, (150, 150), 50, (0, 255, 0), -1)
    
    # 4. Display the image in a window
    print("Opening test window... Press ANY KEY to close it.")
    cv2.imshow("OpenCV Installation Test", test_image)
    
    # 5. Keep the window open until a key is pressed, then clean up
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Test completed successfully!")

if __name__ == "__main__":
    test_opencv()
