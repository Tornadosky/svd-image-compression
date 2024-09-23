from svd_compression.image_utils import load_image, save_image, split_channels, merge_channels
from svd_compression.svd_operations import compress_color_image
from svd_compression.visualization import show_image, compare_images

def main():
    image_path = 'data/test_cat.png'
    
    # Load the image
    image = load_image(image_path, grayscale=True)
    show_image(image, title='Original Image')

    # Compression in grayscale
    n_components = 60
    U, S, Vt = compute_svd(image)
    compressed_image = reconstruct_image(U, S, Vt, n_components)
    compare_images(image, compressed_image, n_components)

    # Compression in color
    color_image = load_image(image_path, grayscale=False)
    R, G, B = split_channels(color_image)
    R_compressed, G_compressed, B_compressed = compress_color_image(R, G, B, n_components)
    compressed_color_image = merge_channels(R_compressed, G_compressed, B_compressed)
    
    show_image(compressed_color_image, title=f'Compressed Color Image (n={n_components})')

if __name__ == '__main__':
    main()
