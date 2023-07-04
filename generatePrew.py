from PIL import Image, ImageDraw, ImageFont
import re

# Configuration
css_file = '/home/volse/Nextcloud/Documents/hackdornfish/hackdornfish_light.css'
output_file = '/home/volse/Nextcloud/Documents/hackdornfish/hackdornfish_light.png'  # Output PNG file
box_size = (75, 75)  # Box size in mm
box_spacing = 5  # Spacing between boxes in mm
line_spacing = 5  # Spacing between lines in mm
font_size = 12  # Font size for the text
font_file = '/home/volse/Nextcloud/Alles_nur_geCloud/Miscellaneous/Fonts/Inter/static/Inter-Regular.ttf'

# Read CSS file
css_data = {}
with open(css_file, 'r') as file:
    lines = file.readlines()

# Extract color definitions and group them by lines
color_regex = r'@define-color (\w+)\s+(#[0-9a-fA-F]{6});'
current_line = []
lines_with_colors = []
for line in lines:
    match = re.match(color_regex, line)
    if match:
        current_line.append(match.groups())
    elif not current_line:
        continue  # Skip lines until we find the first color definition
    else:
        lines_with_colors.append(current_line)
        current_line = []
# Append the last line if it contains colors
if current_line:
    lines_with_colors.append(current_line)

# Determine font color based on CSS file name
css_file_name = css_file.split('/')[-1].lower()
if 'dark' in css_file_name:
    font_color_main = 'white'
    font_color_sec = 'black'

else:
    font_color_main = 'black'
    font_color_sec = 'white'

# Calculate the size of the final image
num_lines = len(lines_with_colors)
total_width = max(len(line) for line in lines_with_colors) * (box_size[0] + box_spacing)
total_height = num_lines * (box_size[1] + line_spacing)

# Create a new image
image = Image.new('RGB', (total_width, total_height), color='white')
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_file, font_size)

# Iterate over the lines and draw the boxes
y = 0
for line in lines_with_colors:
    x = 0
    for class_name, color in line:

        # Determine font color based on class name
        if 'bg' in class_name or 'sec' in class_name:
                font_color = font_color_main
        else:
                font_color = font_color_sec

        # Draw the box
        box_coords = (x, y, x + box_size[0], y + box_size[1])
        draw.rectangle(box_coords, fill=color, outline='black')

        # Write the text
        text = f'{class_name}\n{color}'
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_coords = ((box_size[0] - text_bbox[2]) // 2, (box_size[1] - text_bbox[3]) // 2)
        draw.text((x + text_coords[0], y + text_coords[1]), text, fill=font_color, font=font)

        x += box_size[0] + box_spacing
    y += box_size[1] + line_spacing

# Save the image
image.save(output_file)

