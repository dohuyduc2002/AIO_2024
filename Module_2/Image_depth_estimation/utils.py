import cv2
import numpy as np

def l1_distance(x,y):
    return np.abs(x-y)

def l2_distance(x,y):
    return np.power(x-y,2)

def calculate_cost(left, right, x, y, j, kernel_half, max_value):
    total = 0
    value = 0

    for v in range(-kernel_half, kernel_half):
        for u in range(-kernel_half, kernel_half):
            value = max_value
            if (x + u - j) >= 0:
                value = l1_distance(int(left[y + v, x + u]), int(right[y + v, (x + u) - j]))
            total += value

    return total


def window_based_l1(left_img, right_img, disparity_range, save_name, kernel_size=5):
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)
    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]
    depth = np.zeros((height, width), np.uint8)
    kernel_half = int((kernel_size - 1) / 2)
    scale = 3
    max_value = 255 * 9

    for y in range(kernel_half, height - kernel_half + 1):
        for x in range(kernel_half, width - kernel_half + 1):
            disparity = 0
            cost_min = 65534

            for j in range(disparity_range):
                total = calculate_cost(left, right, x, y, j, kernel_half, max_value)
                if total < cost_min:
                    cost_min = total
                    disparity = j

            depth[y, x] = disparity * scale

    cv2.imwrite(f'{save_name}.png', depth)
    cv2.imwrite(f'{save_name}_l1.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))
    print('Done')
    return depth

def window_based_l2(left_img, right_img, disparity_range,save_name, kernel_size=5):
    left = cv2.imread(left_img, 0)
    right = cv2.imread(right_img, 0)
    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]
    depth = np.zeros((height,width),np.uint8)
    kernel_half = int((kernel_size - 1)/2)
    scale = 3
    max_value = 255 * 9

    for y in range(kernel_half, height - kernel_half + 1):
        for x in range(kernel_half, width - kernel_half + 1):
            disparity = 0
            cost_min = 65534

            for j in range(disparity_range):
                total = calculate_cost(left, right, x, y, j, kernel_half, max_value)
                if total < cost_min:
                    cost_min = total
                    disparity = j

            depth[y, x] = disparity * scale
    
    print('Saving result')
    cv2.imwrite(f'{save_name}.png',depth)
    cv2.imwrite(f'{save_name}_l1.png',cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print('Done')
    return depth
                        
def pixel_based_l1(left_img, right_img, disparity_range, save_result = True):
    # Read left image and right image as grayscale
    left = cv2.imread(left_img, cv2.IMREAD_GRAYSCALE)
    right = cv2.imread(right_img, cv2.IMREAD_GRAYSCALE)

    # Convert to float32 to calculate disparity
    left = left.astype(np.float32)
    right = right.astype(np.float32)

    # Retrieve height and width to instantiate zeros disparity matrix
    height, width = left.shape
    scale = 16 # Changeable, higher scale will make img brighter
    max_value = 255
    cost_volume = np.full((disparity_range, height, width), max_value, dtype=np.float32)
    
    for d in range(disparity_range):
        # Shift the right image
        right_shifted = np.pad(right, ((0, 0), (d, 0)), mode='constant', constant_values=max_value)[:, :width]
        
        # Calculate L1 distance
        cost_volume[d] = l1_distance(left, right_shifted)

    # Find the minimum cost and corresponding disparity
    depth = np.argmin(cost_volume, axis=0) * scale
    depth = depth.astype(np.uint8)
    
    if save_result:
        print('Saving result...')
        cv2.imwrite('pixel_wise_l1.png', depth)
        cv2.imwrite('pixel_wise_color_l1.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))
    
    print('Done')
    return depth

def pixel_based_l2(left_img, right_img, disparity_range, save_result = True):
    # Read left image and right image as grayscale
    left = cv2.imread(left_img, cv2.IMREAD_GRAYSCALE)
    right = cv2.imread(right_img, cv2.IMREAD_GRAYSCALE)

    # Convert to float32 to calculate disparity
    left = left.astype(np.float32)
    right = right.astype(np.float32)

    # Retrieve height and width to instantiate zeros disparity matrix
    height, width = left.shape
    scale = 16 # Changeable, higher scale will make img brighter
    max_value = 255
    cost_volume = np.full((disparity_range, height, width), max_value, dtype=np.float32)
    
    for d in range(disparity_range):
        # Shift the right image
        right_shifted = np.pad(right, ((0, 0), (d, 0)), mode='constant', constant_values=max_value)[:, :width]
        
        # Calculate L1 distance
        cost_volume[d] = l2_distance(left, right_shifted)

    # Find the minimum cost and corresponding disparity
    depth = np.argmin(cost_volume, axis=0) * scale
    depth = depth.astype(np.uint8)
    
    if save_result:
        print('Saving result...')
        cv2.imwrite('pixel_wise_l2.png', depth)
        cv2.imwrite('pixel_wise_color_l2.png', cv2.applyColorMap(depth, cv2.COLORMAP_JET))
    
    print('Done')
    return depth

def cosine_similarity(x,y):
    return np.dot(x,y) / (np.linalg.norm(x) * np.linalg.norm(y))

def window_base_matching_cosine(left_img, right_img, disparity_range,save_name, kernel_size = 5):
    left = cv2.imread(left_img,0)
    right = cv2.imread(right_img,0)

    left = left.astype(np.float32)
    right = right.astype(np.float32)

    height, width = left.shape[:2]

    depth = np.zeros((height,width),np.uint8) 
    kernel_half = int((kernel_size - 1) /2)
    scale = 3 

    for y in range(kernel_half, height-kernel_half):
        for x in range(kernel_half, width - kernel_half):
            disparity = 0 
            cost_optimal = -1

            for j in range(disparity_range):
                d = x - j
                cost = -1
                if (d - kernel_half) > 0:
                    wp = left[(y - kernel_half) : (y+kernel_half) + 1, (x-kernel_half):(x+kernel_half)+1]
                    wqd = right[(y - kernel_half) : (y+kernel_half)+1, (d-kernel_half):(d+kernel_half)+1]

                    wp_flattened = wp.flatten()
                    wqd_flattend = wqd.flatten()
                    cost = cosine_similarity(wp_flattened,wqd_flattend)
                
                if cost > cost_optimal:
                    cost_optimal = cost 
                    disparity = j
                    depth[y,x] = disparity * scale
    cv2.imwrite(f'{save_name}.png',depth)
    cv2.imwrite(f'{save_name}_color.png',cv2.applyColorMap(depth,cv2.COLORMAP_JET))
    print('Done')
    return depth