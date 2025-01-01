# Neuraibu - Twitch AI Overlay using ollama and Flask

## English

This repository contains a Twitch AI Overlay application built with the Ollama API and Flask. It is designed to generate AI responses based on user input and display them in a Twitch stream using an HTML overlay.

### Features

- Interactive AI responses using the Ollama API
- Real-time display of AI responses in a Twitch stream
- Typing effect for a dynamic user experience

### Installing Ollama and the Model

1. **Install Ollama:**

   First, you need to install Ollama. Follow the instructions on the [official Ollama website](https://ollama.com) to download and set up Ollama on your machine. Ensure that you have the necessary system requirements.

2. **Install the Model:**

   Once Ollama is installed, you can install the `llama3:latest` model using the Ollama CLI. Run the following command in your terminal:

   ```bash
   ollama install llama3:latest
   ```

   Make sure you have an active internet connection, as the model will be downloaded from Ollama's repositories.

3. **Verify Installation:**

   After installation, verify that the model is correctly installed by listing the available models:

   ```bash
   ollama list
   ```

   You should see `llama3:latest` in the list of available models.


### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/twitch-ai-overlay.git
   cd twitch-ai-overlay
   ```

2. **Install Dependencies:**

   Make sure you have Python installed. Then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   Execute the script to start the Flask server:

   ```bash
   python index.py
   ```

4. **Access the Overlay:**

   Open your browser and navigate to `http://localhost:5000/overlay` to see the AI overlay in action.

### Usage

- **Testing AI Response:**

  Send a POST request to `http://localhost:5000/query` with a JSON payload containing the user's input:

  ```json
  {
      "input": "Hello, world!"
  }
  ```

- **Streaming Setup:**

  Use the overlay URL in Streamlabs or any streaming software to incorporate the AI responses into your Twitch stream.

## Français

Ce dépôt contient une application de superposition AI pour Twitch, construite avec l'API Ollama et Flask. Elle est conçue pour générer des réponses AI basées sur les entrées des utilisateurs et les afficher dans un stream Twitch à l'aide d'une superposition HTML.

### Caractéristiques

- Réponses AI interactives utilisant l'API Ollama
- Affichage en temps réel des réponses AI dans un stream Twitch
- Effet de frappe pour une expérience utilisateur dynamique

### Installation d'Ollama et du Modèle

1. **Installer Ollama :**

   Tout d'abord, vous devez installer Ollama. Suivez les instructions sur le [site officiel d'Ollama](https://ollama.com) pour télécharger et configurer Ollama sur votre machine. Assurez-vous d'avoir les exigences système nécessaires.

2. **Installer le Modèle :**

   Une fois Ollama installé, vous pouvez installer le modèle `llama3:latest` en utilisant le CLI Ollama. Exécutez la commande suivante dans votre terminal :

   ```bash
   ollama install llama3:latest
   ```

   Assurez-vous d'avoir une connexion internet active, car le modèle sera téléchargé depuis les dépôts d'Ollama.

3. **Vérifier l'Installation :**

   Après l'installation, vérifiez que le modèle est correctement installé en listant les modèles disponibles :

   ```bash
   ollama list
   ```

   Vous devriez voir `llama3:latest` dans la liste des modèles disponibles.

### Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/yourusername/twitch-ai-overlay.git
   cd twitch-ai-overlay
   ```

2. **Installer les dépendances :**

   Assurez-vous d'avoir Python installé. Puis installez les packages requis :

   ```bash
   pip install -r requirements.txt
   ```

3. **Exécuter l'application :**

   Lancez le script pour démarrer le serveur Flask :

   ```bash
   python index.py
   ```

4. **Accéder à la superposition :**

   Ouvrez votre navigateur et allez sur `http://localhost:5000/overlay` pour voir la superposition AI en action.

### Utilisation

- **Test de la réponse AI :**

  Envoyez une requête POST à `http://localhost:5000/query` avec une charge JSON contenant l'entrée de l'utilisateur :

  ```json
  {
      "input": "Bonjour, le monde!"
  }
  ```

- **Configuration pour le streaming :**

  Utilisez l'URL de superposition dans Streamlabs ou tout logiciel de streaming pour incorporer les réponses AI dans votre stream Twitch.


### Auteur

* PerrierBottle - [Github](https://github.com/PerrierBottle) - [Discord](https://discord.gg/PeA3vESxt7)

### Licence

Ce projet est sous licence MIT - Voir le fichier [LICENSE](LICENSE) pour plus de détails.

