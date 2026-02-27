🎨 ColorSnap

ColorSnap is a web app that extracts dominant colors from any image using unsupervised machine learning (K-Means clustering) and lets users click a color to copy its RGB value instantly.

Built with:
✔ Python
✔ Streamlit
✔ Scikit-learn K-Means
✔ HTML + JS for clipboard interaction

It’s designed for designers, developers, and creatives who want a fast and interactive way to get color palettes from images.

🚀 Features

🖼️ Upload any image for color analysis

🎯 Extract top dominant colors using K-Means clustering

👆 Click on a color to copy its RGB code to clipboard

📊 Simple, clean, interactive UI built with Streamlit

🧠 Powered by unsupervised learning (no labels needed)



📦 Getting Started
🎯 Prerequisites

Make sure you have:

Python 3.8+

pip

⚙️ Installation

Clone the repository:

git clone https://github.com/Mueez-khan/color_snap.git
cd color_snap



Run the app:

streamlit run app.py

This will open the app in your default browser.

🧠 How It Works

You upload an image.

The app reshapes the image into a matrix of RGB pixels.

K-Means algorithm clusters similar colors in the image.

Cluster centers represent the dominant colors.

These colors are shown on the UI with clickable boxes.

💡 Usage

Click Browse files and select your image.

Wait a moment while the app computes the color palette.

Click on any color tile to copy its RGB code.

🧪 Example

When you upload a photo of a landscape, ColorSnap might show something like:

rgb(34, 120, 200)
rgb(220, 50, 80)
rgb(10, 200, 140)

Click any card to copy that RGB value.



📌 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

💻 Built With

🐍 Python

📊 scikit-learn — K-Means clustering

🌐 Streamlit — Interactive web UI

💻 HTML + JavaScript — Clipboard interaction

📝 License

This project is open-source — feel free to use, modify, and share!