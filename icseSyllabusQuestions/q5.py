import numpy as nnp
from matplotlib import pyplot as plt
import skimage

image = skimage.data.astronaut()

plt.imshow(image)
plt.axis('off')
plt.title('Gigachad')
plt.show()

print(type(image))
print(image.shape)