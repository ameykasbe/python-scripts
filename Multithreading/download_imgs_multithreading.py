import requests
import time
import concurrent.futures


def download_image(url):
    name = url.split('/')[-1]
    name = f'{name}.jpg'
    print(f"{name} downloading...")

    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as e:
        return(e)

    image_data = response.content

    with open(name, 'wb') as image:
        image.write(image_data)

    return (f"{name} downloaded.")


def download_images(img_urls):
    for url in img_urls:
        result = download_image(url)
        print(result)


def download_images_multithreading(img_urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # # Using submit and result
        # future_objects = [executor.submit(
        #     download_image, url) for url in img_urls]

        # for f in concurrent.futures.as_completed(future_objects):
        #     print(f.result())

        # Using map
        results = executor.map(download_image, img_urls)
        for result in results:
            print(result)


if __name__ == '__main__':
    img_urls = [
        'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
        'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
        'https://images.unsplash.com/photo-1524429656589-6633a470097c',
        'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
        'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
        'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
        'https://images.unsplash.com/photo-1522364723953-452d3431c267',
        'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
        'https://images.unsplash.com/photo-1507143550189-fed454f93097',
        'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
        'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
        'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
        'https://images.unsplash.com/photo-1516972810927-80185027ca84',
        'https://images.unsplash.com/photo-1550439062-609e1531270e',
        'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
    ]

    start = time.perf_counter()
    download_images(img_urls)
    finish = time.perf_counter()
    time_taken = round(finish-start)

    start = time.perf_counter()
    download_images_multithreading(img_urls)
    finish = time.perf_counter()
    time_taken_multithreading = round(finish-start)

    print(f"Completed process in {time_taken} second(s).")
    print(
        f"Completed process with multithreading in {time_taken_multithreading} second(s).")
