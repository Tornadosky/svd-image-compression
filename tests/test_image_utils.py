import unittest
from svd_compression.image_utils import load_image, split_channels, merge_channels

class TestImageUtils(unittest.TestCase):
    def test_load_image(self):
        image = load_image('data/test_cat.png', grayscale=True)
        self.assertEqual(len(image.shape), 2)  # Grayscale image should have 2 dimensions

    def test_split_and_merge_channels(self):
        image = load_image('data/test_cat.png')
        R, G, B = split_channels(image)
        merged_image = merge_channels(R, G, B)
        self.assertEqual(merged_image.shape, image.shape)

if __name__ == '__main__':
    unittest.main()
