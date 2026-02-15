from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))

api.upload_folder(
    folder_path="mlops-pipelines/deployment",
    repo_id="bipjack/PIMA-Diabetes-Prediction",
    repo_type="space",
    path_in_repo=".",
)
print("Deployment pushed successfully.")
