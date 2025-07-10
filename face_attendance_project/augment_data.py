import cv2
import os
import numpy as np

def augment_image(image):
    aug_imgs = []

    # Flip horizontally
    aug_imgs.append(cv2.flip(image, 1))

    # Rotate slightly
    for angle in [-15, 15]:
        h, w = image.shape
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
        rotated = cv2.warpAffine(image, M, (w, h))
        aug_imgs.append(rotated)

    # Brightness adjustment
    for factor in [0.8, 1.2]:  # Darker, brighter
        bright = np.clip(image * factor, 0, 255).astype(np.uint8)
        aug_imgs.append(bright)

    return aug_imgs

def augment_dataset(data_dir="data/train"):
    for label in os.listdir(data_dir):
        person_dir = os.path.join(data_dir, label)
        if not os.path.isdir(person_dir):
            continue

        print(f"📂 Augmenting for: {label}")
        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue

            aug_images = augment_image(img)

            # Save augmented images
            for i, aug in enumerate(aug_images):
                out_path = os.path.join(person_dir, f"{img_name.split('.')[0]}_aug{i}.jpg")
                cv2.imwrite(out_path, aug)

        print(f"✅ Done: {label}")

if __name__ == "__main__":
    augment_dataset()
