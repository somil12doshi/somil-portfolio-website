# Somil Doshi - Portfolio Website

A modern, responsive portfolio website featuring liquid glass morphism effects, smooth animations, and a professional design.

## Features

- ✨ **Liquid Glass Morphism** - Beautiful glassmorphism effects throughout
- 🎨 **Modern UI** - Clean, professional design with gradient accents
- 📱 **Fully Responsive** - Optimized for mobile, tablet, and desktop
- 🎭 **Smooth Animations** - Engaging scroll animations and transitions
- 🧭 **Fixed Navbar** - Sticky navigation with active link highlighting
- ⚡ **Fast & Optimized** - Lightweight and performant

## Getting Started

### Prerequisites

- A modern web browser
- Python 3 (optional, for image conversion)

### Setup

1. **Convert Your Profile Image**

   The website expects a profile image at `images/profile.jpg`. To convert your HEIC images:

   ```bash
   # Install required Python packages
   pip install Pillow pillow-heif
   
   # Run the conversion script
   python convert_image.py
   ```

   This will automatically:
   - Find the first image in the `images/` folder
   - Convert it to JPG format
   - Crop it to a square (centered)
   - Resize it to 800x800 pixels
   - Save it as `images/profile.jpg`

   **Alternative:** You can manually convert your images using online tools or image editing software.

2. **Open the Website**

   Simply open `index.html` in your web browser, or use a local server:

   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server
   ```

   Then visit `http://localhost:8000` in your browser.

## Customization

### Update Your Information

Edit `index.html` to update:

- **About Section** - Your bio and statistics
- **Skills** - Your technical skills and technologies
- **Projects** - Your featured projects with descriptions
- **Experience** - Your work history
- **Contact** - Your contact information and social links

### Change Colors

Edit the CSS variables in `styles/main.css`:

```css
:root {
    --primary-color: #6366f1;    /* Main brand color */
    --secondary-color: #8b5cf6;  /* Secondary color */
    --accent-color: #ec4899;     /* Accent color */
    /* ... */
}
```

### Add Your Projects

Update the project cards in the Projects section with:
- Project images (replace gradient backgrounds)
- Project titles and descriptions
- Technology tags
- Links to live projects and GitHub repositories

## File Structure

```
Somil-Portfolio-Website/
├── index.html          # Main HTML file
├── styles/
│   └── main.css        # All styles and animations
├── scripts/
│   └── main.js         # JavaScript functionality
├── images/
│   ├── profile.jpg     # Your profile picture (generated)
│   └── *.heic          # Your source images
├── convert_image.py    # Image conversion script
└── README.md           # This file
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Technologies Used

- HTML5
- CSS3 (with CSS Grid, Flexbox, and Custom Properties)
- Vanilla JavaScript (ES6+)
- Google Fonts (Inter & Playfair Display)

## License

This project is open source and available for personal use.

## Contact

For questions or suggestions, feel free to reach out!

---

Built with ❤️ by Somil Doshi

