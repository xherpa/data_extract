# 📊 Facebook Data Extraction Project

Welcome to the **Data Extraction** project. This project is developed in **Python** and enables effective and efficient extraction of public data from Facebook using its API, along with customer and lead data from HubSpot API. The goal is to store and process this information for analysis and detailed report generation, supporting comprehensive insights for social media and client management.

---

## 🚀 Description

This project facilitates the retrieval of data such as posts, comments, and reactions from public pages on Facebook, as well as customer and lead data from HubSpot API. The extracted data is stored in a database for further analysis, enabling the generation of accurate reports useful for social media analysis, market research, tracking interactions, and managing client information.

---

## 📂 Repositories

Here are the links to the different repositories for the project:

- Main Repository: [Source Code on GitHub](https://github.com/usuario/facebook_extract)
- Documentation Repository: [Documentation on GitHub](https://github.com/tuusuario/repo-documentacion)

---

## 👥 Collaborators

This project was created by:
- **AxierPer**
  - **[AxierPer](https://github.com/AxierPer)** - [axierperlaz2018@gmail.com](mailto:axierperlaz2018@gmail.com)
  - [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/axier-perlaza-044866274/)
- **SFrancoH**
  - **[SFrancoH](https://github.com/SFrancoH)** - [sebastianfrancoh@hotmail.com](mailto:sebastianfrancoh@hotmail.com)
  - [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sebastian-felipe-franco-herrera/)

---

## 🔧 Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![HubSpot](https://img.shields.io/badge/HubSpot-FF7A59?style=for-the-badge&logo=hubspot&logoColor=white)
---

## 📦 Installation and Setup

### Prerequisites

- Python 3.12 or higher
- poetry 1.8.4 or higher

### 📦 Initial Setup

1. **Install poetry**:
    ```bash
    pip install poetry
    ```

#### Project Installation

1. **Clone the main repository**:
   ```bash
   git clone https://github.com/usuario/data_extract
   cd data_extract
   ```

2. **Install project dependencies**:
    ```bash
    poetry install
    ```

3. **Activate the virtual environment**:
    ```bash
    poetry shell
    ```

4. **Set up environment variables**:
- Copy the `.env.example` file to `.env`: 
    ```bash
    cp .env.example .env
    ```

- Edit the `.env` file and add your Facebook API access token and other necessary parameters: 
    ```bash
    FACEBOOK_API_TOKEN=to_token_de_acceso
    FACEBOOK_PAGE_ID=id_cuenta_aqui
    ```

5. **Run the project**:
    ```bash
    # LINUX
    python3 main.py
    ```

    ```bash
    # WINDOWS
    python main.py
    ```


# 📝 Usage
This project enables multiple data extractions from both the Facebook API and HubSpot API. The data is stored in a database and organized by date, allowing efficient searches and analysis.

- **Post Extraction**: Retrieves posts from a specific page on Facebook.
- **Comment Extraction**: Obtains comments from specific posts.
- **Reaction Extraction**: Records reactions on posts from the page.
- **Customer Data Extraction**: Retrieves customer information from HubSpot API, including essential details to support client management and insights.
- **Lead Data Extraction**: Captures lead information from HubSpot, allowing for effective lead tracking and analysis of potential clients.

With these capabilities, the project offers a comprehensive approach to managing and analyzing both social media interactions and customer relationship data.

# 📖 Documentation

For more details on the implementation and usage of the project, refer to the Documentation Repository.


# 🚨 Common Errors
1. **Authentication Error**: Ensure that the access token is correct and has the necessary permissions. Check the .env file.
2. **API Rate Limit**: If you encounter a rate limit error, wait for a while or implement a pause logic to avoid this issue.
3. **Incomplete Data**: Some data may not be available due to API restrictions. Make sure the token has read permissions for the required pages and elements.


# 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.


# 📬 Contact
If you have any questions or suggestions, feel free to contact the collaborators:

AxierPer - axierperlaz2018@gmail.com
SFrancoH - sebastianfrancoh@hotmail.com


Made with ❤️ in Python.
-
