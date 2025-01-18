
# Jesse Livermore LLM Chatbot

This project aims to develop a chatbot that emulates the trading philosophies and insights of the legendary stock trader, Jesse Livermore. By leveraging transformer-based models, the chatbot provides responses inspired by Livermore's principles.

## Repository Structure

- `app.py`: The main application script that initializes and runs the chatbot interface.
- `helper.py`: Contains auxiliary functions to support the chatbot's operations.
- `tf2_tpu_transformer_chatbot.ipynb`: A Jupyter Notebook detailing the development and training process of the transformer-based chatbot model using TensorFlow 2.
- `reminiscences_of_a_stock_operator_qa.csv`: A dataset comprising question-and-answer pairs extracted from Jesse Livermore's book, "Reminiscences of a Stock Operator," serving as training data for the model.
- `requirements.txt`: Lists the Python dependencies required to run the project.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ParichayDidwania/Jesse-Livermore-LLM.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Jesse-Livermore-LLM
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.x installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Execute the main application script to start the chatbot:
   ```bash
   python app.py
   ```

## Usage

Once the application is running, you can interact with the chatbot through the provided interface. The chatbot responds based on the philosophies and insights of Jesse Livermore, as derived from the training data.

## Contributing

Contributions are welcome! Feel free to fork the repository, make enhancements, and submit pull requests. For major changes, please open an issue first to discuss the proposed modifications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the works and trading philosophies of Jesse Livermore.
- Utilizes TensorFlow 2 for model development.
