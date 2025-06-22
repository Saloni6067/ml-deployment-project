from tensorflow.keras.datasets import mnist
import imageio

# Load the test split
(_, _), (x_test, y_test) = mnist.load_data()

# Pick an example—here, the first one
img_array = x_test[0]

# Save it to digit.png
imageio.imwrite("digit.png", img_array)
print("Saved digit.png, label =", y_test[0])
