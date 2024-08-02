import numpy as np

def compute_mean(x):
    x = np.array(x)
    mean = np.sum(x) / x.size
    return mean

def compute_median(x):
    size = len(x)
    x = np.sort(x)
    print(x)
    if (size % 2 == 0):
        return (x[size//2 - 1] + x[size//2]) / 2
    else:
        return x[size//2]

x = [1, 5, 4, 4, 9, 13]

def compute_std(x):
    mean = compute_mean(x)
    variance = np.sum((x - mean) ** 2) / len(x)
    return np.sqrt(variance)

def compute_correlation_coefficient(x, y):
    mean_x = compute_mean(x)
    mean_y = compute_mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))
    denumerator = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))

    correlation_coefficient = numerator / denumerator
    return correlation_coefficient


if __name__ == '__main__':
    x = [2,0,2,2,7,4,-2,5,-1,-1]
    print(compute_mean(x))

    x = [1,5,4,4,9,13]
    print(compute_median(x))

    x = [171,176,155,167,169,182]
    print(compute_std(x))

    x = np.asanyarray([-2,-5,-11,6,4,15,9])
    y = np.asanyarray([4,25,121,36,16,225,81])
    print(compute_correlation_coefficient(x,y))


