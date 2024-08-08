# Movie-Recommender



---

# 🎥 Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Table of Contents
- [📖 Overview](#overview)
- [✨ Features](#features)
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [🗂️ Project Structure](#project-structure)
- [🤝 Contributing](#contributing)
- [📝 License](#license)
- [📬 Contact](#contact)

## 📖 Overview

The Movie Recommender System is a web application built using Streamlit that allows users to explore and receive movie recommendations based on various algorithms. The system leverages machine learning models to provide recommendations and offers an intuitive and user-friendly interface with a dark theme for enhanced usability.

## ✨ Features

- **Personalized Recommendations**: Get movie suggestions based on your preferences.
- **Search Functionality**: 🔍 Easily search for your favorite movies.
- **Dark Theme**: 🖤 A visually appealing dark theme for comfortable usage.
- **Interactive UI**: User-friendly interface with Streamlit for seamless interaction.
- **Scalable**: Easily extendable to include more features and improve recommendation algorithms.
- **Cosine Similarity-Based Recommendations**: After clicking "Give Recommendation," the system provides 5 movie recommendations that are closest in cosine similarity after vectorizing the tags and selecting the top 5 closest matches.

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chayanC7mondal/Movie-Recommender.git
   cd Movie-Recommender
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the application:**

   ```bash
   streamlit run app.py
   ```

2. **Access the application:**

   Open your web browser and go to `http://localhost:8501` to interact with the Movie Recommender System.

3. **Explore and get recommendations:**

   - Use the app to search for movies, receive personalized recommendations, and explore various features.
   - After clicking "Give Recommendation," you'll get 5 movie recommendations that are closest in cosine similarity to the movie tags you selected.

## 🗂️ Project Structure

```
Movie-Recommender/
├── app.py                 # Main application file
├── data/                  # Dataset and related files
├── models/                # Pre-trained models and scripts
├── utils/                 # Utility scripts for data processing and model evaluation
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .streamlit/            # Streamlit configuration files (theme, etc.)
```

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to submit a pull request or open an issue.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Chayan Mondal - [LinkedIn](https://www.linkedin.com/in/chayanc7mondal/) - chayanC7mondal@gmail.com

Project Link: [https://github.com/chayanC7mondal/Movie-Recommender](https://github.com/chayanC7mondal/Movie-Recommender)

---

Created by **Chayan Mondal** ✨

