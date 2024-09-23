import matplotlib.pyplot as plt

def show_image(image, title='Image'):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_singular_values(S, title='Singular Values'):
    plt.plot(range(1, len(S) + 1), S)
    plt.xlabel('Singular Value Index')
    plt.ylabel('Singular Value')
    plt.title(title)
    plt.show()

def compare_images(original, compressed, n_components):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(original, cmap='gray')
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    ax[1].imshow(compressed, cmap='gray')
    ax[1].set_title(f'Compressed Image (n={n_components})')
    ax[1].axis('off')

    plt.tight_layout()
    plt.show()
