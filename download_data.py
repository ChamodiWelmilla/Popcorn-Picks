import gdown


def download_file(file_id, output_name):
    """
    Download a file from Google Drive using its file ID.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading {output_name}...")
    gdown.download(url, output_name, quiet=False)
    print(f"Saved as {output_name}")


if __name__ == "__main__":
    files_to_download = {
        "movies_list.pkl": "1EsRm8PJmNndVBWAxZVknsfs9_C-zqfCe",
        "similarity.pkl": "1jC6u5kxXnEuZjgrRmVsp8KowIUVeT1_e",
    }

    for output_name, file_id in files_to_download.items():
        download_file(file_id, output_name)
