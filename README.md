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

## 📊 Performance Metrics

| Metric | Score (Typical) |
|--------|-----------------|
| Average Line 1 Similarity | 75-90% |
| Average Line 2 Similarity | 75-90% |
| Strict Both Lines Match | 60-75% |
| Inference Speed | ~0.5-1.0s/address |

### Prerequisites
- Python 3.9+
- CUDA-compatible GPU (24GB+ VRAM recommended)
- Git LFS (for Hugging Face uploads)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/ymlee13/address_parsing.git
cd address_parsing
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the base model (optional if you just want to test)**
```bash
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-3B-Instruct
```

## 📦 Model Weights

The fine-tuned LoRA adapter is available on Hugging Face Hub:
[**ymlee13/Qwen2.5-3B-Instruct_Address_Formatter**](https://huggingface.co/ymlee13/Qwen2.5-3B-Instruct_Address_Formatter)

The parser will automatically download the base model (`Qwen/Qwen2.5-3B-Instruct`) and the adapter from Hugging Face when you run the code for the first time.

## 🚀 Quick Start

### Training the Model

1. **Prepare your data**
```bash
python -c "from jsonl_converter import parse_database_file_to_nested_jsonl; parse_database_file_to_nested_jsonl('./data/database.txt', './data/database.jsonl')"
```

2. **Run training**
 ```bash
jupyter notebook train_model.ipynb
```

### Testing the Model
```bash
jupyter notebook test_model.ipynb
```

### Using the Parser
```python
from llm_parser import HKAddressParserLLM

# Initialize parser
parser = HKAddressParserLLM(
    base_model_path="Qwen/Qwen2.5-3B-Instruct",
    lora_path="ymlee13/Qwen2.5-3B-Instruct_Address_Formatter",
    conf_threshold=0.50,
    max_new_tokens=128
)

# Parse a single address
address = "九龍觀塘區雲漢街61號南寧大樓地庫01舖"
result = parser.parse(address)
print(f"Line 1: {result[1]}")
print(f"Line 2: {result[2]}")

# Batch parsing
addresses = [
    ("九龍觀塘區雲漢街61號南寧大樓地庫01舖", ""),
    ("ROOM 2107, 42/F, WINNING HEIGHTS, TSUEN WAN", ""),
]
results = parser.parse_batch(addresses, batch_size=2)
```
## 🎯 Demo
Try it yourself:
```python
from llm_parser import HKAddressParserLLM

parser = HKAddressParserLLM(
    base_model_path="Qwen/Qwen2.5-3B-Instruct",
    lora_path="ymlee13/Qwen2.5-3B-Instruct_Address_Formatter"
)

test_cases = [
    "九龍觀塘區雲漢街61號南寧大樓地庫01舖",
    "RM 2107, 42/F, WINNING HEIGHTS, 277 CASTLE PEAK RD, TSUEN WAN"
]

for addr in test_cases:
    result = parser.parse(addr)
    print(f"Input: {addr}")
    print(f"Line 1: {result[1]}")
    print(f"Line 2: {result[2]}")
    print("-" * 50)
```

## 📁 Project Structure
```text
address_parsing/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── train_model.ipynb        # Fine-tuning notebook
├── test_model.ipynb         # Testing and evaluation notebook
├── llm_parser.ipynb         # Inference wrapper notebook
├── jsonl_converter.ipynb    # Data conversion utility
├── data/
│   ├── database.txt         # Training data (input|line1|line2)
│   ├── database.jsonl       # Converted training data
│   ├── test_data/
│   │   └── test_data.txt    # Test data examples
│   └── gen_real_address.ipynb # Generate synthetic addresses
└── models/                  # Model storage (not in repo)
    ├── Qwen2.5-3B-Instruct/ # Base model
    └── Qwen2.5-3B-Instruct_Address_Formatter/ # Fine-tuned adapters
```

##🔧 Training (Optional)
If you want to retrain the model:
### 1. **Prepare your data**
```bash
# Convert txt to jsonl format
python -c "from jsonl_converter import parse_database_file_to_nested_jsonl; parse_database_file_to_nested_jsonl('./data/database.txt', './data/database.jsonl')"
```

### 2. **Run training**
```bash
jupyter notebook train_model.ipynb
```

### 3. **Evaluate the model**
```bash
jupyter notebook test_model.ipynb
```

### Training Configuration
- Base Model: Qwen/Qwen2.5-3B-Instruct
- Fine-tuning Method: LoRA (Low-Rank Adaptation)
- Quantization: 4-bit (NF4)
- Learning Rate: 2e-5
- Epochs: 3
- Batch Size: 4 (per device)
- Gradient Accumulation: 2
- LoRA Rank: 8
- LoRA Alpha: 16
- Target Modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

### Post-processing Features
- Character pooling and reconstruction
- Intelligent omission detection and re-insertion
- Language detection (Chinese/English)
- Traditional Chinese conversion
- English spell checking

##📊 Dataset
The model was trained on a dataset of 570+ Hong Kong addresses generated from real geospatial data (ALS-GeoJSON from HK government data portal). Each address is split into:
- Line 1: Specific location (floor, unit, building)
- Line 2: General location (street, district, region)
Data format:
```text
[original input] | [line 1] | [line 2]
```

##🤖 Inference Examples

### Chinese Address
Input:
```text
九龍觀塘區雲漢街61號南寧大樓地庫01舖
```

Output:
```text
Line 1: 南寧大樓地庫01舖
Line 2: 九龍觀塘區雲漢街61號
```

### English Address
Input:
```text
ROOM 2107, 42/F, WINNING HEIGHTS, 277 CASTLE PEAK ROAD, TSUEN WAN, NEW TERRITORIES
```

Output:
```text
Line 1: FLAT 2107, 42/F, WINNING HEIGHTS
Line 2: 277 CASTLE PEAK ROAD, TSUEN WAN, NEW TERRITORIES
```

## 📈 Performance Optimization

### For Tesla P40 / Pascal GPUs
The parser includes special handling for older GPUs:
- Disables Flash Attention
- Uses fp16 instead of 4-bit quantization when needed
- Memory-efficient batching

### Memory Usage
- Training: ~12-14GB VRAM
- Inference: ~6-8GB VRAM

## 📚 References

- Hong Kong Government ALS-GeoJSON Dataset: https://data.gov.hk/en-data/dataset/hk-dpo-als_01-als
- Qwen2.5 Model: https://huggingface.co/Qwen/Qwen2.5-3B-Instruct
- Hugging Face Transformers: https://github.com/huggingface/transformers
- PEFT Library: https://github.com/huggingface/peft

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- Qwen for the base model
- Hugging Face for the transformers library
- Hong Kong Government for the ALS-GeoJSON dataset

## 📧 Contact
- Author: ymlee13
- Hugging Face: @ymlee13
- GitHub: ymlee13
