import os
from datetime import datetime

# List of all example cameras with categories, tags, and descriptions
reviews = [
    # Outdoor cameras
    {
        "title": "Arlo Ultra 2 Review",
        "category": "Outdoor Security Cameras",
        "tags": ["Arlo", "Outdoor", "Security"],
        "content": """2K resolution, wireless, color night vision, and AI motion detection. Ideal for high-end outdoor setups with smart home integration.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Reolink Argus 3 Pro Review",
        "category": "Outdoor Security Cameras",
        "tags": ["Reolink", "Outdoor", "Security"],
        "content": """Battery-powered with 2K video, spotlight, two-way audio, and app notifications. Flexible placement for homes or vacation properties.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Ring Floodlight Cam Review",
        "category": "Outdoor Security Cameras",
        "tags": ["Ring", "Outdoor", "Security"],
        "content": """1080p HD, motion-activated floodlight, two-way talk, Alexa compatible. Effective as a deterrent for entry points.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Nest Cam Outdoor Review",
        "category": "Outdoor Security Cameras",
        "tags": ["Nest", "Outdoor", "Security"],
        "content": """Weatherproof, 1080p, cloud storage, smart alerts via Google Home. Good for homeowners invested in the Google ecosystem.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Wyze Cam Outdoor Review",
        "category": "Outdoor Security Cameras",
        "tags": ["Wyze", "Outdoor", "Security"],
        "content": """Affordable, battery-powered, 1080p HD, night vision. Best for budget-conscious buyers seeking flexible outdoor coverage.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },

    # Indoor cameras
    {
        "title": "Reolink RLC-810A Review",
        "category": "Indoor Security Cameras",
        "tags": ["Reolink", "Indoor", "Security"],
        "content": """4K ultra HD, PoE wired, motion alerts, and night vision. Great for monitoring indoor spaces like offices and living rooms.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Wyze Cam v3 Review",
        "category": "Indoor Security Cameras",
        "tags": ["Wyze", "Indoor", "Security"],
        "content": """1080p HD, color night vision, cloud and local storage options. Affordable option for home monitoring.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    # Wireless cameras
    {
        "title": "Blink Outdoor Review",
        "category": "Wireless Security Cameras",
        "tags": ["Blink", "Wireless", "Security"],
        "content": """Battery-powered, wireless 1080p, motion detection, two-year battery life. Ideal for easy installation without wires.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    },
    {
        "title": "Arlo Pro 4 Review",
        "category": "Wireless Security Cameras",
        "tags": ["Arlo", "Wireless", "Security"],
        "content": """Wireless 2K HDR, color night vision, smart alerts, easy app control. Great for flexible placements indoors or outdoors.

- Video quality and performance  
- Setup and installation guidance  
- Smart home and app features  
- Pros and cons"""
    }
]

# Folder to save markdown files
output_folder = "./content/reviews"
os.makedirs(output_folder, exist_ok=True)

for review in reviews:
    # Generate a filename
    filename = review["title"].lower().replace(" ", "-").replace(".", "") + ".md"
    filepath = os.path.join(output_folder, filename)

    # TOML front matter
    toml_front_matter = f"""+++
title = "{review['title']}"
date = "{datetime.now().strftime('%Y-%m-%d')}"
categories = ["{review['category']}"]
tags = [{', '.join(f'"{tag}"' for tag in review['tags'])}]
+++
"""

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(toml_front_matter)
        f.write("\n")
        f.write(review["content"])

print(f"Generated {len(reviews)} review files in {output_folder}")
