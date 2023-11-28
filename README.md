# hackdornfish
A simple color code for my desktop environment inspired by gruvbox.

## Table of Contents

[1. Concept](#sec1)\
[2. Light Mode](#sec2)\
[3. Dark Mode](#sec3)\
[4. The Python Script](#sec4)\
[5. Roadmap](#sec5)

## 1. Concept <a name="sec1"></a>   
The concept is straightforward: I use Hyprland with Waybar and some Rofi applications, and I want them to look visually appealing. The rest of the configuration is stored in a private repository to ensure no sensitive data is leaked.

As someone who enjoys working outdoors, I appreciate the ability to see my screen clearly even in bright sunlight. Therefore, I've developed a color set for both dark and light modes. My color scheme draws inspiration from [gruvbox](https://github.com/morhetz/gruvbox), a well-known and functional color scheme that provides a nice contrast.

The color names should be self-explanatory, with bg 0-4 representing background and fg 0-4 representing foreground.

## 2. Light Mode <a name="sec2"></a>
![Light mode colors](hackdornfish_light.png)

## 3. Dark Mode <a name="sec3"></a>
![Dark mode colors](hackdornfish_dark.png)

## 4. Python Script <a name="sec4"></a>
The Python script works with a CSS script as input, where colors need to be defined like this:

```css
@define-color black #ffffff;
```
 
Each free line in the CSS code acts as a Backspace for the boxes in the output .png file.

## 5. Roadmap <a name="sec5"></a>

- [ ] Gather more opinions on colors.
- [ ] get the hackdornfish in there

