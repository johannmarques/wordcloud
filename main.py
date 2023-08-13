from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

# Creating a color function
def purple_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(264, 100%%, %d%%)" % random.randint(25, 65)

# Words list
words = ['Econometrics', 'Time Series', 'Forecasting',
         'Macroeconomics', 'Finance', 'Industrial Organization',
         'Soccer', 'Elastic Net', 'Data Viz', 'Urban Economics',
         'Infrastructure', 'Applied Micro', 'Risk',
         'Causal Inference', 'Development', 'Brazil',
         'Energy', 'Python', 'R', 'Public Transport']

# And the respective weights
weights = [50, 10, 20, 10, 10, 10, 15, 30, 20, 15, 10, 5, 1, 1, 1,
           15, 20, 20, 50, 5]

# Checking whether words and weights have the same length
if len(words) == len(weights) :
    print('Both vectors have same length. Everything is ok :)')
else :
    print('Ooops! words has {} entries while weights has {}'.
          format(len(words), len(weights)))

freq = {words[ii] : weights[ii] for ii in range(len(words))}

# Image for mask
gato = np.array(Image.open('gato.png'))

# Generate the cloud

wc = WordCloud(background_color="rgba(255, 255, 255, 0)", mode="RGBA",
               mask = gato, random_state = 3)
wc.generate_from_frequencies(freq)

# Display the generated image:
plt.imshow(wc.recolor(color_func=purple_color_func, random_state=3),
           interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file('wordcloud.png')