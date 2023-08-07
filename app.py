import gradio as gr
import re
from extract import extract_slides
from imgpdf import convert_jpg_to_pdf
def get_filename_without_ext(file_path):
    match = re.search(r'([^/\\]+)(?=\.)', file_path)
    if match:
        return match.group(1)

def upload_file(files, threshold):
    if files:
        files = list(files)
        file_path = files[0].name
        print(file_path,threshold)
        
        folder_path=extract_slides(file_path, threshold)
        file=convert_jpg_to_pdf(folder_path, 'output.pdf')
        return file
    else:
        raise Exception("Please upload a video file.")

demo = gr.Interface(
    upload_file,
    inputs= [gr.File(file_count="multiple", file_types=["video"]),
    gr.Slider(0, 100, label="Threshold")],outputs="file"
)


demo.launch()
