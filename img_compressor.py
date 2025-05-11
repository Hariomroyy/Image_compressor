import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def compress_and_show_image():
    image_path = "deadpool.jpg"
    img = cv2.imread(image_path)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pixels = img_rgb.reshape(-1, 3)

    n_colors = max(1, int(len(np.unique(pixels, axis=0)) * 0.09))
    kmeans = KMeans(n_clusters=n_colors, random_state=0, n_init=10)
    labels = kmeans.fit_predict(pixels)
    compressed_pixels = kmeans.cluster_centers_.astype("uint8")[labels]

    compressed_img = compressed_pixels.reshape(img_rgb.shape)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img_rgb)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title(f"Compressed Image ({n_colors} colors)")
    plt.imshow(compressed_img)

    plt.tight_layout()
    plt.show()

compress_and_show_image()
