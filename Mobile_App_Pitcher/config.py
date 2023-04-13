import os

# This config.py file defines the paths to the various directories and files in the project, 
# as well as default parameters for the machine learning and natural language processing models.
# These default parameters can be used by the model_training.py script to train the models, 
# but can also be overridden with command line arguments or configuration files as needed.

# define the path to the project's root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# define the paths to the data directories
RAW_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'raw_data')
PROCESSED_DATA_DIR = os.path.join(ROOT_DIR, 'data', 'processed_data')
MODELS_DIR = os.path.join(ROOT_DIR, 'data', 'models')

# define the paths to the notebook and source code directories
NOTEBOOKS_DIR = os.path.join(ROOT_DIR, 'notebooks')
SRC_DIR = os.path.join(ROOT_DIR, 'src')

# define the paths to the test directory
TESTS_DIR = os.path.join(ROOT_DIR, 'tests')

# define the path to the requirements file
REQUIREMENTS_FILE = os.path.join(ROOT_DIR, 'requirements.txt')

# define the path to the README file
README_FILE = os.path.join(ROOT_DIR, 'README.md')

# define the default parameters for the machine learning model
DEFAULT_MODEL_PARAMS = {
    'learning_rate': 0.001,
    'num_epochs': 10,
    'batch_size': 32,
    'hidden_units': [64, 32],
    'dropout_rate': 0.3
}

# define the default parameters for the natural language model
DEFAULT_NLP_PARAMS = {
    'max_len': 100,
    'embedding_dim': 128,
    'num_epochs': 5,
    'batch_size': 32,
    'num_lstm_units': 64,
    'num_dense_units': 32,
    'dropout_rate': 0.2
}
