from PIL import Image, ImageDraw, ImageFont
import re

# Configuration
css_file = '/home/volse/Nextcloud/Documents/hackdornfish/hackdornfish_dark.css'
output_file = '/home/volse/Nextcloud/Documents/hackdornfish/hackdornfish_dark.png'  # Output PNG file
box_size = (25, 25)  # Box size in mm
box_spacing = 5  # Spacing between boxes in mm
line_spacing = 5  # Spacing between lines in mm
font_size = 12  # Font size for the text
font_file = '/home/volse/Nextcloud/Alles_nur_geCloud/Miscellaneous/Fonts/Inter/static/Inter-Regular.ttf'

# Read CSS file
css_data = {}
with open(css_file, 'r') as file:
    lines = file.readlines()

# Remove lines that start with comments
lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('//')]

# Extract color definitions and line breaks
color_regex = r'@define-color (\w+)\s+(#[0-9a-fA-F]{6});'
box_lines = [[]]
for line in lines:
    match = re.match(color_regex, line)
    if match:
        class_name, color = match.groups()
        box_lines[-1].append((class_name, color))
    else:
        # Empty line encountered, start a new line of boxes
        box_lines.append([])

# Calculate the size of the final image
num_lines = len(box_lines)
max_boxes_per_line = max(len(line) for line in box_lines)
total_width = max_boxes_per_line * box_size[0] + (max_boxes_per_line - 1) * box_spacing
total_height = num_lines * box_size[1] + (num_lines - 1) * line_spacing

# Create a new image
image = Image.new('RGB', (total_width, total_height), color='white')
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_file, font_size)

# Iterate over the box lines and draw the boxes
y = 0
for line in box_lines:
    x = 0
    for class_name, color in line:
        # Draw the box
        box_coords = (x, y, x + box_size[0], y + box_size[1])
        draw.rectangle(box_coords, fill=color, outline='black')

        # Draw the text
        text = f'{class_name}\n{color}'
        text_width, text_height = draw.textsize(text, font=font)
        text_coords = (x + (box_size[0] - text_width) // 2, y + (box_size[1] - text_height) // 2)
        draw.text(text_coords, text, fill='white', font=font)

        x += box_size[0] + box_spacing
    y += box_size[1] + line_spacing

# Save the image
image.save(output_file)
