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
        print(file_path, threshold)
        
        folder_path=extract_slides(file_path, threshold)
        file=convert_jpg_to_pdf(folder_path, 'output.pdf')
        return file
    else:
        raise Exception("Please upload a video file.")

with gr.Blocks() as demo:
    # Add some Markdown text to the top of the app.
    gr.Markdown("""
    
    # Video to PDF
    
    """)
    gr.Markdown("""
    ### Instructions
    """)
    gr.Markdown("""
Upload a video file from which to extract slides.\n
Adjust the Threshold slider to optimize slide extraction. A higher threshold will result in fewer extracted slides.\n
Press Submit to begin the extraction and conversion to PDF.    """)

    # Add the file input and slider.
    files = gr.File(file_count="multiple", file_types=["video"])
    threshold = gr.Slider(0, 100, label="Threshold")

    # Add the button that triggers the upload_file function.
    button = gr.Button("Convert")
    button.click(upload_file, inputs=[files,threshold], outputs=gr.File())


    demo.launch()
