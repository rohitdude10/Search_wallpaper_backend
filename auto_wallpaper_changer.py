import requests
import os

folder_path = "/home/rohit/Documents/auto_wallpaper/backend/downloaded_images/"
max_size_mb = 100


def get_folder_size():
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def clear_folder():
    folder_size = get_folder_size()
    max_size_bytes = max_size_mb * 1024 * 1024

    if folder_size > max_size_bytes:
        print(
            f"Folder size ({folder_size / (1024 * 1024):.2f} MB) exceeds the limit of {max_size_mb} MB.")

        # Clear the files in the folder
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)

        print("Files cleared successfully.")
    else:
        print(
            f"Folder size ({folder_size / (1024 * 1024):.2f} MB) is within the limit of {max_size_mb} MB.")


def set_wallpaper(image_path):

    # Command to set the wallpaper using gsettings
    command = f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}"
    # gsettings get org.gnome.desktop.background picture-uri

    print(f"image path :{image_path}")
    try:
        os.system(command)
        print("Wallpaper set successfully.")
    except Exception as e:
        print("An error occurred while setting the wallpaper:", e)


def download_image_from_url(url, file_name):

    file_path = folder_path + str(file_name) + ".jpg"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any request errors

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Image downloaded successfully and saved as '{file_name}'.")
        set_wallpaper(file_path)
    except requests.exceptions.RequestException as e:
        print("An error occurred while downloading the image:", e)


def start_process(theme):
    clear_folder()

    api_url = 'https://api.pexels.com/v1/search'

    # theme= random.choice(constant.TOPICS)

    params = {
        'orientation': 'landscape',
        'size': 'large',
        'per_page': '8',
        'query': f'{theme}'
        # Add more parameters as needed
    }

    try:
        print(f"call api using options {params}")
        headers = {'Authorization': os.environ["AUTH_TOKEN"]}
        response = requests.get(api_url, params=params, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data as needed
            print("API response:", data)
            # image_url= data["photos"][0]["src"]["original"]
            # name= data["photos"][0]["id"]
            # download_image_from_url(image_url,name)
            return data

        else:
            print("Failed to fetch data from the API. Status code:",
                  response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while calling the API:", e)


def get_next_page_data(next_page_url):

    try:
        headers = {'Authorization': os.environ["AUTH_TOKEN"]}
        response = requests.get(next_page_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data as needed
            print("API response:", data)
            # image_url= data["photos"][0]["src"]["original"]
            # name= data["photos"][0]["id"]
            # download_image_from_url(image_url,name)
            return data

        else:
            print("Failed to fetch data from the API. Status code:",
                  response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while calling the API:", e)


def get_prev_page_data(next_page_url):

    try:
        headers = {'Authorization': os.environ["AUTH_TOKEN"]}
        response = requests.get(next_page_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Process the data as needed
            print("API response:", data)
            # image_url= data["photos"][0]["src"]["original"]
            # name= data["photos"][0]["id"]
            # download_image_from_url(image_url,name)
            return data

        else:
            print("Failed to fetch data from the API. Status code:",
                  response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while calling the API:", e)

