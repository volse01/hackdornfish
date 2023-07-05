# hackdornfish
little color code for my desktop envrionment based on gruvbox.

## Table of content

[1. Idea](#sec1)\
[2. Light mode](#sec2)\
[3. Dark mode](#sec3)\
[4. The ominous Python script](#sec4)\
[5. Roadmap](#sec5)

## 1. Idea <a name="sec1"></a>   
The idea is simply explained: I am using Hyprland with Waybar and some Rofi applications, and I want them to look aesthetically pleasing. The rest of the configuration is stored in a private repository to ensure that sensitive information is not accidentally synced.

As someone who enjoys working outdoors, I value the ability to see my screen clearly even in bright sunlight. Therefore, I have developed a color set for both dark and light modes. My color scheme draws heavy inspiration from [gruvbox](https://github.com/morhetz/gruvbox), which is a well-known and functional color scheme in contrast with my own.

The names of the colors should be self-explanatory where bg 0-4 stands for background and fg 0-4 for foreground.

## 2. Light mode <a name="sec2"></a>
![Light mode colors](hackdornfish_light.png)

## 3. Dark mode <a name="sec3"></a>
![Dark mode colors](hackdornfish_dark.png)

## 4. Python scipt <a name="sec4"></a>
The python script works with a CSS script as input, in which a color needs to be defined as follows:

`@define-color black #ffffff;`
 
Each free line in the CSS code acts as a Backspace in the output .png file.

## 5. Roadmap <a name="sec5"></a>

- [x] get the python-script to work
- [ ] get third and forth opinon on colors
- [ ] get the hackdornfish in there

