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
