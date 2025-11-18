#!/usr/bin/env python3
"""
Image conversion script to convert HEIC images to JPG and crop them to square format.
Requires: pip install Pillow pillow-heif
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed. Install it with: pip install Pillow")
    sys.exit(1)

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    print("Warning: pillow-heif is not installed. HEIC files won't be supported.")
    print("Install it with: pip install pillow-heif")
    heif_support = False
else:
    heif_support = True


def crop_to_square(image_path, output_path, size=800):
    """Crop image to square, centered, and resize to specified size."""
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Get the smaller dimension
        min_dim = min(width, height)
        
        # Calculate crop box (center crop)
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        
        # Crop to square
        cropped = img.crop((left, top, right, bottom))
        
        # Resize to target size
        resized = cropped.resize((size, size), Image.Resampling.LANCZOS)
        
        # Convert to RGB if necessary (for JPG)
        if resized.mode != 'RGB':
            rgb_image = resized.convert('RGB')
        else:
            rgb_image = resized
        
        # Save as JPG
        rgb_image.save(output_path, 'JPEG', quality=95, optimize=True)
        print(f"✓ Successfully converted {image_path.name} to {output_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error processing {image_path.name}: {str(e)}")
        return False


def main():
    # Get the images directory
    script_dir = Path(__file__).parent
    images_dir = script_dir / "images"
    output_path = images_dir / "profile.jpg"
    
    if not images_dir.exists():
        print(f"Error: Images directory not found at {images_dir}")
        sys.exit(1)
    
    # Find HEIC or other image files
    image_extensions = ['.heic', '.HEIC', '.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(list(images_dir.glob(f"*{ext}")))
    
    if not image_files:
        print("No image files found in the images directory.")
        sys.exit(1)
    
    # Filter out the output file if it exists
    image_files = [f for f in image_files if f.name != "profile.jpg"]
    
    if not image_files:
        print("No source images found (excluding existing profile.jpg).")
        sys.exit(1)
    
    # Use the first image found
    source_image = image_files[0]
    
    # Check if it's HEIC and we have support
    if source_image.suffix.lower() in ['.heic'] and not heif_support:
        print(f"Error: Cannot process HEIC file {source_image.name} without pillow-heif.")
        print("Please install it with: pip install pillow-heif")
        sys.exit(1)
    
    print(f"Processing: {source_image.name}")
    print(f"Output: {output_path.name}")
    
    if crop_to_square(source_image, output_path):
        print(f"\n✓ Profile image created successfully at: {output_path}")
        print("You can now use this image in your portfolio website!")
    else:
        print("\n✗ Failed to create profile image.")
        sys.exit(1)


if __name__ == "__main__":
    main()

