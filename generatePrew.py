from PIL import Image, ImageDraw, ImageFont

# Configuration
css_file = 'styles.css'  # Path to the CSS file
output_file = 'boxes.png'  # Output PNG file
box_size = (25, 25)  # Box size in mm
box_spacing = 5  # Spacing between boxes in mm
font_size = 12  # Font size for the text
font_file = 'arial.ttf'  # Path to the font file

# Read CSS file
css_data = {}
with open(css_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith('.'):
            class_name, color = line.split('{')[0].strip('.'), line.split(':')[1].strip()
            css_data[class_name] = color

# Calculate the size of the final image
num_boxes = len(css_data)
total_width = num_boxes * box_size[0] + (num_boxes - 1) * box_spacing
total_height = box_size[1]

# Create a new image
image = Image.new('RGB', (total_width, total_height), color='white')
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_file, font_size)

# Iterate over the CSS data and draw the boxes
x = 0
for class_name, color in css_data.items():
    # Draw the box
    box_coords = (x, 0, x + box_size[0], box_size[1])
    draw.rectangle(box_coords, fill=color, outline='black')

    # Draw the text
    text = f'{class_name}\n{color}'
    text_width, text_height = draw.textsize(text, font=font)
    text_coords = (x + (box_size[0] - text_width) // 2, (box_size[1] - text_height) // 2)
    draw.text(text_coords, text, fill='white', font=font)

    x += box_size[0] + box_spacing

# Save the image
image.save(output_file)
from PIL import Image, ImageDraw, ImageFont
import re

# Configuration
css_file = 'styles.css'  # Path to the CSS file
output_file = 'boxes.png'  # Output PNG file
box_size = (25, 25)  # Box size in mm
box_spacing = 5  # Spacing between boxes in mm
font_size = 12  # Font size for the text
font_file = 'arial.ttf'  # Path to the font file

# Read CSS file
css_data = {}
with open(css_file, 'r') as file:
    lines = file.readlines()

# Remove lines that start with comments or empty lines
lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('//')]

# Extract color definitions
color_regex = r'@define-color (\w+)\s+(#[0-9a-fA-F]{6});'
for line in lines:
    match = re.match(color_regex, line)
    if match:
        class_name, color = match.groups()
        css_data[class_name] = color

# Calculate the size of the final image
num_boxes = len(css_data)
total_width = num_boxes * box_size[0] + (num_boxes - 1) * box_spacing
total_height = box_size[1]

# Create a new image
image = Image.new('RGB', (total_width, total_height), color='white')
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_file, font_size)

# Iterate over the CSS data and draw the boxes
x = 0
for class_name, color in css_data.items():
    # Draw the box
    box_coords = (x, 0, x + box_size[0], box_size[1])
    draw.rectangle(box_coords, fill=color, outline='black')

    # Draw the text
    text = f'{class_name}\n{color}'
    text_width, text_height = draw.textsize(text, font=font)
    text_coords = (x + (box_size[0] - text_width) // 2, (box_size[1] - text_height) // 2)
    draw.text(text_coords, text, fill='white', font=font)

    x += box_size[0] + box_spacing

# Save the image
image.save(output_file)
