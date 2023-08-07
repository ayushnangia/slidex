import os
import img2pdf

def convert_jpg_to_pdf(folder_path, output_file_path):
  """Converts all .jpg files in the specified folder to one PDF file.

  Args:
    folder_path: The path to the folder containing the .jpg files.
    output_file_path: The path to the output PDF file.
  """

  # Get a list of image file paths and sort it alphabetically
  image_files = sorted([os.path.join(folder_path, i) for i in os.listdir(folder_path) if i.endswith(".jpg")])

  # Convert images to pdf and write to file
  with open(output_file_path, "wb") as f:
    f.write(img2pdf.convert(image_files))  # Pass the list of image file paths
  return output_file_path

