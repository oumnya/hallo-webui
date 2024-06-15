#!/bin/bash

echo "Clone models"
git lfs install
git clone https://huggingface.co/fudan-generative-ai/hallo pretrained_models

echo "Install dependencies"
python3 -m venv venv
source venv/bin/activate
pip install -r requerements.txt
pip install -e . 

echo "Install GPU libraries"
pip install torch==2.2.2+cu121 torchaudio torchvision --index-url https://download.pytorch.org/whl/cu121
pip install onnxruntime-gpu

echo "Installation complete"
read -p "Press any key to continue..."