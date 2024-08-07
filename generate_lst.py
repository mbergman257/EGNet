import os
from dataset import ROOT

def generate_lst_file(image_dir, lst_filename):
    """
    Generate a .lst file from image files in the given directory.
    
    Parameters:
    - image_dir: Path to the directory containing the image files.
    - lst_filename: Name of the output .lst file.
    """
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
    
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_extensions]

    # Sort the list to ensure consistent order
    image_files.sort()

    # Write the image file paths to the .lst file
    with open(lst_filename, 'w') as f:
        for image_file in image_files:
            f.write(os.path.join(image_dir, image_file) + '\n')

    print(f"{lst_filename} has been generated with {len(image_files)} entries.")

# Example usage
# Train
image_directory = ROOT + '/yolov8/datasets/coco/images/train2017'
output_lst_file = ROOT + '/EGNet/coco_train2017.lst'
generate_lst_file(image_directory, output_lst_file)
# Val
image_directory = ROOT + '/yolov8/datasets/coco/images/val2017'
output_lst_file = ROOT + '/EGNet/coco_val2017.lst'
generate_lst_file(image_directory, output_lst_file)