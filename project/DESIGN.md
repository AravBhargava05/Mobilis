# Mobilis LLC Web Application

This project is a web application designed for Mobilis LLC, a biotech start-up, that includes dynamic, informative, and relevant information to help educate others on the company/product. It leverages Flask for backend functionality and a combination of HTML, CSS, Leaflet, and JavaScript for the frontend. The modular design with different files and folders ensures efficient development and maintainability, while the responsive interface enhances user experience and allows better reach to customers.

## Backend

The backend is implemented in Python using Flask, which handles routing and renders dynamic content with Jinja2 templates. Key routes include:
- `/` for the homepage
- `/problem` to discuss challenges
- `/product` for product details
- `/team` to showcase team members
- `/contact` for contact information

The `base.html` template serves as the foundation for all pages, providing a shared header, footer, and navigation structure. Dynamic placeholders like `{% block title %}` and `{% block content %}` allow seamless content updates.

## Frontend

The frontend is styled with `static/styles.css`, featuring responsive layouts built with flexbox and enhanced typography through Google Fonts.

### Features:
- **Responsive Design**: Achieved using CSS media queries and JavaScript for interactivity.
- **Mobile Navigation**: JavaScript toggles the mobile menu visibility, ensuring smooth navigation across devices.
- **Organized Media Assets**: Logos and externally hosted images are organized under the `static/` directory to maintain clarity and scalability.

## Key Technical Features

### Interactive Map
- Built using the Leaflet library, starting with the `L.map()` function to set up the map.
- OpenStreetMap tiles are added with the `L.tileLayer()` method, giving the map its base geographic layout.
- A custom `style()` function makes countries with available amputee data stand out with red borders and light coral fills, while others appear in gray.
- Popups, created using the `onEachFeature()` function and `layer.bindPopup()`, show detailed statistics and descriptions pulled from the `amputeeData` object whenever a country is clicked.
- The `getCountryInfo()` function ties everything together, matching the country name to its data.

### Size Calculator
- Uses a Python algorithm in `app.py` to calculate the corresponding model to the length of the residual limb that is input.
- The `product.html` page includes Jinja code to take the calculated model and display it on the website.

## CSS Design

The CSS design effectively leverages specific code to achieve a polished and responsive user interface:
- **Global Reset**: `* { margin: 0; padding: 0; box-sizing: border-box; }` ensures consistent styling across elements.
- **Responsive Layouts**: Media queries like `@media screen and (max-width: 900px)` hide `.nav-links` on smaller screens and display a `.menu-toggle` for a mobile-friendly hamburger menu.
- **Flexbox and Grid**:
  - Flexbox (`display: flex; justify-content: space-between;`) aligns navigation items in `.navbar`.
  - Grid layouts in `.reason-box` organize content into neat sections.
- **Interactive Effects**:
  - Hover effects: `transition: color 0.3s ease;` in `.nav-links a` smoothly changes link colors to `#FF2D55` on hover.
  - Buttons: Styled with rounded corners (`border-radius: 25px;`), color transitions, and scaling on hover (`transform: scale(1.05);`).
- **Hero Section**: A full-height video background (`#hero-video { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }`) layered beneath text with `z-index: -1`.
- **Map Styling**:
  - `#map`: Styled with a red border (`border: 2px solid #FF2D55;`), rounded corners (`border-radius: 12px;`), and shadows (`box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);`).
  - Popups: Designed with `.popup-content` using `font-family: 'Poppins', sans-serif;`, rounded corners, and subtle shadows.

## Conclusion

By combining these elements, we created a dynamic, interactive webpage that helps potential customers, investors, or the general public understand more about this issue and product. The design effectively communicates information while ensuring engagement and usability.
