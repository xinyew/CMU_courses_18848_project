import cv2
import os
import random


def resize(target_size:tuple, flip_rate:float=0.5, rot_rate:float=0.5, central_crop=False):
    # Get image folder and resized folder
    path = os.getcwd()
    img_folder = os.path.join(path, "img") # Raw image folder
    target_folder = os.path.join(path, "img_small") # Target folder

    if not os.path.exists(target_folder):
        os.mkdir(target_folder)

    for label in os.listdir(img_folder):

        print("Processing images with label {}".format(label))

        if label == ".DS_Store": continue # Skip mac os system file

        curr_path = os.path.join(img_folder, label)
        save_path = os.path.join(target_folder, label)
        
        if not os.path.exists(save_path): os.mkdir(save_path)

        # Image augmentations
        for i, file_name in enumerate(sorted(os.listdir(curr_path))):
            img_path = os.path.join(curr_path, file_name)
            
            if not os.path.isfile(img_path): continue

            img = cv2.imread(img_path)
            resized = cv2.resize(img, target_size)

            if central_crop:
                size = min(target_size)
                xs = [(target_size[0] - size) // 2, (target_size[0] + size) // 2]
                ys = [(target_size[1] - size) // 2, (target_size[1] + size) // 2]
                resized = resized[ys[0]:ys[1], xs[0]:xs[1]]

            cv2.imwrite(f"{save_path}/{label}_{i}.jpg", resized)
            
            # random flip
            if random.random() < flip_rate:
                cv2.imwrite(f"{save_path}/{label}_{i}_f.jpg", cv2.flip(resized, 1))
            
            # random rotation
            if random.random() < rot_rate:
                width, height = target_size
                ang = random.uniform(-10.0, 10.0)
                scale = random.uniform(1.0, 1.3)
                rot_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle=ang, scale=scale)
                if central_crop: target_size = [min(target_size)] * 2
                rot_img = cv2.warpAffine(resized, rot_matrix, dsize=(target_size))
                cv2.imwrite(f"{save_path}/{label}_{i}_r.jpg", rot_img)

    print("Processing finished!")


if __name__ == "__main__":
    output_size = (600, 400) # output image size
    flip_rate = 0.9
    rot_rate = 0.7
    resize(output_size, flip_rate, rot_rate, central_crop=True)