# Hong Kong Address Parser

[![GitHub](https://img.shields.io/badge/GitHub-ymlee13/address_parser-blue)](https://github.com/ymlee13/address_parser)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-ymlee13/Qwen2.5--3B--Instruct--Address--Formatter-yellow)](https://huggingface.co/ymlee13/Qwen2.5-3B-Instruct_Address_Formatter)

## 📝 Overview

A fine-tuned **Qwen2.5-3B-Instruct** model for Hong Kong address parsing and formatting. The model splits unstructured address text into two structured lines following Hong Kong addressing conventions.

### Features

- 🏠 **Address Parsing**: Splits addresses into Line 1 (specific details) and Line 2 (general location)
- 🇭🇰 **Hong Kong Focus**: Specialized for Hong Kong address formats (both English and Chinese)
- 🔄 **Multi-language Support**: Handles English, Traditional Chinese, and Simplified Chinese
- 🎯 **High Accuracy**: Fine-tuned on real Hong Kong address data
- ⚡ **Efficient**: 4-bit quantization support for memory-efficient inference

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ymlee13/address_parser.git
cd address_parser

# Install dependencies
pip install -r requirements.txt
```
### Download the Model
The fine-tuned LoRA adapters are available on Hugging Face:
```bash
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model and adapters
base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-3B-Instruct",
    device_map="auto"
)
model = PeftModel.from_pretrained(base_model, "ymlee13/Qwen2.5-3B-Instruct_Address_Formatter")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct")
```

### Usage
```bash
from src.parser import HKAddressParserLLM

parser = HKAddressParserLLM(
    base_model_path="Qwen/Qwen2.5-3B-Instruct",
    lora_path="ymlee13/Qwen2.5-3B-Instruct_Address_Formatter"
)

# Parse a single address
address = "九龍觀塘區雲漢街61號南寧大樓地庫01舖"
result = parser.parse(address)
print(f"Line 1: {result[1]}")
print(f"Line 2: {result[2]}")

# Parse batch
addresses = [
    ("ROOM 2107, 42/F, WINNING HEIGHTS, 277 CASTLE PEAK ROAD, TSUEN WAN", ""),
    ("九龍深水埗區長沙灣道833號長沙灣廣場二期5樓", "")
]
results = parser.parse_batch(addresses, batch_size=2)
```

### 📊 Model Performance

### Project Structure

```bash
address_parser/
├── src/                    # Source code
│   ├── parser.py          # Main parser class
│   ├── train.py           # Training script
│   ├── test.py            # Testing script
│   └── utils.py           # Utilities
├── notebooks/             # Jupyter notebooks
│   ├── train_model.ipynb
│   ├── test_model.ipynb
│   ├── llm_parser.ipynb
│   └── jsonl_converter.ipynb
├── data/                  # Data files
│   ├── raw/              # Raw training data
│   ├── processed/        # Processed JSONL data
│   └── test/             # Test data
├── scripts/              # Utility scripts
├── requirements.txt      # Dependencies
└── README.md            # This file
```
