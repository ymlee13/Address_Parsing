# address_parsing
[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-blue)](你的HF模型链接)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](你的GitHub仓库链接)

## 📖 项目简介 (Project Description)

这是一个基于 **Qwen2.5-3B-Instruct** 模型，使用 **LoRA** 技术微调而成的香港地址格式化工具。它能将杂乱、非结构化的香港地址文本，智能地拆分为 **行1 (Line 1)** 和 **行2 (Line 2)** 两个部分，适用于地址标准化、数据清洗等场景。

本项目包含了完整的数据处理、模型训练、测试评估和推理部署的代码。

**主要特点:**
*   🧠 **基于LLM**: 利用 Qwen2.5-3B 强大的语义理解能力。
*   ⚡ **高效微调**: 使用 LoRA (Low-Rank Adaptation) 技术，在单卡GPU上即可完成训练。
*   🌏 **双语支持**: 能够处理中文（繁体/简体）和英文地址。
*   🧹 **完整工具链**: 从真实数据生成、数据格式转换，到模型训练、评估和推理，提供全套代码。

## 🚀 快速开始 (Quick Start)

### 环境准备 (Environment Setup)
1.  **克隆仓库 (Clone the repo)**
    ```bash
    git clone https://github.com/ymlee13/HongKong-Address-Formatter.git
    cd HongKong-Address-Formatter
