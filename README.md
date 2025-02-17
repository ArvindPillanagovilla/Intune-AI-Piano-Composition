# Intune-AI Powered Piano Composition

## Overview

The fusion of music and technology has led to remarkable advancements in the field of musical composition, particularly through the application of artificial intelligence. This project, **Intune-AI Powered Piano Composition**, aims to address the challenges faced in traditional piano composition methods by leveraging cutting-edge AI techniques.

Traditional piano composition often relies heavily on human expertise, which can lead to limitations in creativity, subjective barriers, and accessibility issues. Existing tools may be restrictive and time-consuming, especially for aspiring musicians. Recognizing these challenges, this project provides an AI-driven solution to democratize piano composition, enabling effortless creation of original pieces for users of all skill levels.

## Features

- **AI-Driven Composition**: Utilizes advanced AI techniques to generate original piano compositions.
- **Accessibility**: Designed for both professional musicians and hobbyists.
- **Innovative Algorithms**: Employs Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) architectures.

## Approach

This project introduces an innovative approach to music composition by employing artificial intelligence techniques, with a specific focus on Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) architectures. These advanced neural network models are particularly well-suited for understanding and generating sequential data, making them ideal for composing music, which is inherently a sequence of notes, chords, and rhythms.

## Implementation

### Neural Network Architecture

- **Recurrent Neural Networks (RNNs)**: Used for their ability to handle sequential data.
- **Long Short-Term Memory (LSTM)**: Enhances the RNNs by addressing the vanishing gradient problem, making them more effective for long-term dependencies in music sequences.

### Dataset Preparation

- **Data Collection**: Gathering a diverse set of piano compositions.
- **Preprocessing**: Cleaning and structuring the data for training.

### Training Pipeline

- **Model Training**: Training the neural network models on the prepared datasets.
- **Evaluation**: Assessing the performance and fine-tuning the models.

## Getting Started

### Prerequisites

- Python 3.x
- TensorFlow or PyTorch
- Music21 library
- MuseScore application

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Adithya2357/INTUNE-AI-MUSIC-COMPOSITION.git
    ```
2. Navigate to the project directory:
    ```bash
    cd INTUNE-AI-MUSIC-COMPOSITION
    ```

### Usage
1. Run the preprocess file:
   ```bash
   python preprocess.py
   ```
2. Run the training script:
    ```bash
    python train.py
    ```
3. Generate a new composition:
    ```bash
    python melodygenerator.py
    ```
4.  Run display.py to open the generated .mid file in MuseScore for easy viewing and editing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
