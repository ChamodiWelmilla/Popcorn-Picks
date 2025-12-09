🎬 Popcorn Picks 🍿
A movie recommendation app built with Streamlit and powered by TMDB API.

🚀 Getting Started
1. Clone the Repository
bash
git clone https://github.com/ChamodiWelmilla/Popcorn-Picks.git
cd Popcorn-Picks
2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:

bash
pip install -r requirements.txt
3. Fetch the Dataset
Large files (e.g., movies_list.pkl, similarity.pkl) are stored externally. Download them automatically by running:

bash
python download_data.py
This will fetch the required dataset from Google Drive and place it in your project directory.

4. Set Up TMDB API Key
Create a free account at The Movie Database (TMDB).

Navigate to Settings → API → Request an API Key.

Copy your API key.

In app.py, replace:

python
api_key = "Your API key here"
with your actual TMDB API key.

▶️ Run the App
Start the Streamlit app:

bash
streamlit run app.py
Open the provided local URL in your browser to explore recommendations.


📓 See notebooks/ for exploratory analysis and model building steps.
