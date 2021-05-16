import time
import concurrent.futures
from PIL import Image, ImageFilter


def process_image(img_url):
    size = (1200, 1200)
    img = Image.open(img_url)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_url}')
    return (f'{img_url} was processed...')


def process_images(img_urls):
    for img_url in img_urls:
        result = process_image(img_url)
        print(result)


def process_images_multiprocessing(img_urls):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_image, img_urls)

        for result in results:
            print(result)


if __name__ == '__main__':
    img_urls = [
        'photo (1).jpg',
        'photo (2).jpg',
        'photo (3).jpg',
        'photo (4).jpg',
        'photo (5).jpg',
        'photo (6).jpg',
        'photo (7).jpg',
        'photo (8).jpg',
        'photo (9).jpg',
        'photo (10).jpg',
        'photo (11).jpg',
        'photo (12).jpg',
        'photo (13).jpg',
        'photo (14).jpg',
        'photo (15).jpg'
    ]

    start = time.perf_counter()
    process_images(img_urls)
    finish = time.perf_counter()
    time_taken = round(finish-start)

    start = time.perf_counter()
    process_images_multiprocessing(img_urls)
    finish = time.perf_counter()
    time_taken_multiprocessing = round(finish-start)

    print(f"Completed process in {time_taken} second(s).")
    print(
        f"Completed process with multiprocessing in {time_taken_multiprocessing} second(s).")
