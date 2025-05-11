import instaloader
import os
import tempfile
import shutil

def download_instagram_video(url):
    try:
        shortcode = url.strip("/").split("/")[-1]
        loader = instaloader.Instaloader(
            save_metadata=False,
            download_comments=False,
            post_metadata_txt_pattern=""
        )

        # Load login session
        loader.load_session_from_file("viewer_session.json")

        temp_dir = tempfile.mkdtemp()
        target_folder = "downloaded_post"
        loader.dirname_pattern = os.path.join(temp_dir, "{target}")

        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=target_folder)

        post_path = os.path.join(temp_dir, target_folder)
        for file in os.listdir(post_path):
            if file.endswith(".mp4"):
                return os.path.join(post_path, file)

        return None

    except Exception as e:
        print("Download error:", e)
        return None
