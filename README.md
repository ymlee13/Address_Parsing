# address_parsing
A fine-tuned Qwen2.5-3B-Instruct model for Hong Kong address parsing and formatting. This model splits messy address inputs into two structured lines using LoRA fine-tuning.

## 📋 Overview

This project fine-tunes Qwen2.5-3B-Instruct to parse and format Hong Kong addresses into two logical components (e.g., building/unit details in Line 1, street/district in Line 2). The model handles both English and Traditional Chinese addresses with high accuracy.

## 🚀 Features

- **Dual Language Support**: Handles English and Traditional Chinese addresses
- **Intelligent Splitting**: Splits addresses into two logical lines
- **Post-processing**: Includes fallback mechanisms and character-level correction
- **Batch Processing**: Efficient batch inference with GPU support
- **Fine-tuned with LoRA**: Lightweight adapter weights (~8MB)
- **4-bit Quantization**: Optimized for memory-efficient inference

## 📦 Repository Structure
address_parsing/
├── data/
│ ├── test_data/ # Test datasets
│ └── train_data.jsonl # Training data
├── Qwen2.5-3B-Instruct_Address_Formatter/ # LoRA adapters (on Hugging Face)
├── train_model.ipynb # Fine-tuning notebook
├── test_model.ipynb # Evaluation notebook
├── llm_parser.ipynb # Inference wrapper
├── jsonl_converter.ipynb # Data preparation
├── requirements.txt # Python dependencies
└── README.md


## 🛠️ Installation

### Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended)
- 16GB+ RAM (for training)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/ymlee13/address-parsing.git
cd address-parsing
