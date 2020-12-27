from matplotlib import image
from matplotlib import pyplot
from sklearn.cluster import KMeans
import numpy as np

def compress1(k):
    print("Compressing the image ... ")
    # Compress the image using k-means clustering
    kMeans = KMeans(n_clusters=k).fit(reshape_img)
    compressed_img = kMeans.cluster_centers_[kMeans.labels_]
    compressed_img = np.clip(compressed_img.astype(img.dtype), 0, 255)

    # Reshape the image to its original dimension
    compressed_img = compressed_img.reshape(imgDm[0], imgDm[1], imgDm[2])

    # Show the compressed image
    pyplot.imshow(compressed_img)
    pyplot.show()

def compress2(clusters, columns, rows):
    fig = pyplot.figure(figsize=(10, 25))
    ax = []
    num = 0
    print("Compressing images ... ")
    for i in range(columns * rows):
        if i == 0:
            ax.append(fig.add_subplot(rows, columns, i + 1))
            ax[-1].set_title("Original Image")
            pyplot.imshow(img)
        else:
            k = clusters[num]  # the number of clusters in the i-th image
            kMeans = KMeans(n_clusters=k).fit(reshape_img)
            compressed_img = kMeans.cluster_centers_[kMeans.labels_]
            compressed_img = np.clip(compressed_img.astype(img.dtype), 0, 255)
            compressed_img = compressed_img.reshape(imgDm[0], imgDm[1], imgDm[2])

            ax.append(fig.add_subplot(rows, columns, i + 1))
            ax[-1].set_title("k-Means Clustering of " + str(k) + " Colours")
            pyplot.imshow(compressed_img)
            num += 1
    pyplot.show()

print("Save your image to compress in your directory as Image.jpg.\n . . . \n")
while True:
    AskWhichPlot = int(input("Would you like to obtain a compressed image (1) "
                         "or an original with compressed images side by side (2)? (choose 1 or 2)\n"))

    img = image.imread('Image.jpg')     # Read the image
    imgDm = img.shape
    reshape_img = img.reshape(imgDm[0] * imgDm[1], imgDm[2])

    if AskWhichPlot == 1:
        AskColour = int(input("Reduce the number of colours in the image to: "))
        compress1(AskColour)
        break
    elif AskWhichPlot == 2:
        columns = int(input("Number of columns in the plot: "))
        rows = int(input("Number of rows in the plot: "))
        clusters = []
        for i in range(1, columns*rows):
            AskColour = int(input("Reduce the number of colours in the "+ str(i) + ". image to: "))
            clusters.append(AskColour)
        compress2(clusters, columns, rows)
        break
    else:
        pass
print("Successfully compressed image(s).")